import sys

# MSGS = ( ---  11 secret messages  --- )

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        # chr(num) returns the ascii character that corresponds to the num
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

spO = ord(' ')
print(spO)
aOrder = ord('a')
print("aOrder: {0:d} {1:b} {2:x}".format(aOrder,aOrder,aOrder))
aspX = spO ^ aOrder
print("aspX: {0:d} {1:b} {2:x}".format(aspX,aspX,aspX))
print(chr(97))

