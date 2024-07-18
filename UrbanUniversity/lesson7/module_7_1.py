import os


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        if not os.path.exists(self.__file_name):
            open(self.__file_name, 'w').close()
        with open(self.__file_name) as file:
            return ''.join(file.readlines())

    def add(self, *products):
        for product in products:
            prods = self.get_products()
            if product.name in prods:
                print(f"Продукт '{product.name}' уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())
