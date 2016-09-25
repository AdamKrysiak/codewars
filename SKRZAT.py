def skrzat(base, number):
    if base == 'b':
        return "From binary: " + str(number) + " is " + str(
            sum([(-2) ** i for i, numb in enumerate(list(str(number))[::-1]) if numb == '1']))
    elif base == 'd':
        return "From decimal: " + str(number) + " is " + get_bin(number)
    else:
        pass

def get_bin(number):
    div=-number
    binary=""
    if number==0: return "0"
    while div!=0:
        div, rest = divmod(div,-2)
        if rest==-1:
            binary+="1"
        else:
            binary+="0"
    return binary[::-1]

def test():
    assert skrzat('b', '1001101') == 'From binary: 1001101 is 61'


def test2():
    assert skrzat('d', 137) == 'From decimal: 137 is 110011001'


def test3():
    assert skrzat('d', -137) == 'From decimal: -137 is 10001011'


def test4():
    assert skrzat('d', 0) == 'From decimal: 0 is 0'

def test5():
    assert skrzat('d', 21000) == 'From decimal: 21000 is 101011000011000'
