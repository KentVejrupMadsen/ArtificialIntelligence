from fitparse \
    import FitFile

import os

import iterator
import parseGarmin

rootPath = '''D:\\Workspace\\data\\data.garmin.general\\dataset'''
exportTo = '''D:\\Workspace\\codespace\\Codespace.Python\\sample'''

current_year = ''
current_month = ''
current_day = ''


def main():
    global rootPath, \
           current_year, \
           exportTo

    for Year in os.listdir(rootPath):
        current_year = Year

        ex_to_fp = os.path.join(exportTo, current_year)
        if not os.path.exists(ex_to_fp):
            os.mkdir(ex_to_fp)

        print(current_year)

        fullPath = os.path.join(rootPath, Year)

        if os.path.isdir(fullPath):
            year(fullPath)


def year(year_string):
    global current_year, \
           current_month, \
           exportTo

    for Month in os.listdir(year_string):
        fullPath = os.path.join(year_string, Month)
        current_month = Month
        print('     ' + current_month)

        ex_to_fp = os.path.join(exportTo, current_year)
        ex_to_fp = os.path.join(ex_to_fp, current_month)

        if not (os.path.exists(ex_to_fp)):
            os.makedirs(ex_to_fp)

        if os.path.isdir(fullPath):
            month(fullPath)


def month(month_string):
    global current_year, \
           current_month, \
           current_day, \
           exportTo

    for Day in os.listdir(month_string):
        fullPath = os.path.join(month_string, Day)
        current_day = Day

        ex_to_fp = os.path.join(exportTo, current_year)
        ex_to_fp = os.path.join(ex_to_fp, current_month)
        ex_to_fp = os.path.join(ex_to_fp, current_day)

        if not (os.path.exists(ex_to_fp)):
            os.makedirs(ex_to_fp)

        print('          ' + current_day)

        if os.path.isdir(fullPath):
            day(fullPath)


todayBuffer = []


def day(day_path):
    global current_year, \
           current_month, \
           current_day, \
           todayBuffer

    todayBuffer = []
    fit_files = parseGarmin.retrieve_fit_files(day_path)

    iterate_files(fit_files)


def iterate_files(files):
    i = iterator.Iterator()
    i.set_size(len(files))

    while i.continue_iterating():
        current = files[i.currentPos]
        parseFit(current)

        i.next()


def parseFit(path):
    fit = FitFile(path)
    print('               ' + path)

    # Current Time
    ct = 0

    fit.parse()

    for record in fit.get_messages():
        if record.get_values().__contains__('timestamp'):
            ct = record.get_value('timestamp')
#            print('T:' + ct.strftime("%H:%M:%S"))

        if record.get_values().__contains__('local_timestamp'):
            ct = record.get_value('local_timestamp')
#            print('LT: ' + ct.strftime("%H:%M:%S"))

        if record.get_values().__contains__('heart_rate'):
            actual_timestamp = parseGarmin.get_timestamp(ct, record.get_value('timestamp_16'))
            print(actual_timestamp)
            print(record.get_value('heart_rate'))


    fit.close()


main()
