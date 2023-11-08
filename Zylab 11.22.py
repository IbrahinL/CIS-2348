# ask the user for the input
user_input = input(str())
# split the sentence of the input
sentence = user_input.split()
for i in sentence:
# the loop counts the amount of times a word is in the sentence
    frequencies = sentence.count(i)
    print(i, frequencies)