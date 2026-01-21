# Day [8] 1st and 2nd Parts

def solve(part):

    # Add data from the input
    with open('input.txt') as new_file:
        coords = [[int(n) for n in line.strip().split(",")] for line in new_file]

    # Build a list of pairs of coords, reverse sorted by distance
    ncoords = len(coords)

    distances = []
    for c1 in range(ncoords):
        for c2 in range(c1+1, ncoords):
            dx = (coords[c1][0] - coords[c2][0]) ** 2
            dy = (coords[c1][1] - coords[c2][1]) ** 2
            dz = (coords[c1][2] - coords[c2][2]) ** 2
            distances.append([dx + dy + dz, [c1,c2]])
    distances.sort(reverse=True)

    # Create single coordinate circuits
    circuits = [{n} for n in range(ncoords)]
    
    def cfind(n):
        for i,circuit in enumerate(circuits):
            if n in circuit:
                return i
        return None

    n = 1000
    while n > 0:
        n -= 1
        c1, c2 = distances.pop()[1]
        # Find the circuits these coords are in
        i1, i2 = cfind(c1), cfind(c2)
        if i1 != i2:
            # Merge circuits
            circuits[i1] = circuits[i1] | circuits[i2]
            del circuits[i2]
        if part == 2:
            # Keep going until only 1 circuit
            if len(circuits) == 1:
                break
            n += 1
    
    if part == 1:
        # Multiply length of 3 longest circuits
        circuits.sort(key=lambda c: len(c))
        print(len(circuits.pop()) * len(circuits.pop()) * len(circuits.pop()))
    else:
        # Multiply x coords of final joined pair
        print(coords[c1][0] * coords[c2][0])

solve(1)
solve(2)
