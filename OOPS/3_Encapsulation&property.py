class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Price must be greater than zero!")
            return
        self._price = new_price
    
laptop = Product("Laptop", 999.99)
print(laptop.price)
laptop.price = 850.00
print(laptop.price)
laptop.price = -50.00
print(laptop.price)