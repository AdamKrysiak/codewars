def is_valid_IP(strng):
    parts = strng.split(".")
    return len(parts) == 4 and (False not in [True if part.isdigit() and 1 <= int(part )<= 255 and part[0]!="0" else False for part in parts])

if __name__ == '__main__':
    print (is_valid_IP("192.60.10.111"))