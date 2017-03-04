import string
from random import randint, shuffle, choice


def password_gen():
    total = randint(3,17)
    password = [choice(string.letters + string.digits) for i in range(total)]+[rand_str(48, 57),str(unichr(randint(65, 90))), str(unichr(randint(97, 122)))]
    shuffle(password)
    return "".join(password)


def rand_str(a,b):
    repeat = randint(a,b)
    return [str(unichr(randint(a, b))) for i in range(repeat)][b-a]


if __name__ == '__main__':
    print password_gen()
