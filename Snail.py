


def snail(array):
    snail_way=[]
    if array==[[]]:
        return []
    if len(array[0])==1:
        return array[[0][0]]
    get_circut(array, snail_way)
    return snail_way

def get_circut(array, snail_way):
    length = len(array[0])
    for x in range(length):
        snail_way.append(array[0][x])
    for x in range(1,length):
        snail_way.append(array[x][length-1])
    for x in range(length-2,0,-1):
        snail_way.append(array[length-1][x])
    for x in range(length-1,0,-1):
        snail_way.append(array[x][0])
    if length==3:
        snail_way.append(array[1][1])
        return  snail_way
    if length==2:
        return snail_way
    get_circut([row[1:-1] for row in array[1:-1]],snail_way)


def test_1():
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    assert snail(array)== expected

def test_2():
    array = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    expected = [1,2,3,4,5,6,7,8,9]
    assert snail(array)== expected

def test_3():
    array = [[1,2,3,4],
             [4,5,6,7],
             [7,8,9,10],
             [11, 12, 13, 14]]
    expected = [1,2,3,4,7,10,14,13,12,11,7,4,5,6,9,8]
    assert snail(array)== expected

def test_4():
    array = [[ 1, 2, 3, 4, 5],
             [ 6, 7, 8, 9,10],
             [11,12,13,14,15],
             [16,17,18,19,20],
             [21,22,23,24,25]]

    expected = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
    assert snail(array)== expected

def test_5():
    assert snail([[1]])==[1]