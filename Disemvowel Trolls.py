__author__ = 'adam'
import re


def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)



if __name__ == '__main__':
    print(disemvowel("This website is for losers LOL!"))