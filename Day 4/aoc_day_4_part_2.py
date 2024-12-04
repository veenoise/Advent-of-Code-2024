import re

def main():
    total = 0

    with open("input.txt", "r") as val:
        entry = val.read().split()
        total += search_xmas(entry)

        print(total)

def search_xmas(xmas_list:str):
    total = 0
    
    for i in range(len(xmas_list) - 2):
        for j in range(len(xmas_list[0]) - 2):
            if (xmas_list[i + 1][j + 1] == "A" and\
            ((xmas_list[i][j] == "S" and xmas_list[i + 2][j + 2] == "M") or\
            (xmas_list[i][j] == "M" and xmas_list[i + 2][j + 2] == "S")) and\
            ((xmas_list[i][j + 2] == "S" and xmas_list[i + 2][j] == "M") or\
            (xmas_list[i][j + 2] == "M" and xmas_list[i + 2][j] == "S"))):
                total += 1

    return total

main()