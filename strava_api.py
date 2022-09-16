from stravaio import strava_oauth2
from stravaio import StravaIO

from config import CLIENT_ID, CLIENT_SECRET, DATABASE_ID
from notion_api_new import uploadToNotion

token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
print("Authorised")
activities = client.get_logged_in_athlete_activities()
print("Activites fetched")

# compare activitess
#with open('last.txt', 'r') as file:
#    recent = file.read().rstrip()

#for i, activity in enumerate(activities):
#     if str(activity.id) == recent:
#          last_index = i
#          break


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

# save last id

last = str(activities[-1].id)

last_file = open("last.txt", "w")
n = last_file.write('last')
last_file.close()