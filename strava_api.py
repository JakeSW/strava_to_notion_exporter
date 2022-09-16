from datetime import datetime
from time import strftime
from stravaio import strava_oauth2
from stravaio import StravaIO

from config import CLIENT_ID, CLIENT_SECRET, DATABASE_ID, All_Data
from notion_api_new import uploadToNotion

token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
print("Authorised")

if All_Data:
     after_date=0
else:
     with open('last.txt', 'r') as file:
          after_date = file.read().rstrip()

activities = client.get_logged_in_athlete_activities(after=after_date)
print("Activities fetched")

print(activities[-1].id)

# for activity in activities:
#     print(activity)
#     break

# Upload information to Notion
#notion = NotionInterface()
#table = notion.create_activity_log_table()
#for activity in activities:
#    notion.add_row_to_table(table, activity)

parent = { "type": "database_id", "database_id": DATABASE_ID }


for activity in activities:
    
     uploadToNotion(parent=parent, data=activity)
     print("Uploaded activity")

# save sync time

now = datetime.now()
after_date = strftime("%Y-%m-%d")

last_file = open("last.txt", "w")
n = last_file.write(after_date)
last_file.close()