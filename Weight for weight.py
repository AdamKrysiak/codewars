__author__ = 'adam'


def order_weight(strng):
    return " ".join(sorted(strng.split(" "), key = orderKey))

def orderKey(str):
    sum=0
    for i in list(str):
        sum+=int(i)
    return sum+int(list(str)[0])*0.1

if __name__ == '__main__':
    print(order_weight("103 123 4444 99 2000"))