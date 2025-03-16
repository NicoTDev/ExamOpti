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
