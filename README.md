# Test case

## Build setup

```
#install mongodb and run
# then set geo indexes
db.users.createIndex( { location : "2dsphere" } )
db.campaigns.createIndex( { location : "2dsphere" } )
db.events.createIndex( { location : "2dsphere" } )

# install python dependecies
pip install -r requirements.txt

# run dev server at localhost:8080
python run.py
```

## Project description
### URLs
* /admin
    * /events - show events with links to webview
    * /campaigns - show campaging
    * /users - show users with linkg to /api/<user_id>
    * /event/add - create event form
    * /campaign/add - create campaign form
* /api/<user_id> - here you come from /admin/users for get campaigns for user by geolocation
* /event/<event_id> - webview for event from /admin/events.
