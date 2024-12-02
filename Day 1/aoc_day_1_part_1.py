with open("input.txt", 'r') as val:
    is_list1 = True
    total = 0
    entry = val.read().split()
    list1 = []
    list2 = []

    # Split the input into 2 lists
    for i in entry:
        if is_list1:
            list1.append(i)
            is_list1 = not is_list1
        else:
            list2.append(i)
            is_list1 = not is_list1

    # Sort the lists
    list1.sort()
    list2.sort()
    
    # Get the total length
    for i in range(len(list1)):
        total += abs(int(list1[i]) - int(list2[i]))
    
    print(total)