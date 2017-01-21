__author__ = 'adam'

def count(int):
   return '{0:b}'.format(int).count('1')


if __name__ == '__main__':
    print(count(0))