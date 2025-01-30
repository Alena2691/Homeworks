class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
         return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "Файл не найден."

    def add(self, *products):
        existing_products = {}
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    name, weight, category = line.strip().split(', ')
                    existing_products[(name, category)] = float(weight)
        except FileNotFoundError:
            pass

        for product in products:
            key = (product.name, product.category)
            if key in existing_products:
                existing_products[key] += product.weight
                print(f'Продукт {product.name} уже был в магазине, его общий вес теперь равен {existing_products[key]}')
            else:
                existing_products[key] = product.weight

        with open(self.__file_name, 'w') as file:
            for (name, category), weight in existing_products.items():
                file.write(f'{name}, {weight}, {category}\n')
            for (name, category), weight in existing_products.items():
                print(f'{name}, {weight}, {category}')
