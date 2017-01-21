__author__ = 'adam'
import re
dict = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F',
        '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L' ,
        '--':'M' , '-.':'N', '---':'O', '.--.':'P', '--.-':'Q' , '.-.':'R',
        '...':'S', '-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
        '-.--':'Y', '--..':'Z'}

def decodeMorse(morseCode):
        return " ".join(["".join([dict.get(letter) for letter in word.split()]) for word in morseCode.strip().split("   ")])

def test():
        assert decodeMorse('.... . -.--   .--- ..- -.. .')== 'HEY JUDE'
