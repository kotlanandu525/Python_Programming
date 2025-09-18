
"""
librarymanagementsystem.py

Library Management System using Supabase Python client.
Features:
 - Register members
 - Add/update/delete books
 - Borrow/Return (transaction-like via Supabase API)
 - Reports: overdue, most-borrowed
"""

import os
from dotenv import load_dotenv # type: ignore
from supabase import create_client, Client # type: ignore
from tabulate import tabulate # type: ignore
from datetime import datetime, timedelta

# Load Supabase credentials
load_dotenv()
url = os.getenv("supabaseUrl")
key = os.getenv("supabaseKey")
sb: Client = create_client(url, key)

# --- Helpers ---
def print_table(rows):
    if not rows:
        print("(no rows)")
        return
    headers = list(rows[0].keys())
    table = [[row.get(h) for h in headers] for row in rows]
    print(tabulate(table, headers=headers, tablefmt="psql"))


def add_member(name, email):
    return sb.table("members").insert({"name": name, "email": email}).execute().data

def update_member_email(member_id, new_email):
    return sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute().data

def delete_member(member_id):
    borrows = sb.table("borrow_records").select("*").eq("member_id", member_id).execute().data
    if borrows:
        raise ValueError("Cannot delete member: borrow records exist.")
    return sb.table("members").delete().eq("member_id", member_id).execute().data

def show_member(identifier):
    if "@" in str(identifier):
        member = sb.table("members").select("*").eq("email", identifier).execute().data
    else:
        member = sb.table("members").select("*").eq("member_id", int(identifier)).execute().data
    if not member:
        return None, []
    member = member[0]
    borrows = (
        sb.table("borrow_records")
        .select("*, books(title, author)")
        .eq("member_id", member["member_id"])
        .order("borrow_date", desc=True)
        .execute()
        .data
    )
    return member, borrows

# --- Books ---
def add_book(title, author, category, stock=1):
    return sb.table("books").insert({"title": title, "author": author, "category": category, "stock": stock}).execute().data

def list_books():
    return sb.table("books").select("*").order("title").execute().data

def search_books(term):
    return sb.table("books").select("*").ilike("title", f"%{term}%").execute().data

def update_book_stock(book_id, new_stock):
    return sb.table("books").update({"stock": new_stock}).eq("book_id", book_id).execute().data

def delete_book(book_id):
    borrows = sb.table("borrow_records").select("*").eq("book_id", book_id).execute().data
    if borrows:
        raise ValueError("Cannot delete book: borrow records exist.")
    return sb.table("books").delete().eq("book_id", book_id).execute().data

# --- Borrow / Return ---
def borrow_book(member_id, book_id):
    # Check stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute().data
    if not book:
        raise ValueError("Book not found")
    if book[0]["stock"] < 1:
        raise ValueError("No stock available")

    # Decrement stock
    sb.table("books").update({"stock": book[0]["stock"] - 1}).eq("book_id", book_id).execute()

    # Insert borrow record
    return sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute().data

def return_book(member_id, book_id):
    borrow = (
        sb.table("borrow_records")
        .select("*")
        .eq("member_id", member_id)
        .eq("book_id", book_id)
        .is_("return_date", None)
        .limit(1)
        .execute()
        .data
    )
    if not borrow:
        raise ValueError("No active borrow record")

    record_id = borrow[0]["record_id"]

    # Set return_date
    sb.table("borrow_records").update({"return_date": datetime.utcnow().isoformat()}).eq("record_id", record_id).execute()

    # Increment stock
    book = sb.table("books").select("stock").eq("book_id", book_id).execute().data[0]
    sb.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()

    return {"record_id": record_id, "returned": True}

# --- Reports ---
def overdue(days=14):
    cutoff = (datetime.utcnow() - timedelta(days=days)).isoformat()
    return (
        sb.table("borrow_records")
        .select("*, members(name), books(title)")
        .is_("return_date", None)
        .lt("borrow_date", cutoff)
        .execute()
        .data
    )

def most_borrowed(limit=10):
    # Supabase client doesn’t support GROUP BY directly, so we fetch and aggregate manually
    records = sb.table("borrow_records").select("book_id, books(title, author)").execute().data
    counts = {}
    for r in records:
        book_id = r["book_id"]
        key = (book_id, r["books"]["title"], r["books"]["author"])
        counts[key] = counts.get(key, 0) + 1
    sorted_books = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]
    return [{"book_id": b[0], "title": b[1], "author": b[2], "times_borrowed": c} for (b, t, a), c in sorted_books]

# --- CLI ---
def menu():
    print("""
Library CLI - Supabase
1) Register member
2) Add book
3) List all books
4) Search books
5) Show member details & borrows
6) Update book stock
7) Update member email
8) Delete member
9) Delete book
10) Borrow book
11) Return book
12) Reports: overdue
13) Reports: most borrowed
0) Exit
""")

def run_cli():
    while True:
        menu()
        choice = input("Choice: ").strip()

        try:
            if choice == "1":
                name = input("Name: ").strip()
                email = input("Email: ").strip()
                print(add_member(name, email))

            elif choice == "2":
                title = input("Title: ").strip()
                author = input("Author: ").strip()
                category = input("Category: ").strip()
                stock = int(input("Stock: ").strip() or "1")
                print(add_book(title, author, category, stock))

            elif choice == "3":
                print_table(list_books())

            elif choice == "4":
                term = input("Search term: ").strip()
                print_table(search_books(term))

            elif choice == "5":
                identifier = input("Enter member_id or email: ").strip()
                member, borrows = show_member(identifier)
                if not member:
                    print("Member not found.")
                else:
                    print_table([member])
                    print("Borrows:")
                    print_table(borrows)

            elif choice == "6":
                book_id = int(input("Book ID: ").strip())
                new_stock = int(input("New stock: ").strip())
                print(update_book_stock(book_id, new_stock))

            elif choice == "7":
                member_id = int(input("Member ID: ").strip())
                new_email = input("New email: ").strip()
                print(update_member_email(member_id, new_email))

            elif choice == "8":
                member_id = int(input("Member ID to delete: ").strip())
                print(delete_member(member_id))

            elif choice == "9":
                book_id = int(input("Book ID to delete: ").strip())
                print(delete_book(book_id))

            elif choice == "10":
                member_id = int(input("Member ID: ").strip())
                book_id = int(input("Book ID: ").strip())
                print(borrow_book(member_id, book_id))

            elif choice == "11":
                member_id = int(input("Member ID: ").strip())
                book_id = int(input("Book ID: ").strip())
                print(return_book(member_id, book_id))

            elif choice == "12":
                days = int(input("Overdue days (default 14): ").strip() or "14")
                print_table(overdue(days))

            elif choice == "13":
                limit = int(input("Top N (default 10): ").strip() or "10")
                print_table(most_borrowed(limit))

            elif choice == "0":
                print("Bye!")
                break

            else:
                print("Invalid option")
        except Exception as e:
            print("ERROR:", str(e))

if __name__ == "__main__":
    run_cli()
