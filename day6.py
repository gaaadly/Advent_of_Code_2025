# Day [6]. 1st Part

exercises = []
total = 0

# take puzzle input
with open("input.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        exercises.append(line.split(" "))

# remove empty strings from sublists
for exercise in exercises:
    exercise[:] = [item for item in exercise if item]

# iterrate through all exercises and calculate total sum/multiplication based on the function required
for i in range(len(exercises[0])):
    temp_sum = 0
    temp_multiply = 1
    counter = 0

    for j in range(len(exercises)-2, -1, -1):
        counter += 1
        if exercises[-1][i] == '+':
            temp_sum += int(exercises[j][i])
        elif exercises[-1][i] == '*':
            temp_multiply *= int(exercises[j][i])

    # calculate total sum of exercises
    if temp_multiply > 1:
        total += temp_multiply
    else:
        total += temp_sum

print(total)

# Day [6]. 2nd Part

def product(lst):
    p = 1
    for n in lst:
        p *= n
    return p

rows = []

with open("input.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        rows.append(line)

human_math_list = []
num_list = []

for j in range(len(rows[0]) - 1, -1, -1):
    if all(rows[r][j].isspace() for r in range(len(rows))):
        human_math_list.append(num_list)
        num_list = []
        continue
    num = ''
    for i in range(len(rows)):
        try:
            if rows[i][j].isnumeric():
                num += rows[i][j]
            if rows[i][j] in '+*':
                num_list.insert(0, rows[i][j])
        except:
            print(f"culprit: {j=}")
    num_list.append(num)
    if j == 0:
        human_math_list.append(num_list)

checksum = 0
for problem in human_math_list:
    if problem[0] == '+':
        checksum += sum(list(map(int, problem[1:])))
    else:
        checksum += product(list(map(int, problem[1:])))

print(checksum)
