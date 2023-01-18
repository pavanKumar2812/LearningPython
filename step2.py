
class Item:
    pay_rate = 0.8 # the pay rate after 20% discount
    '''
    def __init__(self):
        print("I AM CREATED...!")
        # the init method or constructor pass the object as the first arguments to itself
    '''
    def __init__(self,name: str,price,brand,model,quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"quantity {quantity} is not greater than or equal to zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.brand = brand
        self.model = model
        self.quantity = quantity
        # print(f"Namaste your item is added to cart {self.name}")
        print(f"Price of that {self.name} is {self.price}")
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        # self.price = self.price * Item.pay_rate
        self.price = self.price * self.pay_rate

item1 = Item("Phone",2200,"Samsung","A53",23)
item1.apply_discount()
print(item1.price)

item2 = Item("Laptop",1000,"DELL","XPS",3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)
''' 
item2 = Item("Laptop",99000,"Apple","Mac M1",6)
item2.had_NumPad = False

print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print(Item.__dict__) # All the attributes for class level
print(item1.__dict__) # All the attributes for instance level
'''