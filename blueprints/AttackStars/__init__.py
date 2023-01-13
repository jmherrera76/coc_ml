from flask import Blueprint, request

blueprint = Blueprint('api_tf', __name__, url_prefix='/v1/tf/attack-stars')

@blueprint.route('/')
def hello_world():
    return {'message': 'Hello World!'}

@blueprint.route('/train', methods=[ 'POST'])
def entities():
    return {
        'message': 'This endpoint should create an entity',
        'method': request.method,
        'body': request.json
    }

@blueprint.route('/predict', methods=['GET'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message': 'This endpoint should return the entity {} details'.format(entity_id),
            'method': request.method
        }
