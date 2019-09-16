import math
import helper as h

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def prob30():
    nums = []
    #max possible range will be (9^5)*6 = 354294, since you still can have 6 digits with
    #the sum of the powers of 5
    for i in range(10, 354295):
        string = str(i)
        total = 0
        for digit in string:
            d = int(digit)
            total += d**5
        if total == i:
            nums.append(i)
    
    return sum(nums)

#How many distinct items exist in the union of all a^b and b^a, where 1 < a < 101 and
#1 < b < 101
def prob29():
    all_nums = set()
    for a in range(2, 101):
        for b in range(2, 101):
            all_nums.add(a**b)
            all_nums.add(b**a)
    return(len(all_nums))

#Starting with 1 and forming  a 1001 by 1001 spiral that grows from the center in a 
#clockwise direction, we want to add the values of the diagonals
def prob28():
    top_right, top_left, bottom_left, bottom_right = 0, 0, 0, 0
    for i in range(3, 1002, 2):
        square = i**2
        top_right += square
        top_left += square - (i-1)
        bottom_left += square - 2*(i-1)
        bottom_right += square - 3*(i-1)
    return(1 + top_right + top_left + bottom_left + bottom_right)

#Find product of coefficients, a and b, for the quadratic expression of the
#form n^2+an+b which give the max number of primes for consecutive values of n,
#starting with n = 0
def prob27():
    maxCount = 0
    finalA = 0
    finalB = 0
    answer = 0
    for a in range(-1000, 1000):
        for b in range(-1000, 1001):
            n = 0
            count = 0
            y = n**2 + a*n + b
            if y < 0:
                continue
            while(True):
                y = n**2 + a*n + b
                if y < 0:
                    break
                if h.isPrime(y):
                    n += 1
                    count += 1
                    continue
                else:
                    break
            if count > maxCount:
                maxCount = count
                finalA = a
                finalB = b
                answer = a*b
    print(finalA, finalB, answer, maxCount)
    return(answer)
                
    

#In decimal form, what is the number 1/n that has the largest recurring cycle,
#where n is a positive integer smaller than 1000
def prob26():
    maxCycle = 0
    answer = 0
    for n in range(2, 1000):
        #check if n can be represented in the form 2^a*5^b
        n_prime = n
        while (n_prime % 2 == 0):
            n_prime = n_prime//2
        while (n_prime % 5 == 0):
            n_prime = n_prime//5
        if n_prime == 1:
            continue
       
        k = 1
        while(int(10**k-1) % n_prime != 0):
            k += 1
        if k > maxCycle:
            maxCycle = k
            answer = n
    print(answer, maxCycle)
    return(answer)

#What is the index of the first term in the Fibonacci sequence to contain
#1000 digits?
def prob25():
    a = 1
    b = 1
    index = 2
    while True:
        a += b
        index += 1
        if len(str(a)) == 1000:
            return index
        b += a
        index += 1
        if len(str(b)) == 1000:
            return index

#What is the millionth lexicographic permutation of the digits
#0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
def prob24():
    #find which range element 1000000 occurs, since symbols are ordered
    symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    size = math.factorial(10) #total number of permutations
    key = 999999 #millionth position if start count from 0
    ct = 0
    answer = ''
    for i in range(10):
        size = size/(10-i) #reduce size
        pos = int(key//size) #verify position of symbol where key is found
        key = key - (size*pos) #change value of key by subtracting
                               #this normalizes the range where min = 0 and
                               #max = size*pos - 1
        answer += symbols[pos]
        del symbols[pos]
    print(answer)
    
#Find the sum of all the positive integers which cannot be written as the
#sum of two abundant numbers.
def prob23():
    abundant = []
    for n in range(1, 28124):
        if sum(h.properDivisors(n)) > n:
            abundant.append(n)
    notAbundantSum = 0
    for k in range(1, 28124):
        if h.findSum(abundant, k) == False:
            notAbundantSum += k
    return notSumAbundantSum

#Reading a text file provided, sort it in alphabetical order.
#Then working out the alphabetical value for each name, multiply this value by
#its alphabetical position in the list to obtain a name score.
#Find the sum of all name scores.
#ANSWER: 871198282
def prob22():
    a = h.readstrlist("22_Names.txt", ",")
    a = [i.replace('"', '') for i in a]
    a = sorted(a)
    
    totalScore = 0
    for i in range(0, len(a)):
        nameScore = 0
        for char in a[i]:
            val = ord(char)-64
            nameScore += val
        nameScore *= (i+1)
        totalScore += nameScore
    return totalScore

#find the sum of all amicable numbers under 10000
#amicable numbers are a pair of numbers a and b, such that the sum of all
#divisors of a equals b and vice versa
#ANSWER: 31626
def prob21():
    amicables = []
    for a in range(2, 10001):
        b = sum(h.divisors(a))-a
        if (b == a):
            continue
        if sum(h.divisors(b))-b == a and a < 10000 and b < 10000:
            if b not in amicables: #avoid double counting
                amicables.append(a)
                amicables.append(b)
    return sum(amicables)
        

#find the sum of digits in 100!
#ANSWER: 648
def prob20():
    total = 0
    n = math.factorial(100)
    n = str(n)
    for d in n:
        d = int(d)
        total += d
    return total


#1 Jan 1900 was a Monday.
#A leap year occurs on any year evenly divisible by 4, but not on a century
#unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century
#(1 Jan 1901 to 31 Dec 2000)?
#ANSWER: 171
def prob19():
    answer = 0
    #use 0,1,...,6 to indicate days of the week (0 == Monday)
    day = 6 #6 Jan 1901 was a Sunday
    switch_day = 1 #the day in which the year will be switched
    firsts = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    year = 1901
    while year != 2001:
        if h.isLeap(year) == True:
            switch_day += 366
            while day < switch_day:
                if day in firsts:
                    answer += 1
                day += 7
            firsts[0] += 366
            firsts[1] += 366
            for i in range(2, 12):
                firsts[i] += 365
        else:
            switch_day += 365
            while day < switch_day:
                if day in firsts:
                    answer += 1
                day += 7
            for i in range(0, 12):
                firsts[i] += 365
            if h.isLeap(year+1) == True:
                for i in range(2, 12):
                    firsts[i] += 1
        print(firsts)
                
        
        year += 1
    print(answer)
    return answer


#By starting at the top of the triangle below and moving to adjacent numbers on
#the row below, the maximum total from top to bottom is 23.
#
#          3
#         7 4
#        2 4 6
#       8 5 9 3
#
#That is, 3 + 7 + 4 + 9 = 23.
#
#Find the maximum total from top to bottom of the triangle in file "maxpath18.txt"
def prob18():
    tri = h.read2dlist("18_MaxPath.txt")
    for i in range (len(tri)-2, -1, -1):
        for j in range(0, len(tri[i])):
            if tri[i+1][j] > tri[i+1][j+1]:
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]
    return tri[0][0]

        
#If all the numbers from 1 to 1000 were written out in words, how many letters would
#be used?
#ANSWER: 21124
def prob17():
    answer = 0
    for n in range(1, 1000):
        s = h.buildWord(n)
        answer += len(s)
    answer += len('onethousand')
    return answer

#find the sum of the digits of 2^1000
#ANSWER: 1366
def prob16():
    total = 0
    n = 2**1000
    n = str(n)
    for d in n:
        d = int(d)
        total += d
    return total
        

#How many routes are there through a 20x20 grid if you can go only down and right?
#ANSWER: 137846528820
def prob15():
    #You must go down 20 times and right 20 times
    #Usually if you could go 40 times in either direction, that would be 2^40 routes
    #Because of the restriction, we must consider that there are only 40 choose 20
    #paths for going down (and subsequently right)
    n = 40
    k = 20
    numPaths = math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
    return numPaths

#find the number that gives the longest Collatz sequence under 1,000,000
#Collatz sequence is defined as: n -> n/2  (if even)
#                                n -> 3n+1 (if odd)
#The sequence always seems to end at 1. It has not been proved yet though.
#ANSWER: 837799 (with size 100)
def prob14():
    #simple class with two variables:
    #n identifies the leading number in the sequence
    #size identifies the total size of sequence n
    class collatzNum:
        def __init__(self, n, size):
            self.n = n
            self.size = size

    #create an empty list with 1,000,000 entries
    allValues = [collatzNum(0, 0)]*1000000
    allValues[0] = collatzNum(0, 0) #n=0, does not produce a Collatz sequence
    allValues[1] = collatzNum(1, 1) #n=1, produces a Collatz sequence of size 1
    greater = [] #all numbers greater than n that were found in n's sequence
                 #are placed here, since we will know their seqSize by proxy
    maxSize = 1
    maxValue = 1

    for n in range(2, 1000000):
        if allValues[n].size != 0: #skip it if it has already been classified
            continue

        original = n
        seqSize = 1
        while (n!=1):
            if (n%2 == 1):
                n = 3*n + 1
                seqSize += 1
            else:
                n = n//2
                seqSize += 1
            #after appending n to seq, increment size of items in larger by 1 
            for item in greater:
                item.size += 1
            if (n < original):
                seqSize += allValues[n].size - 1
                for item in greater:
                    item.size += allValues[n].size
                break
            elif (n > original and n < 1000000 and allValues[n].size != 0):
                greater.append(collatzNum(n, 1))
        #add the original value of n to allValues        
        allValues[original] = collatzNum(original, seqSize)

        #fill allValues with values from greater
        for item in greater:
            if item.n < 1000000 and allValues[item.n].size == 0:
                allValues[item.n] = collatzNum(item.n, item.size)

                
        #check if there is a new maxSize
        if seqSize > maxSize:
            maxSize = seqSize
            maxValue = original
        greater.clear()

    return maxValue
            
    
#Work out the first ten digits of the sum of the one-hundred 50-digit numbers
#(read from text file)
#ANSWER: 5537376230
def prob13():
    answer = ""
    a = h.readintlist("13_Numbers.txt")
    sumA = str(sum(a))
    for i in range(0, 10):
        answer += sumA[i]
    return answer
    

#find the first triangular number with over 500 divisors
#ANSWER: 76576500
def prob12():
    div = [] #divisors in triangular number
    triangularNums = []
    triangle = 0
    increment = 1
    while (len(div) < 500):
        triangle += increment
        triangularNums.append(triangle)
        div = h.divisors(triangle)
        increment += 1
    return triangle


#find the greatest product of four adjacent numbers in g, a 20x20 grid (shown
#below) – adjacency can be vertical, horizontal or diagonal
#ANSWER: 70600674
def prob11():
    a = h.read2dlist("11_Grid.txt")
    maxProd, totalHrzt, totalVert, totalDiagTL, totalDiagTR = 0, 0, 0, 0, 0
    for i in range(0, 20):
        for j in range(0, 20):
            if (i < 16):
                totalHrzt = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j]
            if (j < 16):
                totalVert = a[j][i] * a[j+1][i] * a[j+2][i] * a[j+3][i]
            if (i < 16 and j < 16):
                totalDiagTL = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3]
            if (i > 3 and j < 16):
                totalDiagTR = a[i][j] * a[i-1][j+1] * a[i-2][j+2] * a[i-3][j+3]
            maxProd = max([maxProd, totalHrzt, totalVert, totalDiagTL, totalDiagTR])
    return maxProd


#find the sum of all the primes below 2,000,000
#ANSWER: 142913828922
def prob10():
    primeSum = 0
    primeList = h.primeSieve(2000000)
    for num in primeList:
        primeSum += num
    return primeSum


#Find set of pythagorean triplet integers a, b, c, such that a+b+c=1000
#Return product of a, b, c
#ANSWER: (a, b, c) = (200, 375, 425) –– a*b*c = 31875000
def prob9():
    #create list with all squares
    squares = []
    for i in range(1, 999):
        squares.append(i**2)

    triplets = []
    #find potential pythagorean triplets from squares list
    for j in range(0, len(squares)):
        for k in range(j, len(squares)):
            val = squares[j] + squares[k]
            found = h.binarySearch(squares, val) #see if c^2 exists
            if found == True:
                triplets.append([j+1, k+1, int(math.sqrt(squares[j]+squares[k]))])
                a = j+1
                b = k+1
                c = int(math.sqrt(squares[j]+squares[k]))
                abcSum = a+b+c
                if abcSum == 1000:
                    print(a, b, c)
                    return a*b*c
    return 0

            
#what is the largest product of 13 adjacent digits of n (shown below in code)
#ANSWER: 23514624000
def prob8():
    n = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    n = str(n)
    maximum = 0
    for i in range(0, 987):
        new_s = n[i:i+13]
        prod = 1
        for ch in new_s:
            prod *= int(ch)
        if prod > maximum:
            maximum = prod
    return maximum


#what is the 10001st prime number?
def prob7():
    primeNumbers = [2]
    i = 1
    while len(primeNumbers) != 10001:
        i += 2
        for j in primeNumbers:
            #if j divides i, then i is not a prime
            if (i % j == 0):
                break
            elif(primeNumbers[len(primeNumbers)-1] == j):
                primeNumbers.append(i)
    return primeNumbers[10000]
    

#Sum Square Difference
#Find the difference of the sum of the squares and the square of the sum from
#0 to 100
#ANSWER: 25164150
def prob6():
    minimum = 1
    maximum = 100
    sum_euler = (minimum+maximum)*((maximum-minimum+1)/2)
    square_of_sum = sum_euler**2
    
    sum_of_squares = 0
    for i in range(1, 101):
        sum_of_squares += i**2
    
    return square_of_sum - sum_of_squares


#find smallest number that is evenly divisible by all numbers between 1-20
#ANSWER: 232792560
def prob5():
    decomp = []
    primes = h.primeSieve(20) #build list of all primes from 1-20
    result = 1
    #build list of primes and decomposed-nonprimes
    for i in range (2, 21):
        decomp.append(h.decompose(i))
            
    #build multiplier table
    multiplier = []
    for p in primes:
        freq = 1
        mult = p
        for d in decomp:
            if p in d:
                ct = d.count(p)
                if ct > freq:
                    freq = ct
                    mult = p**freq
        multiplier.append(mult)
                
    for k in range(0, len(multiplier)):
        result *= multiplier[k]
    return result


#find largest product of two 3-digit numbers that is a palindrome
#ANSWER: 906609
def prob4():
    maxprod = 0
    for i in range(0, 899):
        a = 999 - i
        for j in range(0, 899):
            b = 999 - j
            prod = a*b
            str_prod = str(prod)
            if (str_prod == str_prod[::-1] and prod > maxprod):
                maxprod = prod
    return maxprod


#find largest prime factor of 600851475143
#idea is that you keep dividing n by small primes, until a large prime is left
#ANSWER: 6857
def prob3():
    upperbd = 1000
    primes = h.primeSieve(upperbd)
    maxpos = len(primes)-1
    pos = 1 #primes[1] is 2
    n = 600851475143
    
    while(h.isPrime(n) == False):
        if (n % primes[pos] == 0):
            n = n/primes[pos]
            continue
        else:
            if (pos == maxpos):
                upperbd = upperbd * 10
                primes = h.primeSieve(upperbd)
                maxpos = len(primes)-1
                pos += 1
            else:
                pos += 1
                
    return n


#finds fibonacci numbers up to 4,000,000 and sums even ones
#ANSWER: 4613732
def prob2():
    total = 0
    _fourmil = 4000000
    a = 1
    b = 2
    while (True):
        if (a > _fourmil or b > _fourmil):
            break
        if (a % 2 == 0):
            total += a
        if (b % 2 == 0):
            total += b
        a += b
        b += a
    return total


#sums multiples of 3 and 5 in range [0, 1000]
#ANSWER: 233168
def prob1():
    total = 0
    for i in range(0, 1000):
        if (i % 3 == 0):
            total += i
        elif (i % 5 == 0):
            total += i
    return total
