from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config.from_object('config')

mongo = PyMongo(app)

from app.mod_admin.views import mod_admin as admin_module
from app.mod_api.views import mod_api as api_module


@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/event/<event_id>', methods=['GET'])
def event_view(event_id):
    event = mongo.db.events.find_one({'_id': ObjectId(event_id)})
    return render_template('event_view.jinja2', event=event)

app.register_blueprint(admin_module)
app.register_blueprint(api_module)
