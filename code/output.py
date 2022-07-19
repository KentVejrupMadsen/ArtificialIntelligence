from output import title, log

def __make_title_line(max_size=100, initial_size=0):
    result = ''

    for i in range(max_size - initial_size):
        result = result + '='

    return str( result )


def __make_space(line=str, length=4):
    value = ''

    for i in range(length):
        value = value + ' '

    result = value + line

    return result

def __make_log_line(name, value):
    result = ''
    return str(result)


def title(name):
    strResult = name + ' '

    Result = strResult + __make_title_line(initial_size=len(strResult))

    print(Result)


def log(name, value):
    log = str(name) + ', (' + str(value) + ')'
    result = __make_space(line=log)

    print(result)