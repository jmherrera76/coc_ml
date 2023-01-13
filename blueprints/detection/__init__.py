from apiflask import APIBlueprint
blueprint = APIBlueprint('Detection', __name__, url_prefix='/v1/predictions/attack',tag={'name': 'COC Attack Predictions', 'description': 'Predicts an attack based on TH and AF'})

def construct_blueprint():
    return blueprint
