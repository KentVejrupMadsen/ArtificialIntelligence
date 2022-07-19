import random

from neuron import Neuron
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

    print('testing')
    print(random.uniform(1.0, 200.0))

    n = Neuron()
    n.set_input(2)

    n.calculate()
    print(n.get_output())
    pass


if __name__ == '__main__':
    main()
