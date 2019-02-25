import sys

def glibc_prng(seed):
    def int32(x): return x & 0xffffffff - \
        0x100000000 if x & 0xffffffff > 0x7fffffff else x & 0xffffffff

    def int64(x): return x & 0xffffffffffffffff - \
        0x10000000000000000 if x & 0xffffffffffffffff > 0x7fffffffffffffff else x & 0xffffffffffffffff

    r = [0] * 344
    r[0] = seed

    for i in range(1, 31):
        r[i] = int32(int64(16807 * r[i - 1]) % 0x7fffffff)

        if r[i] < 0:
            r[i] = int32(r[i] + 0x7fffffff)

    for i in range(31, 34):
        r[i] = int32(r[i - 31])

    for i in range(34, 344):
        r[i] = int32(r[i - 31] + r[i - 3])

    i = 344 - 1

    while True:
        i += 1
        r.append(int32(r[i - 31] + r[i - 3]))
        yield int32((r[i] & 0xffffffff) >> 1)
CORRECT = 'o\n\x03\x81\x04\x81P\xd7\x0co\x04o\n\x04\x0c\n\xf5o\x04\r\xd7\x81\n\x04\xd7$\n\x04\xc1o\x0c\n\x04!\n\x81'

def encrypt1(string):
   key = '}\xc4Iu\x8exh\xc6Ucq\x97`\xc3\xf9\x91DS4\xa4N\x055\x9b\xe3\xf2\xc5\xe7\t\xb5\xcf\xa9O\x9c\x10\x00\x08d\xc9\xd4\xb2\xe6\xa8\xbe\xdf|\xd8(\xad\xd7b\n@\xdc<A\xca. :C\x84\xcb\x06\xc0\xb9\x07\xc2-\xbc\x0eRpsf\xbf\xba\x1cwnJ\x99*6\xef\x90]\x0b\xd3\x13G\xa3\xe1\xe0K\x04\x15m\xf5\xfd\r&\x98v\x0c0\xb7$\xc1\x03\\\x9a\x89\xf4!\x81oZWP[#\xe9\x18\xccM\xde\xf8k,j\xa5\x8f+B\xfe\xbb\x93\x9f\xd2\xe5\xfb\xb1\xd5e\xdd\x83\xf7;\xcd\x1al{\xb0\xaa\xb3)\xd9Q\x1f>g\x96\x8c\xe8\xd1\xec\xce\xf6\x87\x1d\x8d\"E\xff\xa1t\x85\xbd3\xee\xb8\x11H\x88\x16\xf18T\x95\xed\x80\xf07\x199F\xe2\xa0\xdb\x94%2\x02\xaf\xa7\xc8\xe4\x86\x17\xb4?L\'=\x12\xa2a\xab\xb6i\x82\x9eX\x14V/_\xf3Y\x9d\xc7\x8a\x8b\xd0z\xa6\xeb\xda\xea\x1e\x7fy~^\xfc\x0f\xfa\x92\xac1r\xd6\xae\x1b\x01'
   return key[ord(k)]

def checker():
     return 0


def encrypt2(bytes):
    seed = bytes[0]
    for i in range(len(bytes)):
        if (checker(seed)):
                bytes[i]. bytes[-1] = bytes[-1], bytes[1]
    return bytes

def main():
    #print(encrypt1(sys.argv[1]))
    counter = 0
    for i in glibc_prng(int("6f", 16)):
        print(i , (i & 1))
        counter += 1
        if counter > 36:
            break
    for i in CORRECT:
        print(encrypt

if __name__ == "__main__":
    main()
