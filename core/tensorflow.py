from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime

import numpy as np
from keras import Sequential
from keras.layers import Dense

import tensorflow


class TensorFlowCommand(ABC):

    @abstractmethod
    async def predict(self,p) -> None:
        pass

    @abstractmethod
    async def train(self,p) -> None:
        pass

class GetAttackStarsPredictIaCommand(TensorFlowCommand, ABC):
    def __init__(self )-> None:

        self._name = "AttackResultStars"

        self._model = Sequential()
        self._model.add(Dense(25, input_dim=4, activation='relu'))
        self._model.add(Dense(50, activation='relu'))
        self._model.add(Dense(1, activation='sigmoid'))
        self._model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
        try:
            self._model.load_weights(f"data/tensorflow/{self._name}.h5")
        except:
            pass

        log_dir = f"_logs/{self._name}/{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self._tensorboard_callback = tensorflow.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    def predict(self, array_x) -> None:
        _data = np.array([array_x])
        return self._model.predict(_data)
        pass

    def train(self, array_x,array_y):
        _array_x = np.array([array_x])
        _array_y = np.array([array_y])
        self._model.fit(_array_x, _array_y, epochs=2000, callbacks=[self._tensorboard_callback], validation_split=0.4)
        #scores = self._model.evaluate(self._data_in_train, self._data_out_train)
        self._model.save_weights(f"data/tensorflow/{self._name}.h5")
        pass

class _cGetAttackStarsPredictIaCommand(TensorFlowCommand, ABC):

    def __init__(self )-> None:

        self._name = "AttackResult"
        self._model = Sequential()
        self._model.add(Dense(25, input_dim=5, activation='relu'))
        self._model.add(Dense(50, activation='relu'))
        self._model.add(Dense(2, activation='sigmoid'))
        self._model.compile(loss='mean_squared_error', optimizer='adam', metrics=['binary_accuracy'])
        self._model.load_weights('data/tensorflow/AttackResult.h5')

        log_dir = f"_logs/{self._name}/{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self._tensorboard_callback = tensorflow.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    def predict(self, array_x) -> None:
        _data = np.array([array_x])
        return self._model.predict(_data)
        pass

    def train(self, array_x,array_y):
        _array_x = np.array(array_x)
        _array_y = np.array(array_y)
        self._model.fit(_array_x, _array_y, epochs=2000, callbacks=[self._tensorboard_callback], validation_split=0.4)
        #scores = self._model.evaluate(self._data_in_train, self._data_out_train)
        self._model.save_weights(f"data/tensorflow/{self._name}.h5")
        pass

