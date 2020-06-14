from PIL import Image
import numpy as np
import cv2


def get_image(path):
    return Image.open(path)


def convert_pixels_array_to_image(pixels):
    return Image.fromarray(pixels)


def get_image_pixels_array(image):
    return np.array(image)


def get_grayscaled_image(image):
    return image.convert("L")


def get_image_size(image):
    return (image.size[0], image.size[1])


def get_image_size_by_pixels(pixels):
    return (len(pixels), len(pixels[0]))


def get_deviations_list(area_size):
    half_area_size = area_size // 2

    return [i - half_area_size for i in range(area_size)]


def create_surrounding_pixels_getter_function(area_size, pixels):
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

                if area_col_index < 0 or area_col_index > img_width - 1 or (area_row_index, area_col_index) == pixel_position:
                    continue

                surrounding_pixel_position = (area_row_index, area_col_index)
                surrounding_pixel_value = pixels[area_row_index][area_col_index]

                result.append((surrounding_pixel_position,
                               surrounding_pixel_value))

        return result

    return get_surrounding_pixels


def create_segment_getter_function(image, seed_pixel, threshold):
    image_pixels_array = get_image_pixels_array(image)
    get_surrounding_pixels = create_surrounding_pixels_getter_function(
        3, image_pixels_array)

    width, height = get_image_size(image)

    processed_pixels_count = 0
    pixels_count = width * height

    seed_pixel_row_index, seed_pixel_col_index = seed_pixel
    seed_pixel_value = image_pixels_array[seed_pixel_row_index,
                                          seed_pixel_col_index]

    processed_pixels = []

    def mark_as_processed(pixel_positions):
        nonlocal processed_pixels
        processed_pixels += pixel_positions

    def has_been_processed(pixel_position):
        return pixel_position in processed_pixels

    def get_unprocessed_pixels(surrounding_pixels):
        unprocessed_surrounding_pixels = [
            (position, value) for position, value in surrounding_pixels if has_been_processed(position) == False]

        return (
            [position for position, value in unprocessed_surrounding_pixels],
            [int(value) for position, value in unprocessed_surrounding_pixels]
        )

    def get_segment(current_pixel_position):
        result = []
        nonlocal processed_pixels_count

        if processed_pixels_count == pixels_count:
            return result

        mark_as_processed(current_pixel_position)

        surrounding_pixels = get_surrounding_pixels(current_pixel_position)

        unprocessed_pixels_positions, unprocessed_pixels_values = get_unprocessed_pixels(surrounding_pixels)

        if (len(unprocessed_pixels_positions) == 0):
            return result

        mark_as_processed(unprocessed_pixels_positions)

        intencity_diffs_list = [abs(pixel_value - seed_pixel_value)
                                for pixel_value in unprocessed_pixels_values]

        suitable_pixels_positions = [unprocessed_pixels_positions[i] for i, v in enumerate(
            intencity_diffs_list) if v < threshold]

        if (len(suitable_pixels_positions) == 0):
            return result

        result.append(current_pixel_position)

        processed_pixels_count += 1

        for position in suitable_pixels_positions:
            result += get_segment(position)

        return result

    return get_segment


def apply_segment_on_image(image, segment):
    pixels_array = get_image_pixels_array(image)
    for pixel_position in segment:
        pixel_row_index, pixel_col_index = pixel_position
        pixels_array[pixel_row_index][pixel_col_index] = 255

    return convert_pixels_array_to_image(pixels_array)


def get_segmented_image(image, seed_point, threshold=1):
    grayscaled_image = get_grayscaled_image(image)
    seed_col_index, seed_row_index = seed_point

    get_segment = create_segment_getter_function(
        grayscaled_image, (seed_row_index, seed_col_index), threshold
    )
    
    segment = get_segment((seed_row_index, seed_col_index))

    segmented_grayscaled_image = apply_segment_on_image(
        grayscaled_image, segment
    )
    return segmented_grayscaled_image


image = get_image("dog_cropped_grayscaled.jpg")
point_on_nose_coord = [102, 137]
segmented_image = get_segmented_image(image, point_on_nose_coord, threshold=20)

segmented_image.save("dog_cropped_grayscaled_segmented.jpg")
