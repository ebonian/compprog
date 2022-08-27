grade = ["A","B+","B","C+","C","D+","D","F"]

student_ids = []
student_grades = []
student_uids = []

while (True):
  user_input = input()

  if user_input != "q":
    student_id, student_grade = user_input.split(" ")

    student_ids.append(student_id)
    student_grades.append(student_grade)
  else:
    student_uids = input().split(" ")
    break

for student_uid in student_uids:
  for index in range(len(student_ids)):
    if (student_uid == student_ids[index]):
      if (student_grades[index] != "A"):
        upgraded_grade = grade[grade.index(student_grades[index]) - 1]
        
        student_grades[index] = upgraded_grade

for index in range(len(student_ids)):
  print(student_ids[index], student_grades[index])