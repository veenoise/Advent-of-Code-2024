import re

def main():
    entry = filter()
    dont = False
    total = 0

    # Start filtering inputs
    for i in entry:
        if i == "don't()":
            dont = True
            continue
        elif i == "do()":
            dont = False
            continue
        
        if not dont:
            total += mul(list(map(int, i.split(","))))

    print(total)

def filter():
    with open("unfiltered.txt", "r") as val:
        filtered = re.findall(r"do\(\)|don't\(\)|(?<=mul\()\d{1,3},\d{1,3}(?=\))", val.read())
        return filtered
    return None

def mul(inp:list):
    return inp[0] * inp[1]

main()