#Prog01
def max(x, y):
    return x if x > y else y

#Prog02
def isEqual(x, y):
    if x == y: print("Equal")

#Prog03
def sum(x, y):
    return x + y

#Prog04
def pro(x, y):
    return x * y

#Prog05
def quo(x, y):
    return x / y

#Prog06
def exp(x, y):
    return x ** y

#Prog07
def sums(arr):
    total = 0
    for num in arr:
        total += num
    return total

#Prog08
def countOdd(arr):
    oddCount = 0
    for num in arr:
        if num & 1 == 1:
            oddCount += 1
    return oddCount

#Prog09
def printEven(start = 0, stop = 100):
    for num in range(start, stop // 2 + 1):
        print(num * 2)

#Prog10
def nonMultiples(start = 0, stop = 100, val = 10):
    for num in range(start, stop + 1):
        if not(num % val == 0):
            print(num)

