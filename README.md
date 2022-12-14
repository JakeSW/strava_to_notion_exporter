# Strava to Notion exporter in Python (New Notion API)
Import Strava activity information to a Notion database. Subsequent uploads use the most recent entry in the notion database to not double sync.

Inspired by [IVIURRAY](https://github.com/IVIURRAY/strava2notion) and updated for the new Notion API.

# How to use

### Setup 
1. Create an App though the [Strava API](https://www.strava.com/settings/api) (I used media/notion_icon.png for the image).
2. Insert `Client ID` and `Client Secret` into `config.py`.
3. Create an app through the [Notion API](https://www.notion.so/) (I used media/strava_icon.png for the image). Add your secret ID to `config.py` as `TOKEN_V3`.
4. Create a database (create this as a blank database page) in notion, copy the ID to config file. Give your notion integration access to the data base (share button).
5. Add the relevant columns to the database, the default needs Name, Type (select), Length (number), Time (number), Date (date), Power (number), Elevation (number), Strava Link (URL). You can customise these in the `notion_api_new.py` file.

### How to run
1. `git clone https://github.com/jakesw/strava_to_notion_exporter.git`
2. `cd strava_to_notion_exporter`
3. create a new environment from `requirements.txt`
4. `python3 strava_api.py` This will open a browser to ask you to authenticate the integration, I had issues running this in WSL.
5. For subsequent runs set `All_Data` in `config.py` to `False` and it will only upload your new activities.
  
The `notion_api_test.py` file is left in for you to test adding different data to the database. See [Strava API](https://developers.strava.com/docs/reference/) for what other data is taken from the API request.

#### Finding Database ID
Copy the link to your database page that will look like: `https://www.notion.so/<long_hash_1>?v=<long_hash_2>` then choose `<long_hash_1>`, this is the database ID.

#### Libraries
The HTTP Requests are abstracted away by two helpful libraries: [stravio](https://github.com/sladkovm/stravaio) and [notion-sdk-py](https://github.com/ramnes/notion-sdk-py). This documentation coupled with the official API documentation is useful for debugging and customising.
