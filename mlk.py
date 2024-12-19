# This week:  Using the following quote from Martin Luther King's "I Have a Dream"
# speech, find the longest substring of letters that doesn't contain any duplicates.
speech = "I have a dream that one day this nation will rise up and live out the true meaning of its creed. I have a dream that one day on the red hills of Georgia, the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood. I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice. I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character."

speech = speech.lower()

speech = speech.replace(".", "")
speech = speech.replace(",", "")
speech = speech.replace(" ", "")

print(speech)
lengths = []
for i in range(len(speech)):
    repeat = False
    list = []
    count = 0
    while repeat == False:
        if i+count < len(speech):
            if speech[i+count] not in list:
                list.append(speech[i+count])
                count+=1
            else:
                repeat = True
        else:
            repeat = True
    lengths.append([count,i])
    print([count,i])

print(max(lengths))
answer = []
for x in range(max(lengths)[0]):
    answer.append(speech[x+max(lengths)[1]])
    print(speech[x+max(lengths)[1]])

print(answer)

print("The longest non-repeating substring of letters is: ")
print(''.join(answer))
