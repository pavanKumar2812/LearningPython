from item import Item
from phone import Phone

#Item.instantiate_from_csv()
#print(Item.all)
'''
item1 = Item("MyItem",750)
item1.name = "OtherItem"

print(item1.name)
 '''
item1 = Item("karna",750)

#print(item1.name)

#item1.name = "Pavanubguiorgeyuiogbtuob"
#print(item1.name)
'''
print(item1.price)
item1.apply_increment(0.2)
print(item1.price)
item1.apply_discount()
print(item1.price)
item1.send_email()
 '''
# Inheritance

item2 = Phone("Vest",1000,3)
item2.send_email()
item2.apply_increment(0.2)
print(item2.price)


