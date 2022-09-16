from notion_client import Client
from config import TOKEN_V3, DATABASE_ID

# You need to allow the integration access to the page

notion = Client(auth=TOKEN_V3)

#use this DatabasesEndpoint Class
# Documentation from Notion:
# https://developers.notion.com/reference/query-a-database
# Use this to look at data in a notion database
# notion.database.query

# Here we look at the most recent item and take the date from the strave activity
# then we can look at dates after this activity to sync
def most_recent_activity_date(id=DATABASE_ID):
  # query
  data = notion.databases.query(database_id=id,page_size=1)

  # find the date
  results = data['results']
  result_data = dict(results[0])
  properties = result_data['properties']
  Date = properties["Date"]
  date = Date['date']
  start_date = date['start']
  start_date = start_date[0:10]
  print(start_date)

  #add a day to not duplicate, may miss double days though
  end_char = int(start_date[-1])+1
  start_date = start_date[0:9]+str(end_char)
  print(start_date)

  return start_date

