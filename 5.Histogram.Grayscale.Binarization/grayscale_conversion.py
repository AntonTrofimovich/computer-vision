from PIL import Image
import numpy as np

def get_image(path):
    return Image.open(path)

def get_image_dimensions(image):
    return image.size[0], image.size[1]

def get_image_pixels(image):
    return image.load()

def get_grayscaled_pixel(r, g, b):
    grey = int(r * 0.299) + int(g * 0.587) + int(b * 0.114);
    return (grey, grey, grey)

def get_grayscaled_image(image_pixels, image_width, image_height):
    img = Image.new('RGB', (image_width, image_height))

    for row_index in range(image_width):
        for col_index in range(image_height):
            r, g, b = image_pixels[row_index, col_index]
            grayscaled_pixel = get_grayscaled_pixel(r, g, b);
            img.putpixel((row_index, col_index), grayscaled_pixel)
    
    return img

image = get_image('dog_cropped.jpg')
image_width, image_height = get_image_dimensions(image)
image_pixels = get_image_pixels(image)

grayscaled_image = get_grayscaled_image(image_pixels, image_width, image_height)
# grayscaled_image.show()
grayscaled_image.save("dog_cropped_grayscaled.jpg")





