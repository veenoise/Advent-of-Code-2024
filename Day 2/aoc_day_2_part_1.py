with open("input.txt", "r") as val:
    levels = val.read().split("\n")
    total_safe = 0
    list_level = []

    # Populate the input to the 2D list
    for i in levels:
        list_level.append(list(map(int, i.split())))
    
    # Get the safe reports
    for i in list_level:
        isIncrease = None
        for j in range(len(i) - 1):
            if isIncrease == None:
                if i[j] > i[j + 1]:
                    isIncrease = False
                else:
                    isIncrease = True
            if not (abs(i[j] - i[j + 1]) >= 1 and abs(i[j] - i[j + 1]) <= 3):
                break
            if isIncrease and i[j] > i[j + 1]:
                break
            if not isIncrease and i[j] < i[j + 1]:
                break
            
            if j == len(i) - 2:
                total_safe += 1
            
    print(total_safe)