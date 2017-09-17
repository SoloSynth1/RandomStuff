import random

mystr = [chr(random.randint(33,126)) for _ in range(1000)]

print("".join(mystr))

