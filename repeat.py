# There are lots of words in English that have 2 consecutive pairs of identical
# letters.  For example, "Unneeded" and "Woolly" are words that have this quality.
#  However, there is only 1 word (that I am aware of) that has 3 consecutive pairs
#  of identical letters.  What is that word?
#
# If the word has variations, just indicate the base word.  So, for example, if
# the word was "Play", don't bother saying "Plays" or "Playing", that sort of thing.
answer = []
def hasRepeats(word):
    list = []
    repeats = []
    list.append("")
    for letter in word:
        list.append(letter)
    list.append("")
    for letter in list:
        if letter != "":
            letterIndex = list.index(letter)
            if list[letterIndex] == list[letterIndex - 1]:
                if letterIndex not in repeats:
                    repeats.append(letterIndex)
                    repeats.append(letterIndex - 1)
            if list[letterIndex] == list[letterIndex + 1]:
                if letterIndex not in repeats:
                    repeats.append(letterIndex)
                    repeats.append(letterIndex + 1)
    # if len(repeats) > 0:
    #     print(word)
    #     print(repeats)
    #     print('\n')
    if len(repeats) > 4:
        if min(repeats) + len(repeats) - 1 == max(repeats):
            answer.append(word)
dictionary = open("d.txt","r")

for word in dictionary:
    hasRepeats(word)

print('The word with three consecutive pairs of repeated letters is ' + answer[0])

dictionary.close()
