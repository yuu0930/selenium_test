class Item:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price
        
    def get_cost_rate(self):
        cost_rate = self.purchase_price / self.price
        return cost_rate

item_1 = Item("A0001", "半袖クールTシャツ", 5000, 2250)
rate = item_1.get_cost_rate()
print(rate)

item_1.price = 6000
rate = item_1.get_cost_rate()
print(rate)