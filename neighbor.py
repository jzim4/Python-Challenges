#We will define "Neighborly numbers" to be numbers whose digits each differ by exactly 1 from the digits on
#either side.  First and last digits only have 1 neighbor.  So, for example, 123, 789012, and 67876 are
#neighborly, but 12322 and 78907 are not.  We will consider that 9 and 0 are neighbors, counting 0 as 10,
#and 0 is also neighbors with 1.
#Find the sum of all primes between 5,000,000 and 10,000,000 that are also neighborly.


import math
import time

start = time.time()
answer = []

def isPrime(number):
    factors = []
    for factor in range(1,(math.ceil(math.sqrt(number+1)))):
        if number % factor == 0:
            factors.append(factor)
            if factor != number:
                factors.append(number/factor)
    if len(factors) == 2:
        answer.append(number)

for a in range(5,10,2):
    for b in range(-1,2,2):
        for c in range(-1,2,2):
            for d in range(-1,2,2):
                for e in range(-1,2,2):
                    for f in range(-1,2,2):
                        for g in range(-1,2,2):
                            toTest = str(a) + str((a+b)%10) + str((a+b+c)%10) + str((a+b+c+d)%10) + str((a+b+c+d+e)%10) + str((a+b+c+d+e+f)%10) + str((a+b+c+d+e+f+g)%10)
                            isPrime(int(toTest))
print('answer:',sum(answer))

end = time.time()

print('time elapsed:',end-start)
