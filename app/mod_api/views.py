from flask import (
    Blueprint,
    jsonify
)

from app import mongo
from bson.objectid import ObjectId

mod_api = Blueprint('api', __name__, url_prefix='/api')


@mod_api.route('/<user_id>', methods=['GET'])
def get_campaigns_by_age(user_id):
    campaigns = []
    # set radius
    dist = 500
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})
    user_lat = user['location'][0]
    user_lng = user['location'][1]
    campaigns_instance = mongo.db.campaigns.find({
        'location': {'$within': {
            "$center": [[user_lng, user_lat], dist]
        }},
        'target.from': {'$lte': user['age']},
        'target.to': {'$gte': user['age']},
        'target.sex': {'$in': ['both', user['sex']]}
    }).sort('date')
    for camp in campaigns_instance:
        campaigns.append({
            'name': camp['name'],
            'event': camp['event']['name'],
            'date': camp['date'],
            'location': camp['location']
        })
    return jsonify(campaigns=campaigns)
