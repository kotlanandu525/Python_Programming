# add_product.py
import os
from supabase import create_client, Client # type: ignore #pip install supabase
from dotenv import load_dotenv # type: ignore # pip install python-dotenv
 
load_dotenv()
 
url = os.getenv("supabaseUrl")
key = os.getenv("supabaseKey")
sb: Client = create_client(url, key)
 
def add_product(name, sku, price, stock):
    payload = {"name": name, "sku": sku, "price": price, "stock": stock}
    resp = sb.table("products").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    name = input("Enter product name: ").strip()
    sku = input("Enter SKU: ").strip()
    price = float(input("Enter price: ").strip())
    stock = int(input("Enter stock: ").strip())
 
    created = add_product(name, sku, price, stock)
    print("Inserted:", created)
 
 