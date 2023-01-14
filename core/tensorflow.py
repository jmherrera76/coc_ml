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

    def ponderate_in(self, _in):
        return [_in[0] / 15,
                _in[1] / 15,
                _in[2] / 2000,
                _in[3] / 2000]
    def real_in(self, _in):
        return [_in[0] * 15,
                _in[1] * 15,
                _in[2] * 2000,
                _in[3] * 2000]

    def ponderate_out(self, _out):
        return  _out / 3
    def real_out(self, _out):
        return  _out * 3

    def np_array_in(self, _in):
        _array = []
        for a in _in:
            _array.append(self.ponderate_in(a))

        return np.array(_array)

    def np_array_out(self, _out):
        _array = []
        for a in _out:
            _array.append(self.ponderate_out(a))

        return np.array(_array)

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
        _data = self.np_array_in([array_x])
        _result = self._model.predict(_data)
        if _result > 0.90:
            _result = 1
        return self.real_out(_result)


    def train(self, array_x,array_y):
        self._model.fit(self.np_array_in(array_x), self.np_array_out(array_y), epochs=2000, callbacks=[self._tensorboard_callback], validation_split=0.4)
        #scores = self._model.evaluate(self._data_in_train, self._data_out_train)
        self._model.save_weights(f"data/tensorflow/{self._name}.h5")
        pass


class GetAttackDestructionPredictIaCommand(TensorFlowCommand, ABC):

    def ponderate_in(self, _in):
        return [_in[0] / 15,
                _in[1] / 15,
                _in[2] / 2000,
                _in[3] / 2000]
    def real_in(self, _in):
        return [_in[0] * 15,
                _in[1] * 15,
                _in[2] * 2000,
                _in[3] * 2000]

    def ponderate_out(self, _out):
        return  _out / 100
    def real_out(self, _out):
        return  _out * 100

    def np_array_in(self, _in):
        _array = []
        for a in _in:
            _array.append(self.ponderate_in(a))

        return np.array(_array)

    def np_array_out(self, _out):
        _array = []
        for a in _out:
            _array.append(self.ponderate_out(a))

        return np.array(_array)

    def __init__(self )-> None:

        self._name = "AttackResultDestruction"

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
        _data = self.np_array_in([array_x])
        _result = self._model.predict(_data)
        if _result > 0.95:
            _result = 1
        return self.real_out(_result)


    def train(self, array_x,array_y):
        self._model.fit(self.np_array_in(array_x), self.np_array_out(array_y), epochs=2000, callbacks=[self._tensorboard_callback], validation_split=0.4)
        #scores = self._model.evaluate(self._data_in_train, self._data_out_train)
        self._model.save_weights(f"data/tensorflow/{self._name}.h5")
        pass
