def cal_defect_box_ratio(textfile):
    defect_box_ratio = 0

    file = open(textfile , "r")
    scan_data = file.readlines()[3][10:].split(",")

    # determine the dimension and grid
    dimension = round(len(scan_data) ** (1/3))
    grid = [scan_data[i:i+(dimension**2)] for i in range(0, len(scan_data), (dimension**2))]
    grid.reverse()

    # find the defected points and its coordinates
    defected_points = []
    for z in range(len(grid)):
        layer = grid[z]
        if "+" in layer:
            x = -1
            y = 0
            for i in range(len(layer)):
                value = grid[z][i]
                x += 1
                if x == dimension:
                    x = 0
                    y += 1
                if value == "+":
                    defected_points.append((x, y, z))

    # calculate the farthest diagonal points
    farthest_distance = 0
    farthest_points = None
    for i in range(len(defected_points)):
        for j in range(i+1, len(defected_points)):
            distance = ((defected_points[i][0]-defected_points[j][0])**2 + (defected_points[i][1]-defected_points[j][1])**2 + (defected_points[i][2]-defected_points[j][2])**2)
            if distance > farthest_distance:
                farthest_distance = distance
                farthest_points = (defected_points[i], defected_points[j])

    # calculate the area of the defected box
    length = abs(farthest_points[0][0] - farthest_points[1][0]) + 1
    width = abs(farthest_points[0][1] - farthest_points[1][1]) + 1
    height = abs(farthest_points[0][2] - farthest_points[1][2]) + 1

    defected_area = length * width * height
    defect_box_ratio = defected_area / dimension ** 3

    return round(defect_box_ratio,2)

print(cal_defect_box_ratio("001.txt"))
print(cal_defect_box_ratio("008.txt"))
print(cal_defect_box_ratio("010.txt"))