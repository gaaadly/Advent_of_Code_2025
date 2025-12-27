# Day [7]. 1st Part

input_list = []
total = 0

# take puzzle input
with open("input.txt") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        input_list.append(line)

# I change the 2D array as well as calculate the splits
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        if input_list[i][j] == 'S':
            input_list[i+1] = input_list[i+1][:j] + '|' + input_list[i+1][j+1:]
        if input_list[i][j] == '^' and input_list[i-1][j] == '|':
            input_list[i] = input_list[i][:j-1] + '|' + '^' + '|' + input_list[i][j+2:]
            total += 1
        if input_list[i][j] == '.' and input_list[i-1][j] == '|':
            input_list[i] = input_list[i][:j] + '|' + input_list[i][j+1:]
            
print(total)

# Day[7] 2nd part

with open("input.txt") as puzzleInput:
    manifold = [list(line.strip()) for line in puzzleInput]

# For 2nd part I need to create list of each member
a1, timelines = 0, [[0 for _ in row] for row in manifold]

for y, row in enumerate(manifold):
    for x, cell in enumerate(row):
        if cell == "S":
            timelines[y][x] = 1
        elif cell == "^":
            timelines[y][x-1] += timelines[y-1][x]
            timelines[y][x+1] += timelines[y-1][x] + timelines[y-1][x+1]
            
        else:
            timelines[y][x] = max(timelines[max(y-1,0)][x],timelines[y][x])


print(f"Part two: {sum([n for n in timelines[-1]])}")
