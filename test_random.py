import random

def getrandom():
    for i in range(10000):
        yield random.randint(0, 99)

count = [0 for _ in range(100)]
for number in getrandom():
    count[number] += 1

print(count)
print("max = %d, min = %d, diff = %d"%(max(count), min(count), (max(count) - min(count))))