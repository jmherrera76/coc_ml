import marshmallow
from apiflask import Schema
from apiflask.fields import Integer, Dict, List, String,Float, Boolean
from apiflask.validators import Length, OneOf, Range
class PredictAttackIn(Schema):
    th_attacker = Integer(
        required=True,
        validate=Range(1, 15))
    th_defender = Integer(
        required=True,
        validate=Range(1, 15))
    fa_attacker = Integer(
        required=True,
        validate=Range(1, 899))
    fa_defender = Integer(
        required=True,
        validate=Range(1, 899))
    is_mirrow_attack = Boolean()
    is_first_attack = Boolean(
        required=True)
    is_clean_attack = Boolean(
        required=True)

class PredictAttackOut(Schema):
    stars = List(Integer())

class PredictAttackTrain(Schema):
    in_train = List(List(Integer()))
    out_train = List(List(Integer()))

