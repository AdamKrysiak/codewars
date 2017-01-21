__author__ = 'adam'


def order(sentence):
    return sorted(sentence.split(" "),key=lambda word: sorted(list(word))[0])


if __name__ == '__main__':
    print(order("is2 Thi1s T4est 3a"))