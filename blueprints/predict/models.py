import marshmallow
from apiflask import Schema
from apiflask.fields import Integer, List
from apiflask.validators import Length, OneOf, Range
class PredictAttackIn(Schema):
    th_attacker = Integer(
        required=True,
        validate=Range(1,15))
    th_defender = Integer(
        required=True,
        validate=Range(1,15))
    fa_attacker = Integer(
        required=True,
        validate=Range(1,2500))
    fa_defender = Integer(
        required=True,
        validate=Range(1, 2500))

class PredictAttackOut(Schema,marshmallow.base.FieldABC):
    stars = Integer(
        validate=Range(1,3),
        description='Estimated stars')
    destruction = Integer(
        validate=Range(1, 100),
        description='Estimated destruction')

class PredictAttackTrain(Schema):
    in_train = List(PredictAttackOut)
    out_train = []

