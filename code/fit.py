import fitparse
import os

import iterator
import parseGarmin

rootPath = '''D:\\Workspace\\data\\data.garmin.general\\dataset'''

current_year = ''
current_month = ''
current_day = ''


def main():
    global rootPath, current_year

    for Year in os.listdir(rootPath):
        current_year = Year
        fullPath = os.path.join(rootPath, Year)

        if os.path.isdir(fullPath):
            year(fullPath)

    pass


def year(year_string):
    global current_month
    for Month in os.listdir(year_string):
        fullPath = os.path.join(year_string, Month)
        current_month = Month

        if os.path.isdir(fullPath):
            month(fullPath)
    pass


def month(month_string):
    global current_day
    for Day in os.listdir(month_string):
        fullPath = os.path.join(month_string, Day)
        current_day = Day

        if os.path.isdir(fullPath):
            day(fullPath)
    pass


def day(day_path):
    global current_year, current_month, current_day
    fitFiles = parseGarmin.retrieve_fit_files(day_path)


    pass


main()
