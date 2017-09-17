
input1 = input('First Hex String\n')
input2 = input('Second Hex String\n')
output = [int(input1[x:x+2], 16) ^ int(input2[x:x+2], 16) for x in range(0, min(len(input1), len(input2)), 2)]

print("".join(hex(x) for x in output))
print("".join(chr(x) for x in output))
#print(''.join(['%02x' % i for i in output]))