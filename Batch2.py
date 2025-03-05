#Prog01
def min(x, y):
    return x if x < y else y

#Prog02
def isEqual(x, y):
    if x != y: print("Not Equal")

#Prog03
def dif(x, y):
    return x - y

#Prog04
def intQuo(x, y):
    return x // y

#Prog05
def mod(x, y):
    return x % y

#Prog06
def difs(arr):
    val = 2 * arr[0]
    for num in arr:
        val -= num
    return val

#Prog07
def countEven(arr):
    evenCount = 0
    for num in arr:
        if num & 1 == 0:
            evenCount += 1
    return evenCount

#Prog08
def printOdd(start = 0, stop = 100):
    count = start
    while count <= stop:
        if count & 1 == 1:
            print(count)
        count += 1

#Prog09
def nonMultiples(start = 0, stop = 100, val = 5):
    for num in range(start, stop + 1):
        if not(num % val == 0):
            print(num)

#Prog10
def printRange(start, stop):
    for num in range(start, stop + 1):
        print(num)
