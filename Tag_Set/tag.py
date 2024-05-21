# pip install eyed3     -   tag
# pip install transliterate     -   перевод кирилицы в латинские символы
import os
import eyed3
import transliterate

FIND_DIRECTORY = r"/home/qwerty/PycharmProjects/Python_life_hacks/Tag_Set/other"


def walk(directory):
    for root, dirs, files in os.walk(directory):
        for name in files:
            set_tag(os.path.join(root, name))


def set_tag(file):
    name = os.path.basename(file).split(".")[0]
    audiofile = eyed3.load(file)
    audiofile.tag.album = "The Edge"
    audiofile.tag.title = transliterate.translit(name, reversed=True)
    audiofile.tag.save()


if __name__ == '__main__':
    walk(FIND_DIRECTORY)
