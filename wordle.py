# The challenge is to solve Wordle.  We will take all submissions and choose 3-5
# words at random and see which program is the best at finding the secret words.
# The program will give the user a word and the user will reply 0 if a letter is
# not in the word, 1 if it is but in the wrong place, and 2 if it is correct and
# in the right place.  So, if the computer asks "about", I, as the user, might
# reply "00102", meaning that the "o" is correct but in the wrong place, the "t"
# is correct and in the right spot, and the "a", "b" and "u" are not in the word.
#  This continues until the computer guesses the right word.
import random
dictionary = open("d.txt","r")
five = []
for words in dictionary:
    if len(words) == 6:
        five.append(words[:5])
counter = 1

print("Respond in the format #####. If the letter is not in the word, reply 0, if the letter is in the word in the wrong place, reply 1, and if it is the right letter in the right place, write 2.\n")
print("The first feedback goes through the full dictionary, so it is slow. Thank you for your patience.")
print("The first guess is: ADIEU")
guess = "ADIEU"
feedback = input("Type the feedback here: ")
list = []
answer = []
extra = []
wrong = []
inWord = []
while feedback != "22222":
    list.clear()
    for letter in feedback:
        list.append(letter)
    # print(len(list))
    for index in range(5):
        if list[index] == "2":
            answer.append([index,guess[index]])
            inWord.append(guess[index])
        elif list[index] == "1" and [index,guess[index]] not in extra:
            extra.append([index, guess[index]])
            inWord.append(guess[index])
        elif list[index] == "0":
            wrong.append(guess[index])
    toDelete = []
    for word in five:
        # print(word)
        for a in wrong:
            if a not in inWord and a in word and word in five and word not in toDelete:
                toDelete.append(word)

        for b in extra:
            if b[1] not in word and word in five and word not in toDelete:
                toDelete.append(word)
            elif b[1] == word[b[0]]:
                toDelete.append(word)

        for c in answer:
            if c[1] != word[c[0]]:
                toDelete.append(word)

    # print(toDelete)
    for word in toDelete:
        if word in five:
            five.remove(word)

    # print(wrong)
    # print(extra)
    # print(inWord)
    # print(answer)
    # print(five)
    guess = five[random.randint(0,len(five)-1)]
    print('\nThe next guess is: ' + guess)
    feedback = input("Type the feedback here: ")

    counter += 1


if feedback == "22222":
    print("The word is " + guess)
    print("It took " + str(counter) + " guesses.")

dictionary.close()
