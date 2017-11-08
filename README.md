# Test case

## Used technologies
* Flask
* MongoDB
* Bootstrap

## Build setup

```
#install mongodb and run
# then create geo indexes
db.users.createIndex( { location : "2dsphere" } )
db.campaigns.createIndex( { location : "2dsphere" } )
db.events.createIndex( { location : "2dsphere" } )

# set db name, host, port etc in config.py (in meters)

# install python dependecies
pip install -r requirements.txt

# set distance in mod_api/views for searching radius #crutch

# run dev server at localhost:8080
python run.py
```

## Project description
### URLs
* /admin
    * /events - show events with links to webview
    * /campaigns - show campaigns
    * /users - show users with link to /api/<user_id>
    * /event/add - create event form
    * /campaign/add - create campaign form
* /api/<user_id> - here you come from /admin/users for get campaigns for user by geolocation
* /event/<event_id> - webview for event from /admin/events.
