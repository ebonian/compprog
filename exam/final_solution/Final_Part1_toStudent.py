def get_consensus(ss):
    # write your code here.
    ss = [x.upper() for x in ss.split()]

    arranged = {}

    for line in ss:
        for i in range(len(line)):
            arranged[i] = "{}".format(arranged.get(i, "") + line[i])

    count = []

    for row in arranged:
        count_obj = {}
        for char in arranged[row]:
            count_obj[char] = count_obj.get(char, 0) + 1
        count.append(count_obj)

    consensus = []

    for row in count:
        max_count = 0
        max_char = []
        for char in row:
            if row[char] > max_count:
                max_count = row[char]

        for char in row:
            if max_count == row[char]:
                max_char.append(char)

        consensus.append("/".join(sorted(max_char)))

    consensus = " ".join(consensus)

    return consensus  # DO NOT MODIFY THIS LINE


def get_consensus_generic(ss):
    # write your code here.
    return get_consensus(ss)
    # return consensus  # DO NOT MODIFY THIS LINE

# ---------------------------------------
# DO NOTE MODIFY CODE AFTER THIS SECTION
# ---------------------------------------


ss = ("ATCGATGC\n" +
      "GTACaCGC\n" +
      "ACTACAGC\n" +
      "CtCAATTC\n" +
      "CTGgATTC")
print(get_consensus(ss))

ss = ("ATCGATGC\n" +
      "GTACaCCC\n" +
      "ACTACATC\n" +
      "CtCAATAC")
print(get_consensus(ss))

ss = ("YCXBATGZ\n" +
      "YCVBaCGZ\n" +
      "ACXBCTGZ\n" +
      "CtCAATTZ\n" +
      "CTXAATTM")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +
      "YCVBaCGZHQ\n" +
      "ACXBCTGZHQ\n" +
      "CtCAATTZHD\n" +
      "CTXAATTMFD")
print(get_consensus_generic(ss))

ss = ("YCXBATGZ\n" +
      "YCVCaCGZHQ\n" +
      "ACXDCTGZHQ\n" +
      "CtCTATTZHD\n" +
      "CTXAATTMFD")
print(get_consensus_generic(ss))
