import hashlib
from random import randint



def main():
    active = True
    while active:
        a = randint(65, 90)
        b = randint(97, 122)
        c = randint(65, 90)
        d = randint(97, 122)
        message = chr(a) + chr(b) + chr(c) + chr(d)
        hashed = hashlib.sha224(message.encode("utf-8")).hexdigest()
        if hashed[0:2] == '0e':
            print(message)
            return message

main()