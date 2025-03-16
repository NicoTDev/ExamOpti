

class Client:
    def __init__(self, id:int, orders:list, position: dict):
        self.id = id
        self.orders = orders
        self.position = position


    @staticmethod
    def findLongestClientFromEntrepot(clients, position):
        bestClients = clients[0]
        bestDistance = ((clients[0].position['X']-position["X"])**2+(clients[0].position['X']-position["X"])**2)**0.5
        for client in clients:
            distance = ((client.position['X']-position["X"])**2+(client.position['X']-position["X"])**2)**0.5
            if distance > bestDistance:
                bestClients = client
                bestDistance = distance
        return bestClients


    @staticmethod
    def findNearestClientFromEntrepot(clients, position):
        bestClients = clients[0]
        bestDistance = ((clients[0].position['X']-position["X"])**2+(clients[0].position['X']-position["X"])**2)**0.5
        for client in clients:
            distance = ((client.position['X']-position["X"])**2+(client.position['X']-position["X"])**2)**0.5
            if distance < bestDistance:
                bestClients = client
                bestDistance = distance
        return bestClients




