import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import numpy as np

def display_images(train_images, train_labels, indexes):

    sample_images = []
    sample_labels = []

    for index in indexes:
        sample_images.append(train_images[index])
        sample_labels.append(train_labels[index])

    # Map the one-hot encoded labels back to integers
    #sample_labels = [label.argmax() for label in sample_labels]

    # Plot the images
    plt.figure(figsize=(10, 2))
    for i, idx in enumerate(indexes):
        plt.subplot(1, len(indexes), i + 1)
        plt.imshow(sample_images[idx].reshape(28, 28), cmap='gray')
        plt.title(f'Digit: {sample_labels[idx]}')
        plt.axis('off')

    plt.show()

def load_image(path):
    img = Image.open(path).convert('L')  # Convert to grayscale

    inverted = ImageOps.invert(img)

    inverted = inverted.resize((28, 28))

    img_array = np.array(inverted).astype('float32') / 255
    img_array = img_array.reshape((1, 28, 28, 1))

    

    #display_images([img_array], [""], [0])

    return img_array