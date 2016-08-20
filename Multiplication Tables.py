import sys
def multiplication_table(row,col):
    x=[[0 for x in range(col)]for y in range(row)]
    for i in range(1,row+1):
        for j in range(1,col+1):
            x[i-1][j-1] = i*j
    return x


if __name__ == '__main__':
    for row in multiplication_table(10,3):
        for i in row:
            sys.stdout.write(str(i)+" ")
        print("\n")
    print(multiplication_table(3,3))