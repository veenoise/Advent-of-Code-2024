with open("input.txt", "r") as val:
    entry = val.read().split()
    is_list1 = True
    list1 = []
    list2 = []
    dict_numbers = {}
    total = 0

    # Separate the input into two lists
    for i in entry:
        if is_list1:
            list1.append(int(i))
            is_list1 = not is_list1
        else:
            list2.append(int(i))
            is_list1 = not is_list1

    # Count for instance of a number in the left list from the right list
    # Multiply this count by the instance we are looking for (i * count)
    for i in list1:
        if i not in dict_numbers:
            count = list2.count(i)
            dict_numbers[i] = i * count
        total += dict_numbers[i]

    print(total)