# The uncommon word “beefily” has an unusual characteristic.
# What is the longest word that shares this unusual property?


dictionary = open("d.txt","r")
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = []

for word in dictionary:
    list = []
    for letter in word:
        if letter in abc:
            list.append(abc.index(letter))
    listSorted = []
    for i in list:
        listSorted.append(i)
    listSorted.sort()
    if listSorted == list:
        print(listSorted)
        print(list)
        answer.append([word, len(word)])
        print(word)


for word in answer:
    word.reverse()

answer.sort()
print('The longest word with letters in alphabetical order (other than beefily) is: ' + answer[-1][1])
dictionary.close()
