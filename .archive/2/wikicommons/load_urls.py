
def load_lists(path_to):
    list = []
    open_file = None

    try:
        open_file = open(path_to, 'r', encoding='utf-8')

        for line in open_file.readlines():
            list.append(line)

    finally:
        open_file.close()

    return list
