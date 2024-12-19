# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
#  increases by 3330, is unusual in two ways: (i) each of the three terms
#  are prime, and, (ii) each of the 4-digit numbers is a permutation of the others.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing
# sequence.
# What is the sum of the 3 numbers in this sequence?
import math
def isPrime(number):
    factors = []
    for factor in range(1,(math.ceil(math.sqrt(number+1)))):
        if number % factor == 0:
            factors.append(factor)
            if factor != number:
                factors.append(number/factor)
        #    print(factors)
    if len(factors) == 2:
        return True

    else:
        return False

answer = []
for add in range(1,3334):
    for i in range(1000,10000):
        iString = str(i)
        iList = []
        for a in iString:
            iList.append(a)

        testOne = i + add
        testOneString = str(testOne)
        testOneList = []
        for b in testOneString:
            testOneList.append(b)

        testTwo = i + (add * 2)
        testTwoString = str(testTwo)
        testTwoList = []
        for o in testTwoString:
            testTwoList.append(o)
        iList.sort()
        testOneList.sort()
        testTwoList.sort()
        if iList == testOneList and testOneList == testTwoList:
            if isPrime(i) and isPrime(testOne) and isPrime(testTwo):
                answer.append([i,testOne,testTwo])
                print([i,testOne,testTwo])
                for each in answer:
                    if each != [1487, 4817, 8147]:
                        print('the sum of the series is ', str(sum(each)))
