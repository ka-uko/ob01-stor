class Store():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}
        #добавление товара
    def add_item(self, item, price):
        self.items[item] = price
        print(f'Товар {item} добавлен в магазин {self.name}')
        #удаление товара
    def delete_item(self, item, price):
        if item in self.items:
            del self.items[item]
            print(f'Товар {item} удален из магазина {self.name}')
        else:
            print('Товар не найден в списке этого магазина')

    def get_price(self, item):
        print(f'Цена товара {self.items.get(item)} р.')

    def change_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
            print(f'Цена товара {item} обновлена в магазине {self.name}')
        else:
            print('Товар не найден в списке этого магазина')

store1 = Store('One', 'Яблоневая 15')
store2 = Store('Two', 'Вишневая 10')
store3 = Store('Three', 'Черничная 4')

