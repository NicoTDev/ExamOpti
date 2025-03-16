from typesOpti import LegosQty


class Clients:
    def __init__(self, id:int, orders:list[LegosQty], position: dict):
        self.id = id
        self.orders = orders
        self.position = position
