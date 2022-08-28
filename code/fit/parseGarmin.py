import os, \
       datetime, \
       pytz


def retrieve_fit_files(fullPathVar):
    array = []

    for fitFile in os.listdir(fullPathVar):
        fullPath = os.path.join(fullPathVar, fitFile)
        array.append(fullPath)

    return array


def get_timestamp(last_timestamp, timestamp_16):
    timestamp = int(datetime.datetime.timestamp(last_timestamp)) - 631065600
    mesg = timestamp
    mesg += (timestamp_16 - (mesg & 0xFFFF)) & 0xFFFF

    result = datetime.datetime.fromtimestamp((mesg + 631065600), pytz.timezone('Europe/Copenhagen'))
    return result