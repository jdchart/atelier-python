from tensorflow.keras.models import load_model
import os
import utils
import numpy as np

model = load_model(os.path.join(os.getcwd(), "sessions", "session-6", "data", "model_out.keras"))

img = utils.load_image(os.path.join(os.getcwd(), "sessions", "session-6", "data", "3.png"))
predicted_img = model.predict(img)
print(np.argmax(predicted_img))
print(predicted_img)