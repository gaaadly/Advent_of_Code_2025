# Day 5. Part 1

ingredients = []
ingredients_id = []

with open('ingredients_list.txt') as new_file:
    for line in new_file:
        line = line.replace('\n', '')
        if line.find('-') != -1:
            ingredients_id.append(line)
        elif line != '': 
            ingredients.append(line)

fresh_ingredients = 0

for item in ingredients:
    for id in ingredients_id:
        if int(id[0:id.find('-')]) <= int(item) and int(item) <= int(id[id.find('-')+1:])+1:
            fresh_ingredients += 1
            break

print(fresh_ingredients)

# Day 5. Part 2

ingredients_id = []
fresh_ingredients = []

with open('ingredients_list.txt') as new_file:
    for line in new_file:
        line = line.replace('\n', '')
        if line.find('-') != -1:
            ingredients_id.append(line)


def count_fresh_ingredients(ingredients_ranges: list):
    ranges = []
    for r in ingredients_ranges:
        start, end = map(int, r.split('-'))
        ranges.append((start, end))
    
    ranges.sort()
    
    if not ranges:
        return 0
        
    merged = []
    current_start, current_end = ranges[0]
    
    for next_start, next_end in ranges[1:]:
        if next_start <= current_end + 1:
            # Overlap detected: extend the current end if needed
            current_end = max(current_end, next_end)
        else:
            # No overlap: save current range and start a new one
            merged.append((current_start, current_end))
            current_start, current_end = next_start, next_end
            
    # Append the final range
    merged.append((current_start, current_end))
    
    # Calculate total count from merged ranges
    total_count = 0
    for start, end in merged:
        # +1 is necessary because the range includes both start and end
        total_count += (end - start) + 1
        
    return total_count

print(count_fresh_ingredients(ingredients_id))
