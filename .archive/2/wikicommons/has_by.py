def hasByLabel(username, type):
    r = str()
    r = r + str(type) + ' by user:' + str(username).capitalize()
    return r


def hasBy( username, type, inputStr ):
    if hasByLabel(username, type).lower() in str(inputStr).lower():
        return True

    return False


if __name__ == '__main__':
    print(hasBy("designermadsen", "files", "[[category:Files by user:DesignerMadsen]]"))