import os


def retrieve_fit_files(fullPathVar):
    array = []

    for fitFile in os.listdir(fullPathVar):
        fullPath = os.path.join(fullPathVar, fitFile)
        array.append(fullPath)

    return array