# Using the list of words in d.txt, found here, find all words that contain exactly 4 C's.  Change all C's to X's.
# Return the file of all changed words.  Name the file "fourx.txt".  Make sure the list of words is in the form of one word per line.  At the end of the words, write the number
# of words plus the word "words", e.g., "3567 words" or "2 words".
# So:  the final list of words should look like this:
# AXXGFDXX
# BXXDFGXCVX
# DREXFRXWEXRXH
# 3809 words (or however many words there are)

oldFile = open("d.txt","r")

fullList = oldFile.readlines()
cList = []

for word in fullList:
    word = list(word)
    count = 0
    index = 0
    for letter in word:
        if letter == 'C':
            count += 1
            word[index] = 'X'
        index += 1
    if count == 4:
        cList.append(word)
oldFile.close()

newFile = open("fourx.txt","w")

for i in cList:
    newFile.write(''.join(i))

newFile.write(str(len(cList))+' words')

newFile.close()
