import requests



requests.post("https://opti.csgames.org/Solution")
steps = []
body = """
{
  "credentials": {
    "teamName": "or",
    "password": "zoo-accident-running"
  },
  "dayNumber": 0,
  "steps":""" + str(steps) + """
  }
  """


print(body)



