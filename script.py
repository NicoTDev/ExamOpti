import requests
import json

DAY1JSON = json.loads("day_1.json")
print(DAY1JSON)


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




