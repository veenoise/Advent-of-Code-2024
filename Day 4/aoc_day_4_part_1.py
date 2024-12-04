import re

def main():
    total = 0

    with open("input.txt", "r") as val:
        entry = val.read().split()
        total += search_horizontal(entry)
        total += search_vertical(entry)
        total += search_diagonal_right(entry)
        total += search_diagonal_left(entry)

        print(total)

def search_horizontal(xmas_list:str):
    total = 0

    for i in xmas_list:
        for j in range(len(xmas_list[0]) - 3):
            if i[j] == "X" and i[j + 1] == "M"\
            and i[j + 2] == "A" and i[j + 3] == "S":
                total += 1
            elif i[j] == "S" and i[j + 1] == "A"\
            and i[j + 2] == "M" and i[j + 3] == "X":
                total += 1

    return total

def search_vertical(xmas_list:list):
    total = 0
    
    for i in range(len(xmas_list) - 3):
        for j in range(len(xmas_list[0])):
            if xmas_list[i][j] == "X" and xmas_list[i + 1][j] == "M"\
            and xmas_list[i + 2][j] == "A" and xmas_list[i + 3][j] == "S":
                total += 1
            elif xmas_list[i][j] == "S" and xmas_list[i + 1][j] == "A"\
            and xmas_list[i + 2][j] == "M" and xmas_list[i + 3][j] == "X":
                total += 1
    
    return total

def search_diagonal_right(xmas_list:list):
    list_len = len(xmas_list)
    string_len = len(xmas_list[0])
    total = 0

    for i in range(list_len - 3):
        for j in range(string_len - 3):
            if xmas_list[i][j] == "X" and xmas_list[i + 1][j + 1] == "M"\
            and xmas_list[i + 2][j + 2] == "A" and xmas_list[i + 3][j + 3] == "S":
                total += 1
            elif xmas_list[i][j] == "S" and xmas_list[i + 1][j + 1] == "A"\
            and xmas_list[i + 2][j + 2] == "M" and xmas_list[i + 3][j + 3] == "X":
                total += 1

    return total

def search_diagonal_left(xmas_list:list):
    list_len = len(xmas_list)
    string_len = len(xmas_list[0])
    total = 0

    for i in range(list_len - 3):
        for j in range(string_len - 3):
            if xmas_list[i][j + 3] == "X" and xmas_list[i + 1][j + 2] == "M"\
            and xmas_list[i + 2][j + 1] == "A" and xmas_list[i + 3][j] == "S":
                total += 1
            elif xmas_list[i][j + 3] == "S" and xmas_list[i + 1][j + 2] == "A"\
            and xmas_list[i + 2][j + 1] == "M" and xmas_list[i + 3][j] == "X":
                total += 1

    return total

main()