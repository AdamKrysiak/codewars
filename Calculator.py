class Calculator(object):
    pri_operations = { "*": lambda x, y: x * y, "/": lambda x, y: x / y}
    sec_operations = { "+": lambda x, y: x + y, '-': lambda x, y: x - y}
    def evaluate(self, string):
        string = string.split(" ")

        for i in range(0,string.__len__()):
            if string[i] in self.pri_operations:
                string[i+1]=self.pri_operations[string[i]](float(string[i-1]),float(string[i+1]))
                string[i-1]=string[i]="."
        string = [x for x in string if x!="."]
        x=float(string[0])
        for i in string[1:]:
            if i in self.sec_operations:
                operation = self.sec_operations[i]
            else:
                x=operation(x,float(i))
        return round(x,3)


if __name__ == '__main__':
    print(Calculator().evaluate("1.1 * 2.2 * 3.3"))  # => 7
