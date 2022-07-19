import random
import os

seed = None
size = 40


def setup_seed():
    global seed, size
    seed = os.urandom(size)


def get_seed():
    global seed
    return seed


def insert_seed():
    random.seed(a=get_seed())


def main():
    setup_seed()
    insert_seed()

    n = Neuron()

    inp = random.uniform(-1.5, 1.5)
    w = 4 #random.uniform(-1.5, 1.5)

    n.set_input(inp)
    n.set_weight(w)

    n.calculate()

    n.print_state()
    pass


if __name__ == '__main__':
    main()
