# Take a number.  Square each digit and add them together.
# Keep doing this until you get to a single digit.  If that digit is 1,
# the number is singular.
# Challenge: Find the sum of all singular numbers between 10001 and 20000

answer = []
for i in range (10001,20001):
    print(i)
    numberString = str(i)
    numberList = []
    for digit in numberString:
        numberList.append(digit)
    while len(numberList) != 1:
        for index in range(len(numberList)):
            numberList[index] = pow(int(numberList[index]),2)
        print(numberList)
        numberString = str(sum(numberList))
        print(numberString)
        numberList = []
        for digit in numberString:
            numberList.append(digit)
    if numberString == '1':
        answer.append(i)
        print(i)
    print('\n')

print('The sum is ' + str(sum(answer)))
