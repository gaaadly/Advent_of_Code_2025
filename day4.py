# Day [4]. 1st Part

warehouse = []
total_count = 0

with open("warehouse.txt") as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        warehouse.append(line)


rows = len(warehouse)
cols = len(warehouse[0])

# Offsets for 8 directions: (row_change, col_change)
# Top-Left, Top, Top-Right, Right, Bottom-Right, Bottom, Bottom-Left, Left
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, 1), (1, 1), (1, 0),
    (1, -1), (0, -1)
]

for r in range(rows):
    for c in range(cols):
        if  warehouse[r][c] != '@':
            continue
        counter = 0
        # Check all 8 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Verify coordinates are within valid bounds before accessing
            if 0 <= nr < rows and 0 <= nc < cols:
                if warehouse[nr][nc] == '@':
                    counter += 1
    
        if counter < 4:
            total_count += 1

print(total_count)


# Day [4]. 2nd Part

warehouse = []
total_count = 0

with open("warehouse.txt") as new_file:

    for line in new_file:
        line = line.replace("\n", "")
        warehouse.append(line)

rows = len(warehouse)
cols = len(warehouse[0])

# Offsets for 8 directions: (row_change, col_change)
# Top-Left, Top, Top-Right, Right, Bottom-Right, Bottom, Bottom-Left, Left
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, 1), (1, 1), (1, 0),
    (1, -1), (0, -1)
]

while True:
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if  warehouse[r][c] != '@':
                continue
            counter = 0
            # Check all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Verify coordinates are within valid bounds before accessing
                if 0 <= nr < rows and 0 <= nc < cols:
                    if warehouse[nr][nc] == '@':
                        counter += 1
        
            if counter < 4:
                total_count += 1
                to_remove.append((r, c))

    # if list is empty break the cycle
    if not to_remove:
        break
    
    # create new updated array
    for r, c in to_remove:
        warehouse[r] = warehouse[r][:c] + '.' + warehouse[r][c+1:]

print(total_count)
