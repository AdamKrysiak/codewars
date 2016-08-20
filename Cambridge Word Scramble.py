__author__ = 'adam'
from random import randint


def mix_words(string):
    result=""
    for word in string.split():
        sign=""
        if ord(word[-1])<64:
            sign+=word[-1]
            word=word[:-1]
        x= list(word)
        for a in range(1,len(x)-1):
            i=randint(1,a)
            j=randint(1,a)
            x[j],x[i] = x[i],x[j]
        result+="".join(x)+sign+" "
    return result[:-1]


if __name__ == '__main__':
    print(mix_words("scrambler, bambler"))
