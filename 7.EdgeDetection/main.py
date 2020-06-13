import cv2
import numpy as np
from PIL import Image


def get_image(path):
    return Image.open(path).convert("L")


def convert_pixels_array_to_image(pixels):
    return Image.fromarray(pixels)


def get_image_pixels_array(image):
    return np.array(image)


def get_edges(image):
    image_pixels = get_image_pixels_array(image)
    edges = cv2.Canny(image_pixels, threshold1=100, threshold2=180)
    return convert_pixels_array_to_image(edges)


image = get_image("dog_cropped_grayscaled.jpg")
edges = get_edges(image)

edges.show()
