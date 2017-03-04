def get_array(size):
    return [[0] * size for i in range(size)]


def spiralize(size):
    # Make a snake
    if size==0:
        return []
    spiral = get_array(size)
    return get_spiral(spiral, 0)


def get_spiral(spiral, start_index):
    size = len(spiral[0])
    for i in range(start_index, size - start_index):
        for j in range(start_index, size - start_index):
            if i == start_index or i == size - 1 - start_index:
                spiral[i][j] = 1
            if j == size - 1 - start_index or (j == start_index and i != 1 + start_index):
                spiral[i][j] = 1
            if j == start_index + 1 and i == start_index + 2:
                spiral[i][j] = 1
    if start_index <= len(spiral[0]) / 2:
        get_spiral(spiral, start_index + 2)
    if size % 2 == 0:
        spiral[int(size / 2)][int(size / 2) - 1] = 0
    return spiral


if __name__ == '__main__':
    # print (get_array(10))
    for i in spiralize(6):
        print(i)




        #
        # 0000000000
        # .........0
        # 00______.0
        # 0.______.0
        # 0.______.0
        # 0.______.0
        # 0.______.0
        # 0.______.0
        # 0........0
        # 0000000000

        # 000000
        # .....0
        # 00__.0
        # 0.__.0
        # 0....0
        # 000000

        # 00
        # .0
