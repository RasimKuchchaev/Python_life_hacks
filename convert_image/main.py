import os

from PIL import Image

DIRECTORY = 'img'
FROM_EXTENSION = ".jpg"
TO_EXTENSION = ".png"
MAX_SIZE = (1024, 1024)


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            # print(name)
            conversion(os.path.join(root, name))


def conversion(file):
    image_resize(file)
    name, extension = os.path.splitext(file)
    '''
    os.path.splitext(file) возвращает кортеж из пути c именем файла и расширением
    ('img/T_SpeedPlant_BC', '.png')
    '''
    if extension == FROM_EXTENSION:
        im = Image.open(file)
        im.save(name + TO_EXTENSION)
        os.remove(file)


def image_resize(file):
    im = Image.open(file)
    im.thumbnail(MAX_SIZE)
    im.save(file)


if __name__ == '__main__':
    walk(DIRECTORY)
