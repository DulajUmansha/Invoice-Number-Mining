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
      self.model.add(Input(shape=input_shape))

      # Convolutional layers
      self.model.add(TimeDistributed(layers.Conv1D(32, kernel_size=3, activation='relu')))
      self.model.add(TimeDistributed(layers.MaxPooling1D(pool_size=2)))

      # LSTM layer
      self.model.add(TimeDistributed(LSTM(20, activation='relu', return_sequences=True)))

      # Flatten the output for dense layers
      self.model.add(Flatten())

      # Dense layers
      self.model.add(Dense(64, activation='relu'))
      self.model.add(Dense(32, activation='relu'))
      self.model.add(Dense(16, activation='relu'))

      # Output layer
      self.model.add(Dense(1, activation='softplus'))

      return self.model

  def train(self, x_train, y_train,callback):
    self.model.fit(x_train, y_train, epochs=self.epochs, batch_size=9,callbacks=[callback])