import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input, TimeDistributed, Flatten
from tensorflow.keras import layers, models

class Model:
  def __init__(self) -> None:
      self.epochs = 10

  def get_epochs(self):
        return self.epochs

  def set_epochs(self, value):
        self.epochs = value

  def __call__(self, input_shape):
        self.model = Sequential()
        self.model.add(Input(shape=input_shape))  # Input layer
        self.model.add(TimeDistributed(LSTM(64, activation='relu', return_sequences=True)))  # TimeDistributed LSTM layer
        self.model.add(TimeDistributed(LSTM(32, activation='elu')))  # Additional TimeDistributed LSTM layer
        self.model.add(Flatten())  # Flatten the output for dense layers
        self.model.add(Dense(1, activation='linear'))  # Output layer with linear activation since it's a regression problem

        return self.model

  def train(self, x_train, y_train,callback):
    self.model.fit(x_train, y_train, epochs=self.epochs, batch_size=9,callbacks=[callback])