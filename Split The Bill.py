def split_the_bill(x):
    sr = round(sum(x.values())/float(x.__len__()),2)
    for key in x.keys():
        x[key] = x[key]-sr
    return x

if __name__ == '__main__':
    print(split_the_bill({'A': 20, 'B': 15, 'C': 10}))
        # {'A': 5, 'B': 0, 'C': -5}