from apiflask import APIBlueprint
from blueprints.predict.models import *
from core.tensorflow import GetAttackStarsPredictIaCommand, GetAttackDestructionPredictIaCommand, \
    GetAttackStarsPredictIaCommandMultiClass

blueprint = APIBlueprint('AttackStars', __name__, url_prefix='/v1/predictions/attack',tag={'name': 'COC Attack Predictions', 'description': 'Predicts an attack based on TH and AF'})

def construct_blueprint():
    tensor_model_attack_predict = GetAttackStarsPredictIaCommandMultiClass()

    @blueprint.doc(summary='1 - Predict attack', description='Predicts an attack based on TH and AF')
    @blueprint.get('/<int:townhall_attacker>/<int:townhall_defender>/<int:units_level_attacker>/<int:units_level_defender>/<int:is_mirrow_attack>/<int:is_first_attack>/<int:is_clean_attack>/')
    @blueprint.output(PredictAttackOut)
    def get_attack(townhall_attacker, townhall_defender, units_level_attacker, units_level_defender, is_mirrow_attack, is_first_attack, is_clean_attack):
        print('paso')
        _stars = tensor_model_attack_predict.predict([townhall_attacker,townhall_defender,units_level_attacker,units_level_defender,is_mirrow_attack,is_first_attack,is_clean_attack])

        ex = PredictAttackOut()
        ex.stars = _stars

        return ex

    @blueprint.doc(summary='2 - Train NN for atttacks predicts', description='Train NN for atttacks predicts')
    @blueprint.post('/train')
    @blueprint.input(PredictAttackTrain)
    @blueprint.output(PredictAttackOut)
    def post_attack(Resurce):

        out_stars = [item[0] for item in Resurce['out_train']]
        stars_train = tensor_model_attack_predict.train(Resurce['in_train'],out_stars)
        return [stars_train]

    return blueprint


