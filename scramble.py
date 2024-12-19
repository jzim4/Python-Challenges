# Rearrange the letters in the following to form 2 normal, average words.
# Hints:  One of them is, like, a thing.  The other is not particularly complicated.


words = ["dgoaarftwtrshri", "itaacamathlwchl"]

fullDictionary = open("d.txt","r")
dictionary = []
for word in fullDictionary:
    if len(word) == 16:
        dictionary.append(word)

# print(dictionary)


def addLetter(letter):
    solution.append(letter)
    listCopy.remove(letter)

list = []
for letter in words[0]:
    list.append(letter)
for a in range(len(list)):
    listCopy = list
    solution = []
    print(listCopy)
    addLetter(a)
    for b in listCopy:
        addLetter(b)
        for c in listCopy:
            addLetter(c)
            for d in listCopy:
                addLetter(d)
                for e in listCopy:
                    addLetter(e)
                    for f in listCopy:
                        addLetter(f)
                        for g in listCopy:
                            addLetter(g)
                            for h in listCopy:
                                addLetter(h)
                                for i in listCopy:
                                    addLetter(i)
                                    for j in listCopy:
                                        addLetter(j)
                                        for k in listCopy:
                                            addLetter(k)
                                            for l in listCopy:
                                                addLetter(l)
                                                for m in listCopy:
                                                    addLetter(m)
                                                    for n in listCopy:
                                                        addLetter(n)
                                                        for m in listCopy:
                                                            addLetter(m)
                                                            if ''.join(solution) in dictionary:
                                                                print(word)



dictionary.close()
