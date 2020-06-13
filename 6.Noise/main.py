
import numpy as np
from PIL import Image

def get_image(path):
    return Image.open(path).convert("L")

def convert_pixels_array_to_image(pixels):
    return Image.fromarray(pixels)

def get_image_pixels_array(image):
    return np.array(image)

def get_deviations_list(area_size):
    half_area_size = area_size // 2

    return [i - half_area_size for i in range(area_size)]

def get_image_size_by_pixels(pixels):
    return (len(pixels), len(pixels[0]))

def create_surrounding_pixels_getter_function(area_size, pixels):
    half_area_size = area_size // 2
    img_height, img_width = get_image_size_by_pixels(pixels)

    def get_surrounding_pixels(pixel_position):
        row_index, col_index = pixel_position
        deviations = get_deviations_list(area_size)

        result = []
        for row_deviation in deviations:
            area_row_index = row_index + row_deviation

            if area_row_index < 0 or area_row_index > img_height - 1:
                continue

            for column_deviation in deviations:
                area_col_index = col_index + column_deviation

                if area_col_index < 0 or area_col_index > img_width - 1:
                    continue

                result.append(pixels[area_row_index]
                            [area_col_index])
        
        
        return result

    return get_surrounding_pixels


def apply_median_filter(image, area_size):
    pixels = get_image_pixels_array(image)
    get_surrounding_pixels = create_surrounding_pixels_getter_function(area_size, pixels)

    height, width = get_image_size_by_pixels(pixels)
    result = pixels

    for row_index in range(height):
        for col_index in range(width):
            surrounding_pixels = get_surrounding_pixels((row_index, col_index))
            surrounding_pixels.sort()

            result[row_index][col_index] = surrounding_pixels[len(surrounding_pixels) // 2]

    return convert_pixels_array_to_image(result)

binary_image_with_noise = get_image("dog_binary.jpg")
unnoised_binary_image = apply_median_filter(binary_image_with_noise, 3)
unnoised_binary_image.save("dog_binary_unnoised.jpg")

grayscaled_image_with_moise = get_image("grayscaled_image_with_noise.png")
unnoised_grayscaled_image = apply_median_filter(grayscaled_image_with_moise, 5)
unnoised_grayscaled_image.save("unnoised_grayscaled_image.png")
