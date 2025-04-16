# app/file_loader.py
import json
product_data = {}

def load_product_data(file):
    global product_data
    product_data = json.load(file)

def get_product_info():
    return json.dumps(product_data, indent=2) if product_data else ""