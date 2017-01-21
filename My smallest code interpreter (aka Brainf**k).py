class Brainfuck_mashine:
    tape = [0] * 256
    pointer = 0
    while_open_list = []
    code = []
    safe_copy_of_code = []
    code_ptr = 0
    out_str = ""
    input = ""
    function_map = {}

    def __init__(self):
        self.function_map = {">": self.inc_ptr, "<": self.dec_ptr, "+": self.inc_byte,
                             "-": self.dec_byte, ",": self.input_byte, ".": self.output_byte,
                             "[": self.add_open, "]": self.go_to_open, "0": self.zero}

    def zero(self):
        pass

    def inc_ptr(self):
        self.pointer = (self.pointer + 1) % 256

    def dec_ptr(self):
        self.pointer = (self.pointer - 1) % 256

    def inc_byte(self):
        self.tape[self.pointer] = (self.tape[self.pointer] + 1) % 256

    def dec_byte(self):
        self.tape[self.pointer] = (self.tape[self.pointer] - 1) % 256

    def output_byte(self):
        # sys.stdout.write(chr(self.tape[self.pointer]))
        self.out_str += ""+chr(self.tape[self.pointer])

    def input_byte(self):
        self.tape[self.pointer] = ord(self.input[0])
        self.input = self.input[1:]

    def go_to_open(self):
        if self.tape[self.pointer] == 0:
            self.code[self.code_ptr] = "0"
            self.code[self.while_open_list[-1]] = "0"
            self.while_open_list.pop()
        else:
            self.code_ptr = self.while_open_list[-1]
            self.code[self.code_ptr:] = self.safe_copy_of_code[self.code_ptr:]

    def add_open(self):
        if self.code_ptr in self.while_open_list:
            pass
        else:
            self.while_open_list.append(self.code_ptr)

        if self.tape[self.pointer] == 0:
            self.code[self.code_ptr] = "0"
            for x, i in enumerate(self.code[self.code_ptr:]):
                if x == ']':
                    self.while_open_list.pop()
                    self.code_ptr = i
                    self.code[self.code_ptr] = '0'
                    break

    def get_next_code(self):
        return self.code[self.code_ptr]

    def interprete(self, code="", input=""):
        self.safe_copy_of_code = list(code) + [';']
        self.code = list(code) + [';']
        self.input = list(input)
        while self.get_next_code() != ';':
            temp = self.code[self.code_ptr:]
            actual_instruction = self.code[self.code_ptr]
            self.function_map[self.code[self.code_ptr]]()
            self.code_ptr += 1
        return self.out_str


def brain_luck(code, input_code):
    print(code, input_code)
    x = Brainfuck_mashine()
    score = x.interprete(code, input_code)
    print format(ord(score[0]), '02x')
    return score


if __name__ == '__main__':
    print brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', '\x08\t')
