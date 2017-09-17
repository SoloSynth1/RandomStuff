import time

def Isprimenumber(number):
    if number ==1:
        return False
    div = number - 1
    while div >= 2:
        if number%div == 0:
            return False
        else:
            div -= 1
    return True

printcount =0
starttime = time.time()
for x in range(1,30000):
    if Isprimenumber(x) == True:
        printcount += 1
        print ("Prime number No.%d: %d" % (printcount, x) )

endtime = time.time()

print ("%d prime numbers found. %.3f seconds used for the iteration." % (printcount, (endtime - starttime)))
