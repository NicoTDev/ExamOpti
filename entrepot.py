class Entrepot:
    def __init__(self, id:int, stock:list, position:dict):
        self.id = id
        self.stock = stock
        self.position = position


    def del_from_stock(self, lego: int, qty: int):
        map_stock = map(lambda s: s["LegoId"], self.stock)

        idx = list(map_stock).index(lego)
        self.stock[idx]["Quantity"] -= qty
