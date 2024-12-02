with open("input.txt", "r") as val:
    entry = val.read().split()
    isList1 = True
    list1 = []
    list2 = []
    dictNumbers = {}
    total = 0

    # Separate the input into two lists
    for i in entry:
        if isList1:
            list1.append(int(i))
            isList1 = not isList1
        else:
            list2.append(int(i))
            isList1 = not isList1

    # Count for instance of a number in the left list from the right list
    # Multiply this count by the instance we are looking for (i * count)
    for i in list1:
        if i not in dictNumbers:
            count = list2.count(i)
            dictNumbers[i] = i * count
        total += dictNumbers[i]

    print(total)