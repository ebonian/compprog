output_f = "A.txt"
expected_f = "B.txt"


def check_all():
    count_error = 0
    with open(output_f, 'r', encoding="utf8") as t1, open(expected_f, 'r', encoding="utf8") as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    if range(len(fileone)) == range(len(filetwo)):
        for idx, (line1, line2) in enumerate(zip(fileone, filetwo)):
            if line1 != line2:
                count_error += 1
                print(idx+1, end=" ")
                print(line1, end="")
                print(idx+1, end=" ")
                print(line2)
        if count_error == 0:
            print("Check Passed")
        else:
            print("Check Failed", count_error, "errors")
    else:
        print('Files are not the same length')


def check_one_line(line_number):
    line_number -= 1
    with open(output_f, 'r', encoding="utf8") as t1, open(expected_f, 'r', encoding="utf8") as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    if range(len(fileone)) == range(len(filetwo)):
        print(fileone[line_number], filetwo[line_number])
        for x, y in zip(fileone[line_number].split(','), filetwo[line_number].split(',')):
            if x != y:
                print(x, y)
                break
    else:
        print('Files are not the same length')


# check_one_line(1878)
check_all()
