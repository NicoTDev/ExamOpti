import requests

from client import Client
from truck import Truck
from entrepot import Entrepot
import json

from typesOpti import Daily

LASBRICKAS = json.load(open("las_brickas.json"))

clients = []
entrepots = []
trucks = []

def start_day(dayNumber:int):
    jsonJour = json.load(open(f"day_{dayNumber}.json"))
    populateEntrepots(jsonJour["Warehouses"])
    populateTrucks(jsonJour["Trucks"])
    populateClients(jsonJour["Customers"])


def populateEntrepots(p_entrepots):
    for entrepot in p_entrepots:
        entrepots.append(Entrepot(entrepot["Id"], entrepot["Stock"], LASBRICKAS["Warehouses"][entrepot["Id"]]))


def populateTrucks(p_trucks):
    for truck in p_trucks:
        trucks.append(Truck(truck["Id"],truck["AffiliatedWarehouseId"], truck["Capacity"]))
def populateClients(p_clients):
    for client in p_clients:
        clients.append(Client(client["Id"], client["Orders"], LASBRICKAS["Customers"][client["Id"]]))



steps = []
body = """
{
  "credentials": {
    "teamName": "or",
    "password": "zoo-accident-running"
  },
  "dayNumber": 1,
  "steps":""" + str(steps).replace("'", "\"") + """
  }
  """

start_day(2)
print(entrepots)


