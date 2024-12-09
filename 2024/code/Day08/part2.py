def solve(input):
    matrix = []

    for line in input:
        matrix.append(list(line))

    antinodes = set()
    freqs = dict()

    # Finds all frequencies and their positions
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            elem = matrix[y][x]
            if elem == ".":
                continue

            if elem in freqs:
                freqs[elem].append((x, y))
            else:
                freqs[elem] = [(x, y)]

    # Goes through each pairs of positions for each frequency
    for freq in freqs.values():
        for pos1 in freq:
            for pos2 in freq:
                if pos1 == pos2:
                    continue

                newx = 0
                newy = 0
                mult = 2

                # Keep adding antinodes until it's out of bounds
                while (
                    newx >= 0
                    and newy >= 0
                    and newx < len(matrix[0])
                    and newy < len(matrix)
                ):
                    diffx = -1 * mult * (pos1[0] - pos2[0])
                    diffy = -1 * mult * (pos1[1] - pos2[1])

                    newx = pos1[0] + diffx
                    newy = pos1[1] + diffy

                    if (
                        newx < 0
                        or newy < 0
                        or newx >= len(matrix[0])
                        or newy >= len(matrix)
                    ):
                        continue

                    antinodes.add((newx, newy))

                    mult += 1

            # Add the nodes that appear on every antenna
            antinodes.add((pos1[0], pos1[1]))

    return len(antinodes)
