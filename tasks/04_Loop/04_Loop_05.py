# import regex lib
import re

# take the input of word and sentence
word = input()
sentence = input()

# init word count
word_counts = 0

# split string of sentence to list of word in sentence by include only alphabet
sentence = re.split(r'\W',sentence)

# loop through word in sentence
for sentence_word in sentence:
  # if sentence_word equal to word then increase the word count
  if sentence_word == word:
    word_counts += 1

# print the result of word counts
print(word_counts)