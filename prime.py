# The number 3797 has an interesting property. Being prime itself, it is possible
#to continuously remove digits from left to right, and remain prime at each stage:
#3797, 797, 97, and 7. Similarly, we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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
possible = 11
while len(answer) < 11:
    possibleString = str(possible)
    couldBePrime = True
    toTestFront = possibleString
    toTestBack = possibleString
    #print(isPrime(possible))
    #print(possible)
    if isPrime(possible) == True:
        for i in range(len(possibleString)-1):
            toTestFront = toTestFront[1:]
            toTestBack = toTestBack[:-1]
            if isPrime(int(toTestFront)) == False:
                couldBePrime = False
            if isPrime(int(toTestBack)) == False:
                couldBePrime = False

        if couldBePrime == True:
            print(possible)
            answer.append(possible)



    possible += 2

print('answer:',answer)
print('sum of primes',sum(answer))

#23,37,53,73,313,317,373,797,3137,3797
