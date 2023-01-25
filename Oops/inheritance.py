import csv
class Item:
    pay_rate = 0.8  # The pay rate after 20% discount

    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_int(num):
        # we will count out the floats that are point zero
        # for example: 10.0, 15.0
        if isinstance(num, float):
            # count out the floats that are zero
            return num.is_integer();
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name},{self.price},{self.quantity}')"

class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to have access to all attributes / methods
        super().__init__(name, price, quantity)
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


phone1 = Phone("Samsung S22",50999,5,1)
#print(phone1.calculate_total_price())
phone2 = Phone("iphone 13",59999,9,1)
#print(phone2.calculate_total_price())

print(Item.all)
print(Phone.all)