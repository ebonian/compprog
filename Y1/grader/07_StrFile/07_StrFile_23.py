file_name, year = input().split()

if (file_name != 'data.txt'):
  print("No data")
else:
  f = open(file_name).read()

  student_ids = f.split()[0::2]
  student_grades = [float(grade) for grade in f.split()[1::2]]

  DATA = {}

  for key in student_ids:
      for value in student_grades:
          DATA[key] = value
          student_grades.remove(value)
          break

  grades = []

  short_year = year[2:]

  if (short_year not in [key[:2] for key in DATA.keys()]):
    print("No data")
  else:
    for i in range(len(DATA.keys())):
      if (short_year == [key[:2] for key in DATA.keys()][i]):
        key = [key for key in DATA.keys()][i]
        grades.append(DATA.get(key, 0))
    
    print(min(grades), max(grades), sum(grades) / len(grades))