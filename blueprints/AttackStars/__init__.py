import torch
from flask import Blueprint, request

from core.tensorflow import GetAttackStarsPredictIaCommand


def construct_blueprint():

    blueprint = Blueprint('tf', __name__, url_prefix='/v1/tf/attack-stars')
    tensor_model_attack_predict = GetAttackStarsPredictIaCommand()

    @blueprint.route('/hello')
    def hello_world():
        return {'message': 'Hello World!'}

    @blueprint.route('/train', methods=[ 'POST'])
    def train():
        tensor_model_attack_predict.train(request.json['in'],request.json['out'])
        return {"train":True}

    @blueprint.route('/predict', methods=['POST'])
    def predict(entity_id):
        predic = tensor_model_attack_predict.predict(request.json['data'])
        return str(predic)

    return blueprint
