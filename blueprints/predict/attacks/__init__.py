from apiflask import APIBlueprint
from blueprints.predict.models import *
from core.tensorflow import GetAttackStarsPredictIaCommand

blueprint = APIBlueprint('AttackStars', __name__, url_prefix='/v1/predictions/attack',tag={'name': 'COC Attack Predictions', 'description': 'Predicts an attack based on TH and AF'})

def construct_blueprint():
    tensor_model_attack_predict = GetAttackStarsPredictIaCommand()
    @blueprint.doc(summary='Predict attack', description='Predicts an attack based on TH and AF')
    @blueprint.get('/<int:th_a>/<int:th_d>/<int:fa_a>/<int:fa_o>')
    @blueprint.output(PredictAttackOut)
    def post_attack_stars(th_a,th_d,fa_a,fa_o):

        exit = tensor_model_attack_predict.predict([th_a,th_d,fa_a,fa_o])
        ex = PredictAttackOut()
        ex.stars = exit[0]


        return ex

    @blueprint.doc(summary='Train NN for atttacks predicts', description='Train NN for atttacks predicts')
    @blueprint.post('/')
    @blueprint.input(PredictAttackIn)
    @blueprint.output(PredictAttackOut)
    def patch_attack_stars(Resurce):
        exit = tensor_model_attack_predict.train(Resurce.json['in'],Resurce.json['out'])

        return exit

    return blueprint


