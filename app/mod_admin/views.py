import os
from datetime import datetime
from bson.objectid import ObjectId
from app import app, mongo
from flask import (
    Blueprint,
    render_template,
    redirect
)
from werkzeug.utils import secure_filename
from .forms import EventForm, CampaignForm

mod_admin = Blueprint('admin', __name__, url_prefix='/admin')


@mod_admin.route('/', methods=['GET'])
def index():
    return render_template('admin/index.jinja2')


@mod_admin.route('/campaigns', methods=['GET'])
def campaigns_list():
    campaigns = mongo.db.campaigns.find()
    return render_template('admin/campaignsList.jinja2', campaigns=campaigns)


@mod_admin.route('/events', methods=['GET'])
def events_list():
    events = mongo.db.events.find()
    return render_template('admin/eventsList.jinja2', events=events)


@mod_admin.route('/users', methods=['GET'])
def users_list():
    users = mongo.db.users.find()
    return render_template('admin/usersList.jinja2', users=users)


@mod_admin.route('/campaign/add', methods=['GET', 'POST'])
def campaign():
    form = CampaignForm()

    if form.validate_on_submit():
        event_instance = mongo.db.events.find_one({"_id": ObjectId(form.event.data)})
        campaign_instance = {
            'name': form.name.data,
            'event': event_instance,
            'target': [form.target_from.data, form.target_to.data],
            'sex': form.sex.data,
            'target': {
                'from': form.target_from.data,
                'to': form.target_to.data,
                'sex': form.sex.data,
                'radius': form.radius.data
            },
            'date': datetime.strftime(form.date.data, '%Y-%m-%d'),
            'location': [form.lat.data, form.lng.data]
        }
        mongo.db.campaigns.save(campaign_instance)
        return redirect('/admin/campaigns')
    for errors in form.errors:
        print(errors)
    events = mongo.db.events.find()
    return render_template('admin/campaignForm.jinja2', events=events, form=form)


@mod_admin.route('/event/add', methods=['GET', 'POST'])
def event():
    form = EventForm()
    if form.validate_on_submit():
        file = form.logo.data
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.root_path, 'static', 'img', filename)
        file.save(filepath)
        event_instance = {
            'name': form.name.data,
            'organizator': form.organizator.data,
            'logo': filename,
            'icon': form.icon.data,
            'description': form.description.data,
            'what': form.what.data,
            'where': form.where.data,
            'when': form.when.data,
            'location': [form.lat.data, form.lng.data],
            'number': form.number.data,
            'url': form.url.data
        }
        mongo.db.events.save(event_instance)
        return redirect('/admin/events')
    for errors in form.errors:
        print(errors)
    return render_template('admin/eventForm.jinja2', form=form)
