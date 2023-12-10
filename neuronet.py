from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import numpy as np

data = np.random.rand(100, 5) 
labels = np.random.randint(2, size=(100,))  

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2)

model = Sequential()
model.add(Dense(64, input_shape=(5,), activation='relu'))  
model.add(Dense(1, activation='sigmoid'))  

model.compile(optimizer=Adam(lr=0.001), loss='binary_crossentropy', metrics=['accuracy'])


model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy}')