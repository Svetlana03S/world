
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

data = np.arange(1, 101, 1)

input_sequence = [data[i:i+5] for i in range(len(data)-5)]
output_sequence = [data[i+5] for i in range(len(data)-5)]

X = np.array(input_sequence).reshape(-1, 5, 1)
y = np.array(output_sequence)

model = Sequential()
model.add(SimpleRNN(50, activation='relu', input_shape=(5, 1)))
model.add(Dense(1))

model.compile(optimizer=Adam(), loss='mean_squared_error')
model.fit(X, y, epochs=50, batch_size=1)

test_data = np.arange(101, 111, 1)
X_test = np.array([test_data[i:i+5] for i in range(len(test_data)-5)])
y_test = np.array([test_data[i+5] for i in range(len(test_data)-5)])

predictions = model.predict(X_test.reshape(-1, 5, 1))

mse = np.mean((predictions.flatten() - y_test) ** 2)
print("mse")
