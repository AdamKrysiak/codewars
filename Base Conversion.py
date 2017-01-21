alphabets = {
    'bin':'01',
    'oct':'01234567',
    'dec':'0123456789',
    'hex':'0123456789abcdef',
    'allow':'abcdefghijklmnopqrstuvwxyz',
    'allup':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'alpha':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'alphanum':'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'}

def convert(input, source, target):
    to_tenth(input, source)


def to_tenth(input,source):
    return sum([pow(alphabets.get(source).__len__(),i)*list(alphabets[source]).index(input) for i, input in enumerate(list(input)[::-1])])
def from_tenth(input,target):
    return sum([pow(alphabets.get(source).__len__(),i)*list(alphabets[source]).index(input) for i, input in enumerate(list(input)[::-1])])



if __name__ == '__main__':
    print(to_tenth("110", 'dec'))