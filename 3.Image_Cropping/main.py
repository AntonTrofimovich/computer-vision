from PIL import Image

original_image = Image.open('dog.jpg')

original_image.crop((200, 75, 400, 400)).save("dog_cropped.jpg", quality=95)
