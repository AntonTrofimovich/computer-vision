from PIL import Image
import numpy as np

def get_image(path):
    return Image.open(path)

def get_binarized_image(image, threshold):
    image_pixels_array = np.array(image);
    image_pixels_binarized = (image_pixels_array > threshold) * 255

    return Image.fromarray(np.uint8(image_pixels_binarized))

grayscaled_image = get_image("dog_cropped_grayscaled.jpg")
binarized_image = get_binarized_image(grayscaled_image, threshold=160)

binarized_image.save("dog_cropped_grayscaled_binarized.jpg")