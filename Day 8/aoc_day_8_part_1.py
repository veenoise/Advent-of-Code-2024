import pprint

def main():
    with open("input.txt", "r") as val:
        entry = val.read().split("\n")
        mapping = {}
        max_x = 0
        max_y = 0
        antinodes = []
        max_x = len(entry[0]) - 1
        max_y = len(entry) - 1

        # Map the coordinates {"T": [(1, 2), (2, 3)]}
        for i in range(len(entry)):
            for j in range(len(entry[i])):
                if entry[i][j] != ".":
                    if entry[i][j] not in mapping:
                        mapping[entry[i][j]] = [(j, i)]
                    else:
                        mapping[entry[i][j]].append((j, i))
        
        # Get mapping keys
        for i in mapping:
            # Call get_antinodes to get list of valid antinodes
            for j in get_antinodes(max_x, max_y, mapping[i]):
                antinodes.append(j)
        
        # Use set to get unique values only
        print(len(set(antinodes)))

def get_antinodes(max_x:int, max_y:int, coords:list):
    valid_antinodes = []

    for i in range(len(coords) - 1):
        for j in range(1 + i, len(coords)):
            # Get antinodes of this pair
            # print(f"{coords[i]} {coords[j]}")
            
            # Get the distance
            distance = (coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])

            # Calculate the antinodes
            antinode_1 = (coords[i][0] + distance[0], coords[i][1] + distance[1])
            antinode_2 = (coords[j][0] - distance[0], coords[j][1] - distance[1])

            # Append to list if not out of bounds
            if antinode_1[0] >= 0 and antinode_1[0] <= max_x and antinode_1[1] >= 0 and antinode_1[1] <= max_y:
                valid_antinodes.append(antinode_1)
            if antinode_2[0] >= 0 and antinode_2[0] <= max_x and antinode_2[1] >= 0 and antinode_2[1] <= max_y:
                valid_antinodes.append(antinode_2)
    
    # Returns coords of antinodes
    return valid_antinodes

main()