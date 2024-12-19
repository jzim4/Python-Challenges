#We shall say that an n-digit number is pandigital if it makes use of
#all the digits 1 to n exactly once; for example, the 5-digit number,
#15234, is 1 through 5 pandigital.
#The product 7254 is unusual, as the identity, 39 × 186 = 7254,
#containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#Find the sum of all products whose multiplicand/multiplier/product identity
#can be written as a 1 through 9 pandigital.



answer = []
productList = []
multiplicandList = []
multiplierList = []


for multiplicand in range(1,10000):
    multiplicandString = str(multiplicand)
    multiplicandList.clear()
    for a in multiplicandString:
        multiplicandList.append(a)
    for multiplier in range(1,pow(10,(5-len(multiplicandList)))):
        multiplierString = str(multiplier)
        multiplierList.clear()
        for b in multiplierString:
            multiplierList.append(b)

        product = multiplicand*multiplier
        productString = str(product)
        productList.clear()
        for c in productString:
            productList.append(c)

        isAnswer = productList + multiplicandList + multiplierList
        if len(isAnswer) == 9:
            #print(isAnswer,'\n')
            isAnswer.sort()
            if isAnswer == ['1','2','3','4','5','6','7','8','9']:

                answer.append([product,multiplicand,multiplier])
                print(answer)

answerSet = set()
for x in answer:
    answerSet.add(x[0])
print(answerSet)
print('The sum of the products is: ', sum(answerSet))
