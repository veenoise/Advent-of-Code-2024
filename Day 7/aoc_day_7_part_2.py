from itertools import product
import re

def main():
    with open("input.txt", "r") as val:
        total = 0
        entry = val.read().split("\n")

        for i in entry:
            tmp = i.split(" ")
            key = re.findall("(.+):", i)
            total += int(determine_operation(key[0], tmp[1:]))

        print(total)

def determine_operation(key:int, operands:list):
    operators = ['*', "+" , "|"]
    permutations = list(product(operators, repeat=(len(operands) - 1)))

    for perm in permutations:
        operator_perm = "".join(perm)
        tmp_total = 0

        for j in range(len(operator_perm)):
            if tmp_total == 0:
                tmp_total += evaluate(operands[0], operator_perm[0], operands[j + 1])
            else:
                tmp_total = evaluate(tmp_total, operator_perm[j], operands[j + 1])

        if int(key) == int(tmp_total):
            return key
    
    return 0

def evaluate(operand_1:int, operator:str, operand_2):
    if operator == "+":
        return int(operand_1) + int(operand_2)
    elif operator == "|":
        return int(f"{operand_1}{operand_2}")
    else:
        return int(operand_1) * int(operand_2)

main()