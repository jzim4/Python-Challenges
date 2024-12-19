# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime,
# contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math
def isPrime(number):
    factors = []
    for factor in range(1,(math.ceil(math.sqrt(number+1)))):
        if number % factor == 0:
            factors.append(factor)
            if factor != number:
                factors.append(number/factor)
    if len(factors) == 2:
        return True
    else:
        return False


primes = []
for i in range(2,50000):
    if isPrime(i):
        primes.append(i)
# print(primes)
consecutivePrime=[]

for x in range(len(primes)):
    current=0
    for y in range(len(primes)-x):
        current+=primes[x+y]
        if current < 1000000:
            if isPrime(current):
                consecutivePrime.append([y,x,current])
                # print([y,x,current])
# print(max(consecutivePrime))
print('The prime number ' + str(max(consecutivePrime)[2]) + ' can be written as ' + str(max(consecutivePrime)[0]+1) + ' consecutive primes.')
