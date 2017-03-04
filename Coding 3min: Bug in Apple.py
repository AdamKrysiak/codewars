def sc(apple):
    return [(i,j)for i in range(len(apple)) for j in range(len(apple[i])) if apple[i][j] == "B"]


if __name__ == '__main__':
    apple = [
        ["A", "A", "A", "A", "A"],
        ["A", "B", "A", "A", "A"],
        ["A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A"],
        ["A", "A", "A", "A", "A"]
    ]
    print (sc(apple))
