# Tui Popenoe
# Binary Utilities
import struct
import sys

def floatToBinary(value):
    value = float(value)
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return bin(val)

def binaryToFloat(value):
    hx = hex(int(str(value), 2))
    return struct.unpack('d', struct.pack('q', int(hx, 16)))[0]

def main(arg1, arg2):
    if arg1 == '-fb':
        value = floatToBinary(arg2)
        print(value)
    if arg2 == '-bf':
        value = binaryToFloat(arg2)
        print(value)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])