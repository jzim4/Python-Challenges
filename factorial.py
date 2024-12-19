# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.



def getFactorial(num):
    output = 1
    for i in range(1,num+1):
        output = output*i
    return output

factorials = {0:1, 1:getFactorial(1), 2:getFactorial(2), 3:getFactorial(3), 4:getFactorial(4), 5:getFactorial(5), 6:getFactorial(6), 7:getFactorial(7), 8:getFactorial(8), 9:getFactorial(9)}

# print(factorials[4])
answer = 0
for x in range(9, 1000000):
    stringX = str(x)
    listX = []
    for digit in stringX:
        listX.append(digit)
    sum = 0
    for digit in listX:
        sum += factorials[int(digit)]
    if sum == x:
        answer += sum

print('the sum is ' + str(answer))
