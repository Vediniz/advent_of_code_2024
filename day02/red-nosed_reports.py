
def readfile_n_split_list(filename):
    reports = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split()
            reports.append(line)
    return reports

valids_entries = 0
entries= []
invalid = []

for i in readfile_n_split_list("./data.txt"):
    valid = True

    for num, j in enumerate(i):
        j = int(j)        
        prev_number = int(i[num-1])

        if num == 0:
            next_number = int(i[num+1])
            value = j - next_number
            direction = "increase" if value < 0 else "decrease"
            print(direction)

        else:
            value = j - prev_number
            value = abs(value)
            print(f"{i}{num} Value: {value}")
            if value > 3 or value == 0:
                print(f"Invalid entry: {i}")
                valid = False
                invalid.append(i)
                break
            if direction == "increase" and prev_number >= j:
                valid = False
                invalid.append(i)
                break    
            if direction == "decrease" and prev_number <= j:
                valid = False
                invalid.append(i)
                break            
            
    if valid:
        entries.append(i)
        print(f"Valid entry: {i}")
        valids_entries += 1

print(f"Valid entries: {valids_entries}")

# for num, i in enumerate(entries):
#     print(f"valid: {num}, {i}")


# for num, i in enumerate(invalid):
#     print(f"invalid : {num}, {i}")