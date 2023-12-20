from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy
import numpy as np

iris = load_iris()

# Obtenir les données et leurs classifications:
dims = iris.feature_names
classes = iris.target_names
x = iris.data
y = iris.target

# Découper les données en ensembles d'entrainement et de test:
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

# Standardisation:
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Création du MLP:
model = Sequential()
model.add(Dense(units = 128, activation = 'relu', input_dim = 4))
model.add(Dense(units = 64, activation = 'relu'))
model.add(Dense(units = 3, activation = 'softmax'))
model.compile(optimizer = Adam(learning_rate=0.001),
              loss = SparseCategoricalCrossentropy(),
              metrics = ['accuracy'])

history = model.fit(x_train, y_train, epochs = 10, batch_size = 32)#, validation_data=(x_test, y_test))

# Getting accuracy:
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"loss: {test_loss}, accuracy: {test_accuracy}")

# Nouvelle prédiction:
#nouveau_prediction = np.array([[5.1, 3.5, 1.4, 0.2]])
nouveau_prediction = np.array([[5.9, 3.,  5.1, 1.8]])

nouveau_prediction = scaler.transform(nouveau_prediction)
res = model.predict(nouveau_prediction)
print(res)
print(classes[np.argmax(res[0])])