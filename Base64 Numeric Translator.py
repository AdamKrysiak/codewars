base64_characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
def base64_to_base10(str):
    return sum([base64_characters.index(sign)*pow(64,i) for i,sign in enumerate(list(str)[::-1])])

if __name__ == '__main__':
    print(base64_to_base10("A"  ), 0 )
    print(base64_to_base10("/"  ), 63   )
    print(base64_to_base10("BA" ), 64   )
    print (base64_to_base10("//" ), 4095 )
    print (base64_to_base10("WIN"), 90637)