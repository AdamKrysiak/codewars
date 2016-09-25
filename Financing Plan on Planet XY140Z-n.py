


# def finance(n):
#     z=0
#     for x in range(0,n+1):
#         z+= sum(range(2*x,n+1+x))
#     return z

finance = lambda n: sum(map(lambda x : sum(range(2*x,n+1+x)) , range(0,n+1)))

def test():
    assert finance(5) == 105

def test2():
    assert finance(6) == 168

def test3():
    assert finance(8) == 360

def test24():
    assert finance(15) == 2040