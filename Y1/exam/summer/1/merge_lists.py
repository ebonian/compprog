def merge_lists(d1, d2, n):
    d1 += [0]
    d2 += [0]

    for d1_index in range(len(d1)):
        d1_item = d1[d1_index]
        for d2_index in range(len(d2)):
            d2_item = d2[d2_index]

            if (d1_item == d2_item):
                print(d1_item, d2_item)
        
exec("print(merge_lists([1, 2, 3, 4, 5], [2, 3, 4], 2))")
exec("print(merge_lists([1, 2, 3, 4, 5], [2, 3, 4], 3))")
exec("print(merge_lists([1, 2, 3, 4, 5], [2, 3, 4], 4))")