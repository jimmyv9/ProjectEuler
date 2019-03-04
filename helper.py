import math

def isLeap(year):
    if year % 4 == 0 and (not(year % 100 == 0) or year % 400 == 0):
        return True
    return False

def buildWord(n):
    word = ''
    if n < 0 or n > 999:
        print("Can only output positive numbers less than 1000")
        return
    
    units = ['', 'one','two','three','four','five','six','seven','eight','nine']
    tens = ['twenty','thirty','forty','fifty','sixty',
            'seventy','eighty','ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
             'sixteen', 'seventeen', 'eighteen', 'nineteen']

    hundredsDigit = n//100
    tensDigit = (n % 100)//10
    unitDigit = n % 10

    if hundredsDigit != 0:
        word += units[hundredsDigit]
        word += 'hundred'
        if tensDigit != 0 or unitDigit != 0:
            word += 'and'
    
    if tensDigit == 1:
        word += teens[unitDigit]
    elif tensDigit == 0:
        word += units[unitDigit]
    else:
        word += tens[tensDigit - 2]
        word += units[unitDigit]

    return word    

#finds whether there are 2 numbers in nlist that sum to n
#returns boolean value
def findSum(nlist, n):
    for i in nlist:
        if n//2 < i:
            return False
        if binarySearch(nlist, n-i) == True:
            return True
    return False

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

#Erasthotenes Sieve to find all prime numbers up until n
def primeSieve(n):
    primes = []
    #create boolean list to indicate whether a number is prime or not
    #initially set all numbers equal to true
    a = [True] * (n+1)
    a[0] = False #0 is not prime
    a[1] = False #1 is not prime
    limit = int(math.sqrt(n))
    for i in range(2, limit+1):
        if a[i] == True:
            j = i**2
            while (j <= n):
                a[j] = False
                j += i
    #append indices that are 'True', given those are prime
    for k in range(2, n+1):
        if a[k] == True:
            primes.append(k)

    return primes

#is n prime?
def isPrime(n):
    _isPrime = True
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return _isPrime

#decomposes a composite number into its primes
#returns a list with all the composite numbers
def decompose(n):
    result = []
    #check if n is prime
    if (isPrime(n) == True):
        result.append(n)
        return result
    
    #create prime list with possible divisors of n
    primes = primeSieve(int(n//2)+1)
    #decompose non-prime numbers
    for p in primes:
        while(n % p == 0):
            n = n // p
            result.append(p)
            if n == 1:
                break
    return result

def properDivisors(n):
    divisors = [1]
    sqrt = int(math.sqrt(n))
    #iterate i from 1 to ~sqrt
    for i in range(2, sqrt+1):
        if (n % i == 0):
            divisors.append(i)
            divisors.append(n//i)
    #check if it is a perfect square and if so, pop the second square
    if sqrt**2 == n and n!=1:
        divisors.pop()
    return divisors

#find all divisors of n
def divisors(n):
    divisors = []
    sqrt = int(math.sqrt(n))
    #iterate i from 1 to ~sqrt
    for i in range(1, sqrt+1):
        if (n % i == 0):
            divisors.append(i)
            divisors.append(n//i)
    #check if it is a perfect square and if so, pop the second square
    if sqrt**2 == n:
        divisors.pop()
    return divisors

def read2dlist(filename):
    file = open(filename, "r")
    grid = []
    for line in file:
        line = line.split()
        a = []
        for item in line:
            a.append(int(item))
        grid.append(a)
    return grid

def readintlist(filename):
    file = open(filename, "r")
    _list = []
    for line in file:
        line = int(line)
        _list.append(line)
    return _list

def readstrlist(filename, delimiter):
    file = open(filename, "r")
    _list = []
    for line in file:
        line = line.split(delimiter)
        for word in line:
            _list.append(word)
    return _list
        
        
