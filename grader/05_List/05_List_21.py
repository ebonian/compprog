# assign list of grade ascending
grade = ["A","B+","B","C+","C","D+","D","F"]

# assign list of student's id, student's grade, and student's uid
student_ids = []
student_grades = []
student_uids = []

# take the input
while (True):
  user_input = input()

  # check if user_input is "q" or not
  if user_input != "q":
    # if user_input is not "q" then split input into two values, student_id and student_grade
    student_id, student_grade = user_input.split(" ")

    # then append each id and grade to the lists as assigned before
    student_ids.append(student_id)
    student_grades.append(student_grade)

  else:
    # if user_input is "q" then take the input of student's id that recieve upgrade and split it to list
    student_uids = input().split(" ")

    # then break out of the input loop
    break

# loop through student_uids list which is the list of student that receive upgrade
for student_uid in student_uids:
  # in each student_uid, loop through student_ids list by its index
  for index in range(len(student_ids)):
    # check if uid is equal to id and check if its student_grades is not equal to A prevent index is out of range
    if (student_uid == student_ids[index] and student_grades[index] != "A"):
      # assign the the grade that is upgraded for that uid
      upgraded_grade = grade[grade.index(student_grades[index]) - 1]
      
      # replace the grade with upgraded_grade by index in list of student_grades
      student_grades[index] = upgraded_grade

# loop through student_ids by index
for index in range(len(student_ids)):
  # print out the result of id and grade by index of student_ids
  print(student_ids[index], student_grades[index])