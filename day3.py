# Day [3]. 1st Part

batteries = []
total_joltage = 0

with open("batteries.txt") as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        batteries.append(line)

for i in batteries:

    biggest_jolt = 0
    biggest_jolt2 = 0
    jolt_index = 0

    for j in range(len(i)-1):
        if int(i[j]) > biggest_jolt:
            biggest_jolt = int(i[j])
            jolt_index = j
    
    for k in range(jolt_index + 1, len(i)):
        if int(i[k]) > biggest_jolt2:
            biggest_jolt2 = int(i[k])
    
    total_joltage = total_joltage + ((biggest_jolt * 10) + biggest_jolt2)

print(total_joltage)

# Day [3]. 2nd Part

batteries = []
total_joltage = 0

with open("batteries.txt") as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        batteries.append(line)

for i in batteries:
    battery_joltage = 0
    jolt_place = 0
    jolt_index = 0

    for m in range(11, -1, -1):
        biggest_jolt = 0
        
        for j in range(jolt_index, len(i)-m):
            if int(i[j]) > biggest_jolt:
                biggest_jolt = int(i[j])
                jolt_place = j
        
        jolt_index = jolt_place + 1
        battery_joltage = battery_joltage + (biggest_jolt * (10**m))

    total_joltage += battery_joltage

print(total_joltage)
