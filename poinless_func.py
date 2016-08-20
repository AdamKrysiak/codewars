__author__ = 'adam'
def pointless(*args):
    return args[::-1]

if __name__ == '__main__':
    print(pointless(2,3,1,122))