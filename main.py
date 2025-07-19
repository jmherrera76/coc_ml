# YOLOv5 🚀 by Ultralytics, GPL-3.0 license
"""
Run a Flask REST API exposing one or more YOLOv5s models
"""

import argparse
import base64
import io
import os

import torch
from flask import Flask, request
from PIL import Image

from core.tensorflow import GetAttackStarsPredictIaCommand
# from blueprints.AttackStars import construct_blueprint as attacks_stars_endpoints
from blueprints.predict import attacks as attacks_stars_endpoints

app = Flask(__name__)

models = {}

DETECTION_URL = "/v1/object-detection/<model>"
GAME_PREDICTION_URL = "/v1/game-prediction/<model>"
GAME_PREDICTION_TRAIN = GAME_PREDICTION_URL + "/train"


@app.route(DETECTION_URL, methods=["POST"])
def predict(model):
    if request.files.get("image"):
        im_file = request.files["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))
        results = yolo_model_cannons(im)
        results.render()
        image = Image.fromarray(results.ims[0])
        # image.show()

        return results.pandas().xyxy[0].to_json(orient="records")


@app.route(GAME_PREDICTION_URL, methods=["POST"])
def predict_tensor(model):
    pass

@app.route(GAME_PREDICTION_TRAIN, methods=["POST"])
def train_tensor(model):

    pass


if __name__ == "__main__":

    app.register_blueprint(attacks_stars_endpoints(), name='api_tf')
    app.register_blueprint(attacks_stars_endpoints())
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5003, type=int, help="port number")
    parser.add_argument('--model', nargs='+', default=['cannons2'], help='model(s) to run, i.e. --model yolov5n yolov5s')
    opt = parser.parse_args()


    # SET UP YOLOv5 MODELS
    yolo_model_cannons = torch.hub.load('yolov5/', 'custom', path=f"data/yolo5/cannons_v2.pt", source='local')
    yolo_model_towers_inferno = torch.hub.load('yolov5/', 'custom', path=f"data/yolo5/cannons.pt", source='local')

    # SET UP TENSORFLOWS MODELS
    #tensor_model_attack_predict = GetAttackStarsPredictIaCommand()


    app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat