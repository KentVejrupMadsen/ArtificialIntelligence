import pywikibot
from content import values

site = pywikibot.Site()

page = None


def textToArray():
    global page
    arrayValues = page.text.splitlines()
    return arrayValues


def hasTakenOn():
    findTakenOn = textToArray()

    for line in findTakenOn:
        if '{{taken on'.lower() in line.lower():
            return True
    return False


def insert_taken_on():
    content = textToArray()
    result = ''

    for line in content:
        if '|date=' in line:
            seperated = line.split("=")

            newLine = seperated[0] + '=' + "{{taken on|"
            newLine = newLine + seperated[1] + '|location=denmark}}'

            result = result + newLine + '\n'
        else:
            result = result + line + '\n'

    return result


def apply(newPage):
    global page
    page.text = newPage


def found_location():
    for line in textToArray():
        if "{{Location|".lower() in line.lower():
            return True

    return False


def found_midjourney_category():
    for line in textToArray():

        if str.lower("[[category:Midjourney works by Designermadsen") in str.lower(line):
            return True

    return False


def found_photographed_by():
    for line in textToArray():
        if str.lower("Photographs by DesignerMadsen") in str.lower(line):
            return True

    return False


def not_qualified():
    global page

    if found_location():
        return False

    if found_photographed_by():
        return False

    print('warning: not qualified \r\n')
    return True


def main():
    global page, site
    remove = 'https://commons.wikimedia.org/wiki/'
    size = len(remove)

    # Removes the url part
    for line in values():
        if len(line) == 0:
            pass
        else:
            page_name = line[size:len(line)]
            page = pywikibot.Page(site, page_name)

            print('current: ' + page_name)

            if not_qualified():
                pass
            else:
                if not hasTakenOn():
                    apply(insert_taken_on())
                    print(page.text)
                    page.save('added taken on template with location')


if __name__ == '__main__':
    main()