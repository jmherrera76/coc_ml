import json

import requests
import os

def load_data():
    dir_path = r'_data/'
    res = os.listdir(dir_path)
    in_total = []
    out_total = []
    for file in res:
        json_file = open(f"{dir_path}/{file}", 'r')
        data = json.load(json_file)

        # IN
        th = int(data['attacker']['town_hall'])
        tho = int(data['defender']['town_hall'])

        fa = int(data['attacker']['total_level_units'])
        fao = int(data['defender']['total_level_units'])
        in_total.append([th,tho,fa,fao])
        # OUT
        stars = data['stars']
        destruction = data['destruction']
        duration = data['duration']
        out_total.append(int(stars))
        json_file.close()

    return {"in":in_total,
            "out":out_total }


def train():
    response = requests.post('http://localhost:5003/v1/tf/attack-stars/train', json=load_data())
    print(response)

train()

