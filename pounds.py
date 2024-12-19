# In the United Kingdom, the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

one = 1
two = 2
five = 5
ten = 10
twenty = 20
fifty = 50
hundred = 100
twohundred = 200

makesTwoPounds = []

toAppend = []
makesTwoPounds.append([twohundred])
makesTwoPounds.append([hundred,hundred])
for g in range(2):
    for f in range(5):
        for e in range(11):
            for d in range(21):
                for c in range(41):
                    for b in range(101):

                        toAppend.clear()

                        if sum(toAppend) < 200:
                            for t in range(g):
                                toAppend.append(hundred)

                        if sum(toAppend) < 200:
                            for u in range(f):
                                toAppend.append(fifty)

                        if sum(toAppend) < 200:
                            for v in range(e):
                                toAppend.append(twenty)

                        if sum(toAppend) < 200:
                            for w in range(d):
                                toAppend.append(ten)

                        if sum(toAppend) < 200:
                            for x in range(c):
                                toAppend.append(five)

                        if sum(toAppend) < 200:
                            for y in range(b):
                                toAppend.append(two)

                        while sum(toAppend) < 200:
                            toAppend.append(one)

                        if sum(toAppend) == 200:
                            # print(len(toAppend))
                            # if len(toAppend) == 1:
                            #     print(toAppend)
                            if toAppend not in makesTwoPounds:
                                makesTwoPounds.append([])
                                makesTwoPounds[-1].extend(toAppend)
                                print(len(makesTwoPounds))

print(len(makesTwoPounds))
