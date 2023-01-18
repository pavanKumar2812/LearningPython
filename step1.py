'''
print("Hi Namaste :)")

item1 = "Phone"
item1_price = 75000
item1_brand = "Apple"
item1_model = "iphone 13"

print(type(item1))
print(type(item1_price))
print(type(item1_brand))
print(type(item1_model))

# ========================================
class Item:
    pass

item1 = Item()
item1.price = 2200
item1.brand = "Samsung"
item1.model = "A53"
item1.stock = 23

print(type(item1))
print(type(item1.price))
print(type(item1.brand))
print(type(item1.model))
print(type(item1.stock))

random_string = "india"
print(random_string.upper())

#=====================================


class Item:
    def calculate_total_price(self,x,y):
        return x * y

item1 = Item()
item1.price = 22000
item1.brand = "Samsung"
item1.model = "A53"
item1.stock = 23
print(item1.calculate_total_price(item1.price, item1.stock))

item2 = Item()
item2.price = 75000
item2.brand = "Apple"
item2.model = "iphone 13"
item2.stock = 9
print(item2.calculate_total_price(item2.price , item2.stock))
'''