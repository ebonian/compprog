key_string = input()
answer_string = input()

correct_answer = 0

if (len(key_string) == len(answer_string)):
  for key, answer in zip(key_string, answer_string):
    if (key == answer):
      correct_answer += 1
  print(correct_answer)
else:
  print("Incomplete Answer")