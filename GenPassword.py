import random

from random import randint


def get_letters():

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u' 'v', 'w', 'x'
                'y', 'z']

    select_letter = random.choice(alphabet)

    print(select_letter)


get_letters()
