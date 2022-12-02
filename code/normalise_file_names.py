# !/usr/bin/python
import os

toBeRemoved = "OpenHardwareMonitorLog-2022-11-"
sizeOfRemoval = 0


def remove_text_area_size():
    global toBeRemoved, sizeOfRemoval

    if sizeOfRemoval == 0:
        sizeOfRemoval = len(toBeRemoved)

    return sizeOfRemoval


def normalise(path):
    for root, dirs, files in os.walk(path, topdown=False):

        for name in files:
            f = os.path.join(root, name)

            if has_openhardware_stamp(name):
                rename(f, root, name)
        pass


def has_openhardware_stamp(name):
    if 'OpenHardwareMonitorLog' in name:
        return True
    return False


def rename(old, dir, name):
    newName = name[remove_text_area_size():len(name)]
    newPath = os.path.join(dir, newName)

    os.rename(old, newPath)


pathTo = """C:\\Workspace\\common hardware initiative\\Archive\\dataset\\csv"""
normalise(pathTo)