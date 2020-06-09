import matplotlib.pyplot as plot;

def read_image(path):
    return plot.imread(path)

def create_histogram(image):
    plot.hist(image.ravel(), bins=256)
    return plot

image = read_image("dog_cropped.jpg")
histogram = create_histogram(image)

histogram.show()
