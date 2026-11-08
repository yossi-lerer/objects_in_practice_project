from classes.inventory import Inventory
from classes.product import Product

shop = Inventory()
shop.add(Product("Pen", 5, 10))
shop.add(Product("Bag", 60, 2))
shop.add(Product("Notebook", 12, 5))

shop.find("Pen").sell(4) # type: ignore
shop.find("Bag").add_stock(1) # type: ignore

try:
    shop.find("Notebook").sell(50) # type: ignore
except ValueError as error:
    print("error:", error)
 
try:
    shop.add(Product("Pen", 7))
except ValueError as error:
    print("error:", error)
 
try:
    shop.find("Bag").price = -3 # type: ignore
except ValueError as error:
    print("error:", error)
 
for product in shop.by_value():
    print(product)
print("Total:", shop.total_value)
