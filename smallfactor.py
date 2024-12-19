# We define small factor numbers as numbers whose only prime factors are 2, 3,
# and 5.  For example, 12 (2x2x3), 50 (2x5x5) and 90 (2x3x3x5) are all small
# factor numbers, while 28 (2x2x7) and 22 (2x11) are not.
# What is the sum of all small factor numbers between 1,000,000 and 1,999,999?

import math

answers = []
maybe = 0

for two in range(0,21):
    if two == 0:
        twodivisor = 1
    else:
        twodivisor = two
    for three in range(0,14):
        if three == 0:
            threedivisor = 1
        else:
            threedivisor = three
        for five in range(0,10):
            maybe = pow(2,two)*pow(3,three)*pow(5,five)
            if maybe >= 1000000 and maybe <= 1999999 and maybe not in answers:
                print(two, ' twos')
                print(three, ' threes')
                print(five, ' fives')
                print(maybe, "\n")
                answers.append(maybe)

print('the sum is ' + str(sum(answers)))
