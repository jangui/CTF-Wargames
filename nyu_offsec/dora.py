from pwn import *


for i in range(256):
    p = process("./dora")
    p.sendline(str(i))
    print "\n SENDING " + str(i) + "\n"
    print p.recvall() 




