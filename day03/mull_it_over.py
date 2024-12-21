import re

def read_file_and_get_data(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()

def mul(a, b):
    return a * b

file_data = read_file_and_get_data("./data.txt")

regex = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"

file_data_list = re.findall(regex, str(file_data))
print(file_data_list)
# print(str(file_data))

print(len(file_data_list))
total = 0
for i in file_data_list:
    # print(i)
    multiplication = mul(int(i[0]), int(i[1]))
    print(f"Multiplication of {i[0]} * {i[1]}: ", multiplication)
    total += multiplication

print(total)