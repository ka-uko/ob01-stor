class Store():
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress
        self.items = {}
        #добавление товара
    def add_item(self, item, price):
        self.items[item] = price
        print(f'Товар: {item} добавлен в магазин {self.name}')
        #удаление товара
    def delete_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f'Товар: {item} -удален из магазина {self.name}')
        else:
            print(f'Товар: {item} -не найден в списке магазина {self.name}')

    def get_price(self, item):
        if item in self.items:
            print(f'Цена товара: {item} -в магазине {self.name}- {self.items.get(item)} р.')
        else:
            print(f'Товар: {item} -не найден в списке магазина {self.name}')

    def change_price(self, item, new_price):
        if item in self.items:
            self.items[item] = new_price
            print(f'Цена товара: {item} -обновлена в магазине {self.name}, новая цена {new_price} p.')
        else:
            print(f'Товар: {item} -не найден в списке магазина  {self.name}')

store1 = Store('One', 'Яблоневая 15')
store2 = Store('Two', 'Вишневая 10')
store3 = Store('Three', 'Черничная 4')


store1.add_item('яблоки', 125)
store2.add_item('рис', 200)
store3.add_item('капуста',50)
store3.add_item('бананы',100)

store3.get_price('капуста')
store3.get_price('рис')

store3.delete_item('бананы')

store1.change_price('яблоки',135)