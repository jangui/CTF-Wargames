#!/usr/bin/env python2
import subprocess, os
import struct

#p = process("./gibson", env={'LD_PRELOAD':'./libc-2.19.so'})
p = subprocess.Popen("./gibson", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#p = process("./gibson")
#libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")
#libc = ELF("./libc-2.19.so")

# gdb.attach(p, """
# b *0x401725
# """)

def p64(x):
    return struct.pack('<Q', x)

def u64(x):
    return struct.unpack('<Q', x)

def recvuntil(thingy):
    read = p.stdout.readline()
    #read = p.stdout.read(1)
    buf = read
    while buf.find(thingy) == -1:
        read = p.stdout.readline()
        buf += read
    print("receiving {}".format(buf))
    return buf

def sendline(thingy):
    print("emitting {}".format(thingy))
    p.stdin.write(thingy + "\n")


def main():
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()    
    print p.stdout.readline()    
main()
