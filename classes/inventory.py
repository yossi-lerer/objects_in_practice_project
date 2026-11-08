class Inventory:
    def __init__(self) -> None:
        self.__products = []

    def add(self, product):
        if self.find(product.name) != None:
            raise ValueError(f"{product.name} already exists")
        self.__products.append(product)
    
    def find(self, name_product):
        for product in self.__products:
            if product.name == name_product:
                return product
        return None
    def by_value(self):
        sort = sorted(self.__products,key=lambda p: p.total_value(), reverse=True)
        return sort
    @property
    def total_value(self):
        total = 0
        for product in self.__products:
            total += product.total_value()
        return total