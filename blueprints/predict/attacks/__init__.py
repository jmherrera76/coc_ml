from apiflask import APIBlueprint
from blueprints.predict.models import *
from core.tensorflow import GetAttackStarsPredictIaCommand, GetAttackDestructionPredictIaCommand

blueprint = APIBlueprint('AttackStars', __name__, url_prefix='/v1/predictions/attack',tag={'name': 'COC Attack Predictions', 'description': 'Predicts an attack based on TH and AF'})

def construct_blueprint():
    tensor_model_attack_predict = GetAttackStarsPredictIaCommand()
    tensor_model_attack_destruction_predict = GetAttackDestructionPredictIaCommand()
    @blueprint.doc(summary='Predict attack', description='Predicts an attack based on TH and AF')
    @blueprint.get('/<int:townhall_attacker>/<int:townhall_defender>/<int:units_level_attacker>/<int:units_level_defender>')
    @blueprint.output(PredictAttackOut)
    def get_attack(townhall_attacker,townhall_defender,units_level_attacker,units_level_defender):
        print('paso')
        _stars = tensor_model_attack_predict.predict([townhall_attacker,townhall_defender,units_level_attacker,units_level_defender])
        _destruction = tensor_model_attack_destruction_predict.predict([townhall_attacker,townhall_defender,units_level_attacker,units_level_defender])
        ex = PredictAttackOut()
        ex.stars = _stars
        ex.destruction = _destruction
        return ex

    @blueprint.doc(summary='Train NN for atttacks predicts', description='Train NN for atttacks predicts')
    @blueprint.post('/')
    @blueprint.input(PredictAttackTrain)
    @blueprint.output(PredictAttackOut)
    def post_attack(Resurce):
        out_stars = [item[0] for item in Resurce['out_train']]
        out_destruction = [item[1] for item in Resurce['out_train']]
        stars_train = tensor_model_attack_predict.train(Resurce['in_train'],out_stars)
        destruction_train = tensor_model_attack_destruction_predict.train(Resurce['in_train'], out_destruction)
        return [stars_train,destruction_train]

    return blueprint


