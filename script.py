import requests
from truck import Truck
import json

from typesOpti import Daily

LASBRICKAS = json.load(open("las_brickas.json"))

clients = []
entrepots = []
trucks = []

def start_day(dayNumber:int):
    jsonJour = json.load(open(f"day_{dayNumber}.json"))
    populateTrucks(jsonJour["Trucks"])


def populateTrucks(p_trucks):
    for truck in p_trucks:
        trucks.append(Truck(truck["Id"],truck["AffiliatedWarehouseId"], truck["Capacity"]))
def populateClients(clients):
    for client in clients:
        pass
def populateEntrepots(entrepots):
    pass
steps = ["load truck=0 quantity=1 lego=0",
         "move_to_customer truck=0 customer=0",
         "deliver truck=0 quantity=1 lego=0",
         "move_to_warehouse truck=0 warehouse=0"]
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
print("bonne journée!")


