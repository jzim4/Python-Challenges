# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

toTestList = []
global sum
works = []
for i in range(2,1000000):
    toTestString = str(i)
    toTestList = []
    for y in toTestString:
        toTestList.append(y)
    sum = 0
    for x in range(len(toTestString)):
        sum += pow(int(toTestList[x]),5)
            #print(sum)
            #print(sum)
    if sum == i:
        works.append(i)
            #print('added')


print(works)
endSum = 0
for a in works:
    endSum += a

print('This is the solution: ',endSum)
