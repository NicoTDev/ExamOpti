

class Client:
    def __init__(self, id:int, orders:list, position: dict):
        self.id = id
        self.orders = orders
        self.position = position


    @staticmethod
    def findLongestClientFromEntrepot(clients, position):
        bestClients = clients[0]
        bestDistance = -1
        for client in clients:
            distance = ((client.position['X']-position["X"])**2+(client.position['X']-position["X"])**2)**0.5
            if distance > bestDistance:
                bestClients = clients
                bestDistance = distance





