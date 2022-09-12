from notion_client import Client
from config import TOKEN_V3, DATABASE_ID

# You need to allow the integration access to the page***

notion = Client(auth=TOKEN_V3)

#use this DatabasesEndpoint Class
# Documentation from Notion:
# https://developers.notion.com/reference/update-a-database this changes properties
# notion.database.create

# Use this to add pages to the database

parent = { "type": "database_id", "database_id": DATABASE_ID }

properties = {
      "Name": {
        "type": "title",
        "title": [{ "type": "text", "text": { "content": "testmac" } }]
      },
      "Type": {
        "type": "select",
        "select": {"name":"Run"}
      },
      "Length": {
        "type": "number",
        "number": 1.49
      },
      "Time": {
        "type": "number",
        "number": 1.49
      },
      "Date": {
        "type": "date",
        "date": { "start": "2021-05-11" }
      }
    }
  

  
notion.pages.create(parent = parent, properties=properties)
  
