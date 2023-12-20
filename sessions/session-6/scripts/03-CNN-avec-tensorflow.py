from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models
import numpy as np
import utils
import os

# Charger les données:
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
utils.display_images(train_images, train_labels, [0])

# Mettre la forme des données aux normes:
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Convertir en "matrice de classes binaire":
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Créer le CNN:
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrainer le CNN:
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_labels))

# Evaluer le CNN:
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f'Test accuracy: {test_acc * 100:.2f}%')

model.save(os.path.join(os.getcwd(), "sessions", "session-6", "data", "model_out.keras"))

# img = utils.load_image(os.path.join(os.getcwd(), "sessions", "session-6", "data", "1.png"))
# predicted_img = model.predict(img)
# print(np.argmax(predicted_img))