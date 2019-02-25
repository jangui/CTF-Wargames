from pwn import *

option = 0
ans = ['L', 'R', 'LR' 'RL']


while 1==1:
    p = process("./labyrinth")
    #p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1337)
    p.recvuntil("?")
    #p.sendline('jd3846')
    #gdb.attach(p)
    if (option%2) == 0:
        let = 'L'
        ans += let
    else:
        let = 'R'



    p.sendline("")
    p.interactive()
    option += 1
