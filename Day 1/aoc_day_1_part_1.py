with open("input.txt", 'r') as val:
    isList1 = True
    total = 0
    entry = val.read().split()
    list1 = []
    list2 = []

    # Split the input into 2 lists
    for i in entry:
        if isList1:
            list1.append(i)
            isList1 = not isList1
        else:
            list2.append(i)
            isList1 = not isList1

    # Sort the lists
    list1.sort()
    list2.sort()
    
    # Get the total length
    for i in range(len(list1)):
        total += abs(int(list1[i]) - int(list2[i]))
    
    print(total)