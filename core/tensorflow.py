from __future__ import annotations
from abc import ABC, abstractmethod

import numpy as np
from keras.saving.legacy.model_config import model_from_json

class TensorFlowCommand(ABC):

    @abstractmethod
    async def predict(self,p) -> None:
        pass
class GetAttackStarsPredictIaCommand(TensorFlowCommand, ABC):

    def __init__(self )-> None:
        json_file = open('data/tensorflow/AttackResult.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        self._model = model_from_json(loaded_model_json)
        self._model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
        self._model.load_weights('data/tensorflow/AttackResult.h5')

    def predict(self, array_x) -> None:
        _data = np.array([array_x])
        return self._model.predict(_data)
        pass