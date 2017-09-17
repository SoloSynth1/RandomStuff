
L32o = int(input("Please enter the Leftmost output 32 bit in hex.\n"), 16)
R32o = int(input("Please enter the Rightmost output 32 bit in hex.\n"), 16)

funs1 = L32o
funs2 = L32o ^ R32o

L32 = int("ffffffff", 16) ^ funs1
print(hex(L32))
R32 = int("00000000", 16) ^ L32 ^ funs2


print("The funs1 and funs2 are %s, and %s.", hex(funs1), hex(funs2))
print("If the input is 1^32 0^32, the output would be: %s, %s.", hex(L32), hex(R32))

