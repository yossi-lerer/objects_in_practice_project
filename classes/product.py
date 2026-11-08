class Product:
    def __init__(self, name,  price, quantity=0):
        self.__name = name
        self.__quantity = quantity
        self.__price = self.price = price

    @property
    def name(self):
        return self.__name

    @property
    def quantity(self):
        return self.__quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 1:
            raise ValueError("price must be positive")
        self.__price = value

    def add_stock(self, amount):
        if amount < 1:
            raise ValueError("amount must be positive")
        self.__quantity += amount
    
    def sell(self, amount):
        if amount > self.quantity:
            raise ValueError(f"not enough {self.name}")
        self.__quantity -= amount
        
    def total_value(self):
        return self.quantity * self.price
    
    def __str__(self) -> str:
        return f"{self.name}: {self.price} x {self.quantity} = {self.price * self.quantity}"