import os

DIRECTORY = "/home/qwerty/PycharmProjects/Python_life_hacks/rename_file/Test"


def renames_files(directory):
    for root, dir, file in os.walk(directory):
        for name in file:
            rename_file(root, name)


def rename_file(root, name):
    valid_name = valid_rename(name)
    old_name = os.path.join(root, name)
    new_name = os.path.join(root, valid_name)
    os.replace(old_name, new_name)


def valid_rename(name):
    name = name.replace("_Diff.", "_BC.")
    name = name.replace("_Diffuse.", "_BC.")
    name = name.replace("_ORM.", "_AORM.")
    name = name.replace("_Normal.", "N.")
    name = name.replace("_O.", "_A.")
    if not name.startswith("T_"):
        name = "T_" + name
    return name


if __name__ == '__main__':
    renames_files(DIRECTORY)