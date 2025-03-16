from entrepot import Entrepot


class Truck:
    def __init__(self, id: int, affiliatedWarehouseId: int, capacity: int, entrepots: list[Entrepot]):
        self.id = id
        self.affiliatedWareHouseId = affiliatedWarehouseId
        self.capacity = capacity
        self.position = entrepots[affiliatedWarehouseId].position

    def find_nearest_entrepot(self, entrepots: list[Entrepot]) -> Entrepot:
        dist = map(lambda e: (e, abs((e.position["X"] - self.position["X"]) + (e.position["Y"] - self.position["Y"]))), entrepots)
        tri = sorted(dist, key=lambda t: t[1])

        return tri[0][0]

    def find_entrepot_has_stock(self, lego: int, qty: int, entrepots: list[Entrepot]) -> list[Entrepot]:

        entre: list[Entrepot] = []

        for e in entrepots:
            # check if stock
            map_stock = map(lambda s: s["LegoId"], e.stock)
            
            try:
                idx = list(map_stock).index(lego)
            except:
                continue

            stock = e.stock[idx]

            if stock["Quantity"] < qty:
                continue

            entre.append(e)

        return entre
