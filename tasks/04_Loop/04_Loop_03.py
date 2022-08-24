# take the input of correct answer and student answer string line by line
key_string = input()
answer_string = input()

# init correct answer
correct_answer = 0

# if the length between correct answer and student answer then loop through the condition
if (len(key_string) == len(answer_string)):
  # loop correct answer and student answer
  for key, answer in zip(key_string, answer_string):
    # check if character of correct answer and student answer are the same then increase the correct answer
    if (key == answer):
      correct_answer += 1

  print(correct_answer)

# if the length between correct answer and student answer then it's incomplete answer
else: 
  print("Incomplete answer")