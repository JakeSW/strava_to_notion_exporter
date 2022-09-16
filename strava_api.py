from datetime import datetime
from time import strftime
from stravaio import strava_oauth2
from stravaio import StravaIO

from config import CLIENT_ID, CLIENT_SECRET, DATABASE_ID, All_Data
from notion_api_new import uploadToNotion
from notion_api_date import most_recent_activity_date


token = strava_oauth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)

# Get Strava Data
client = StravaIO(access_token=token["access_token"])
print("Authorised")

# Check if we sync all activities or activities after a the last date
if All_Data:
     after_date=0
else:
     after_date = most_recent_activity_date()

activities = client.get_logged_in_athlete_activities(after=after_date)
print("Activities fetched")

parent = { "type": "database_id", "database_id": DATABASE_ID }

for activity in activities:
    
     uploadToNotion(parent=parent, data=activity)
     print("Uploaded activity")