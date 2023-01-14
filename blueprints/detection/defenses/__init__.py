import io
import os

from PIL import Image
from apiflask import APIBlueprint
from blueprints.predict.models import *
import torch

from apiflask import Schema
from apiflask.fields import Integer, Dict, List, String,Float, File
from apiflask.validators import Length, OneOf, Range

blueprint = APIBlueprint('defenses', __name__, url_prefix='/v1/detection/defenses',tag={'name': 'COC base detection', 'description': "Detects a base's defenses by sending a screenshot"})

PATH_PT = 'data/yolo5/'
PATH_YOLO5 = 'yolov5/'
FILE_NAME_PT = {
    "cannons" : f"{PATH_PT}cannons_v2.pt",
    "towerinterno" : f"{PATH_PT}cannons_v2.pt"
}

class DetectionOut(Schema):
    cannons = List(List(Float()),
                required=True)

class ImageBase(Schema):
    image = File()

class WeigthsFileIn(Schema):
    file = File()

class DetectPatchOut(Schema):
    id = Integer()
    message = String()

def construct_blueprint():

    yolo5_models = {
        "cannons" : torch.hub.load(PATH_YOLO5, 'custom', path=FILE_NAME_PT['cannons'], source='local'),
        "towerinterno" : torch.hub.load(PATH_YOLO5, 'custom', path=FILE_NAME_PT['towerinterno'], source='local')
    }


    @blueprint.doc(summary='', description="Detects a base's defenses by sending a screenshot")
    @blueprint.post('/')
    @blueprint.input(ImageBase, location='files')
    @blueprint.output(DetectionOut)
    def post_detect_defenses(data):
        _out = {"cannons" : []}
        im_file = data['image']

        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))
        results = yolo5_models['cannons'](im)
        results.render()
        image = Image.fromarray(results.ims[0])
        image.show()
        _results = results.pandas().xyxy[0].to_dict(orient="records")
        for item in _results:
            # CANNONS FOR BASE, ALL 1
            _out['cannons'].append([item['xmin'],
                                    item['ymin'],
                                    item['xmax'],
                                    item['ymax']])
                # TODO: AQUI SE DEBERIA METER LA DETECCION DE NIVEL POR MEDIO DE SELECCION DE IMAGENES


        return _out

        return


    @blueprint.doc(summary='Push cannons Weight', description='Push pt weights for cannons yolo5 detection')
    @blueprint.patch('/cannons')
    @blueprint.input(WeigthsFileIn, location='files')
    @blueprint.output(DetectPatchOut)
    def patch_attack_stars(data):
        file = data['file']
        file.save(FILE_NAME_PT['cannons'])
        yolo5_models['cannons'] = torch.hub.load(PATH_YOLO5, 'custom', path=FILE_NAME_PT['cannons'], source='local')
        _out = {"id":1,'message': 'OK McKEY'}
        return _out

    return blueprint


