import re

def main():
    entry = filter()
    total = 0

    for i in entry:
        total += mul(list(map(int,i.split(","))))
    print(total)

def filter():
    with open("unfiltered.txt", "r") as val:
        filtered = re.findall(r"(?<=mul\()\d{1,3},\d{1,3}(?=\))", val.read())
        return filtered
    return None

def mul(inp:list):
    return inp[0] * inp[1]

main()