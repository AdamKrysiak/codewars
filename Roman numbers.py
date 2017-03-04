class RomanNumerals:
    human_to_roman = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }
    roman_to_human = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @staticmethod
    def to_pair_list(iterable):
        a = iter(iterable)
        return zip(a, a)

    @staticmethod
    def from_roman(roman_number):
        total = 0
        numer_list = [RomanNumerals.roman_to_human[single_sign] for single_sign in list(roman_number)]
        if len(numer_list) % 2 != 0: numer_list.append(0)
        for i, j in RomanNumerals.to_pair_list(numer_list):
            if i >= j:
                total += i + j
            else:
                total += j - i
        return total

    @staticmethod
    def human_descending_generator():
        for human in sorted(RomanNumerals.human_to_roman.keys(), reverse=True):
            yield human

    @staticmethod
    def to_roman(human_numer):
        roman_number = ''
        generator = RomanNumerals.human_descending_generator()
        actual_checked = generator.__next__()
        while human_numer != 0:
            if human_numer - actual_checked < 0:
                actual_checked = generator.__next__()
            else:
                roman_number += RomanNumerals.human_to_roman[actual_checked]
                human_numer-=actual_checked
        return roman_number


def test_should_return_human_value_of_single_roman_number():
    assert RomanNumerals.from_roman('I') == 1
    assert RomanNumerals.from_roman('V') == 5
    assert RomanNumerals.from_roman('X') == 10
    assert RomanNumerals.from_roman('L') == 50
    assert RomanNumerals.from_roman('C') == 100
    assert RomanNumerals.from_roman('D') == 500
    assert RomanNumerals.from_roman('M') == 1000


def test_should_return_human_value_of_raising_roman_number():
    assert RomanNumerals.from_roman('MDCLXVI') == 1666
    assert RomanNumerals.from_roman('XVI') == 16
    assert RomanNumerals.from_roman('XVIII') == 18
    assert RomanNumerals.from_roman('XXXVIII') == 38


def test_should_reduce_number_if_smaller_sign_before_bigger():
    assert RomanNumerals.from_roman('IV') == 4
    assert RomanNumerals.from_roman('IXV') == 14


def test_should_return_roman_number_of_single_human_number():
    assert RomanNumerals.to_roman(1) == 'I'
    assert RomanNumerals.to_roman(5) == 'V'
    assert RomanNumerals.to_roman(10) == 'X'
    assert RomanNumerals.to_roman(50) == 'L'
    assert RomanNumerals.to_roman(100) == 'C'
    assert RomanNumerals.to_roman(500) == 'D'
    assert RomanNumerals.to_roman(1000) == 'M'


def test_should_return_roman_number_of_complicated_human_number():
    assert RomanNumerals.to_roman(1666) == 'MDCLXVI'
    assert RomanNumerals.to_roman(16) == 'XVI'
