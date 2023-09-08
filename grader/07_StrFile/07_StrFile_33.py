data1path, data2path = input().split()

data1 = open(data1path).read()
data2 = open(data2path).read()

ids = data1.split()[0::2] + data2.split()[0::2]
grades = data1.split()[1::2] + data2.split()[1::2]

sorted_ids = []
sorted_grades = []

# sort by student id
for id, grade in sorted(zip(ids, grades)):
  sorted_ids.append(id)
  sorted_grades.append(grade)

# sort by faculty id
for id, grade in sorted(zip(sorted_ids, sorted_grades), key=lambda x: int(x[0][-2:])):
  print(id, grade)