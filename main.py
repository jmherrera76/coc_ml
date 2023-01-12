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

app = Flask(__name__)
models = {}

DETECTION_URL = "/v1/object-detection/<model>"
GAME_PREDICTION_URL = "/v1/game-prediction/<model>"

@app.route(DETECTION_URL, methods=["POST"])
def predict(model):
    if request.method != "POST":
        return

    if request.files.get("image"):

        im_file = request.files["image"]
        im_bytes = im_file.read()
        im = Image.open(io.BytesIO(im_bytes))
        results = model_cannons(im)
        results.render()
        image = Image.fromarray(results.ims[0])
        image.show()


        return results.pandas().xyxy[0].to_json(orient="records")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask API exposing YOLOv5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    parser.add_argument('--model', nargs='+', default=['cannons2'], help='model(s) to run, i.e. --model yolov5n yolov5s')
    opt = parser.parse_args()


    # SET UP YOLOv5 MODELS
    model_cannons = torch.hub.load('yolov5/', 'custom', path=f"data/yolo5/cannons2.pt", source='local')
    model_towers_inferno = torch.hub.load('yolov5/', 'custom', path=f"data/yolo5/cannons.pt", source='local')

    app.run(host="0.0.0.0", port=opt.port)  # debug=True causes Restarting with stat