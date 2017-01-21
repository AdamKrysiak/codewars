import re
def solution(string,markers):
    for marker in markers:
        string=re.sub(r"[ \t\r\f\v]*"+"\\"+marker+".*","",string)
    return string


def test():
    assert solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])=="apples, pears\ngrapes\nbananas"
    assert solution("a #b\nc\nd $e f g", ["#", "$"])== "a\nc\nd"