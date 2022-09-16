from notion_client import Client
from config import TOKEN_V3

import numpy as np

# You need to allow the integration access to the page

notion = Client(auth=TOKEN_V3)

#use this DatabasesEndpoint Class
# Documentation from Notion:
# https://developers.notion.com/reference/update-a-database this changes properties
# notion.database.create

# Use this to add pages to the database


def uploadToNotion(parent, data):

  print(data.name)

  date = str(data.start_date_local)

  distance = np.round(data.distance / 1000,2)

  if data.weighted_average_watts == None:
    power = 0
  else:
    power = data.weighted_average_watts

  link = "https://strava.com/activities/"+str(data.id)

  properties = {
        "Name": {
          "type": "title",
          "title": [{ "type": "text", "text": { "content": data.name } }]
        },
        "Type": {
          "type": "select",
          "select": {"name": data.type }
        },
        "Length": {
          "type": "number",
          "number": distance
        },
        "Time": {
          "type": "number",
          "number": data.moving_time
        },
        "Power": {
          "type": "number",
          "number": power
        },
        "Elevation": {
          "type": "number",
          "number": data.total_elevation_gain
        },
        "Date": {
          "type": "date",
          "date": { "start": date }
        },
        "Strava Link":{
        "type": "url",
        "url": link
      }
      }
  
  notion.pages.create(parent = parent, properties=properties)
  
