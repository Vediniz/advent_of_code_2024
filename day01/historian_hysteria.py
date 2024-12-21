
def readfile_n_split_list(filename):
    rigth_list = []
    left_list = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split()
            left_list.append(int(line[0]))
            rigth_list.append(int(line[1]))
    return left_list, rigth_list

l_list, r_list = readfile_n_split_list("./data.txt")

if len(l_list) != len(r_list):
    print(f"Error: The lists are not the same length, {len(l_list)} != {len(r_list)}")
    exit()
else:
    total = 0
    print(f"Lists are the same length: {len(l_list)}")
    l_list = sorted(l_list)
    r_list = sorted(r_list)
    for i in range(len(l_list)):
        print(f"Left: {l_list[i]} Right: {r_list[i]}")
        difference = l_list[i] - r_list[i]
        if difference < 0 and difference != 0:
            difference = difference * -1
        total += difference

    print(f"Sum of differences: {total}")
