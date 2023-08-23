#ChatGPTexcel

import openpyxl
import random
from datetime import datetime, timedelta

# Create a new workbook and select the default sheet
wb = openpyxl.Workbook()
ws = wb.active

# Write headers
ws.append(["Product Name", "Price", "Quantity", "Sale Date"])

# List of sample product names and prices
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Monitor"]
prices = [800, 600, 400, 100, 200]

# Generate and write random sales data
for _ in range(100):
    product_name = random.choice(products)
    price = random.choice(prices)
    quantity = random.randint(1, 10)
    sale_date = datetime.now() - timedelta(days=random.randint(0, 365))
    
    ws.append([product_name, price, quantity, sale_date])

# Save the workbook to the specified path
file_path = 'c:\\work\\sales.xlsx'
wb.save(file_path)

print(f"Sales data has been saved to '{file_path}'.")
