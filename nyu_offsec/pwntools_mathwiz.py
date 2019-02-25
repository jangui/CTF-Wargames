#!/usr/bin/env python
import time
import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    end = data.find("=")
    start = data.find("!\n") + 2
    print end
    ls = data[start:end+1].split(" ")
    print ls
    op = ls[1]
    try:
        n1 = int(ls[0])
    except:
        try:
            n1 = int(ls[0], 2)
        except:
            try:
                n1 = int(ls[0], 16)
            except:
                n1 = ls[0].split("-")
                n = []
                temp = None
                for l in n1:
                    print l
                    if l =='ONE':
                        temp = '1'
                    elif l=='TWO':
                        temp = '2'
                    elif l=='THREE':
                        temp = '3'
                    elif l=='FOUR':
                        temp = '4'
                    elif l=='FIVE':
                        temp = '5'
                    elif l=='SIX':
                        temp = '6'
                    elif l=='SEVEN':
                        temp = '7'
                    elif l=='EIGHT':
                        temp = '8'
                    elif l=='NINE':
                        temp = '9'
                    elif l=='ZERO':
                        temp = '0'
                    n.append(temp)
                print n
                n1 = int("".join(n))

    try:
        n2 = int(ls[2])
    except:
        try:
            n2 = int(ls[2], 2)
        except:
            try:
                n2 = int(ls[2], 16)
            except:
                n2 = ls[2].split("-")
                print(n2)
                n = []
                temp = None
                for l in n2:
                    print l
                    if l =='ONE':
                        temp = '1'
                    elif l=='TWO':
                        temp = '2'
                    elif l=='THREE':
                        temp = '3'
                    elif l=='FOUR':
                        temp = '4'
                    elif l=='FIVE':
                        temp = '5'
                    elif l=='SIX':
                        temp = '6'
                    elif l=='SEVEN':
                        temp = '7'
                    elif l=='EIGHT':
                        temp = '8'
                    elif l=='NINE':
                        temp = '9'
                    elif l=='ZERO':
                        temp = '0'
                    n.append(temp)
                print n
                n2 = int("".join(n))



    if op == '+':
        ret = n1 + n2
    elif op == '-':
        ret = n1 - n2
    elif op == '*':
        ret = n1 * n2
    elif ret == '/':
        ret = n1 / n2

    print n1, n2, ret

    ret = str(ret).encode('utf-8')
    return ret

def pwn(address, port):
    connection = remote(address, port)
    # Let's print the data we receive from this server
    print connection.recvuntil(":")
    # Let's send it some data!
    connection.sendline("jd3846")

    response = connection.recvuntil("= ?")
    print response

    start = response.find("??") + 3
    end = response.find("=")
    ls = response[start:end].split(" ")

    op = ls[1]
    print ls
    n1 = int(ls[0])
    n2 = int(ls[2])

    if op == '+':
        ret = n1 + n2
    elif op == '-':
        ret = n1 - n2
    elif op == '*':
        ret = n1 * n2
    elif ret == '/':
        ret = n1 / n2

    ret = str(ret).encode('utf-8')
    connection.sendline(ret)
    print ret
    print "WE DID IT"
    # Let's print thihe data we receive from this server, but also store it
    for i in range(99):
        print i
        response = connection.recvuntil("?")
        print response
        # Hmm, they seem to be asking for some mathematical computations?
        # If we complete all these tasks, we will be rewarded with a flag!
        connection.sendline(processResponse(response))
    connection.interactive()


def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print "Usage: ./client.py [IP] [Port]"
        sys.exit(1)
    pwn(address, port)

if __name__ == "__main__":
    main()

