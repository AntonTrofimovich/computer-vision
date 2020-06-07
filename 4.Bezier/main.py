from PIL import Image, ImageDraw
import numpy as np

def qubic_bezier(directional_points, parameter):
    P0, P1, P2, P3 = [np.array(point) for point in directional_points]

    result = (1 - parameter)**3 * P0 + 3 * (1 - parameter)**2 * parameter * P1 + 3 * (1 - parameter) * parameter**2 * P2 + parameter**3 * P3
    return [curve_point for curve_point in result]

def get_curve(directional_points):
    curve = [];

    for parameter in range(101):
        curve.append(tuple(qubic_bezier(directional_points, parameter / 100)))

    return curve

def draw_curve(curve, draw):
    for index in range(len(curve) - 1):
        line = [curve[index], curve[index + 1]]
        draw.line(line, fill="red", width=2)

    return draw

def draw_directional_lines(directional_points, draw):
    for index in range(len(directional_points) - 1):
        line = [directional_points[index], directional_points[index + 1]]
        draw.line(line, fill="black", width=1)
    
    return draw

image = Image.new('RGB', (350, 350), (255, 255, 255))
draw = ImageDraw.Draw(image)

directional_points = [(57.0, 122.0), (172.0, 37.0), (268.0, 123.0), (252.0, 252.0)]
draw = draw_directional_lines(directional_points, draw)

curve = get_curve(directional_points)
draw = draw_curve(curve, draw)

image.show()
