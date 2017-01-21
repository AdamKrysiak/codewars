import re
def autocorrect(input):
    return re.sub(r"(?<![a-z])[Yy]o[u]+(?![a-z])|(?<![a-z])u(?![a-z])", "your sister", input)



def test0():
    assert autocorrect("do you like me")=="do your sister like me"

def test1():
    assert autocorrect("u")=="your sister"

def test2():
    assert autocorrect("you")=="your sister"

def test3():
    assert autocorrect("Youuuuu")=="your sister"

def test4():
    assert autocorrect("youtube")=="youtube"

def test5():
    assert autocorrect('I miss you!') == 'I miss your sister!'

def test6():
    assert autocorrect('u want to go to the movies?') == 'your sister want to go to the movies?'

def test7():
    assert autocorrect('I want to film the bayou with u and put it on youtube') == \
           'I want to film the bayou with your sister and put it on youtube'
def test8():
    assert autocorrect('You youville utube you youyouyou uuu raiyou united youuuu u you') == \
           'your sister youville utube your sister youyouyou uuu raiyou united your sister your sister your sister'

