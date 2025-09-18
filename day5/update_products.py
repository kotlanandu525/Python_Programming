# update_stock.py
from supabase import create_client, Client # type: ignore
from dotenv import load_dotenv # type: ignore
import os
 
load_dotenv()
 
url = os.getenv("supabaseUrl")
key = os.getenv("supabaseKey")
sb: Client = create_client(url, key)
 
def update_stock(product_id, new_stock):
    resp = sb.table("products").delete({"stock": new_stock}).eq("product_id", product_id).execute()
    return resp.data
 
if __name__ == "__main__":
    pid = int(input("Enter product_id to update: ").strip())
    new_stock = int(input("Enter new stock value: ").strip())
 
    updated = update_stock(pid, new_stock)
    if updated:
        print("Updated record:", updated)
    else:
        print("No record updated — check product_id.")
 
 