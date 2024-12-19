
# "Facetious" is an unusual English word.  Why is it unusual, and what other
#words have the same property?  Find all words that share the property that
#make facetious special.
# Don't include words that are derived from a simpler word (i.e., don't say
#"big" and then "bigger", or "slow" and then "slowly".  Just say big and slow.)

dict = open('words_alpha.txt','r')

wordList = dict.readlines()
answer = []
vowels = ['a','e','i','o','u']

for word in wordList:
    tester = []
    for letter in word:
        if letter.lower() in vowels:
            tester.append(letter.lower())
    if tester == vowels:
        answer.append(word)

print(''.join(answer))
print('There are ' + str(len(answer)) + ' words in the English language that')
print('have all regular vowels in alphabetical order.')

print(len(wordList))

dict.close()
