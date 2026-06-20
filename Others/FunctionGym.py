def add(a, b):
    # return sum
    return a + b

def maxOfTwo(a, b):
    # return bigger number
    if a > b:
        return a
    else:
        return b

def isEven(n):
    # return True/False
    if n % 2 == 0:
        return True
    else:
        return False

def countVowels(s):
    # return number of vowels
    s = s.lower()
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

def reverseString(s):
    # return reversed string
    return s[::-1]

def isPrime(n):
    # return True/False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sumOfFactors(n):
    # return sum of all factors of a number
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor.append(i)
    factor.sort()
    return sum(factor)

def numOfFactor(n):
    # count how many factors n has
    factor = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor.append(i)
    factor.sort()
    return factor

def removeNegatives(lst):
    # return new list without negatives
    new_list = []
    for num in lst:
        new_list.append(abs(num))
    return new_list
