def main():
    with open("input.txt", "r") as val:
        levels = val.read().split("\n")
        total_safe = 0
        list_level = []

        # Populate the input to the 2D list
        for i in levels:
            list_level.append(list(map(int, i.split())))
        
        # Get the safe reports
        for i in list_level:
            if is_safe(i) == 0:
                total_safe += second_chance(i)
            else:
                total_safe += is_safe(i)
        print(total_safe)

def is_safe(report:list):
    is_increase = None
    for j in range(len(report) - 1):
        if is_increase == None:
            if report[j] > report[j + 1]:
                is_increase = False
            else:
                is_increase = True
        if not (abs(report[j] - report[j + 1]) >= 1 and abs(report[j] - report[j + 1]) <= 3):
            return 0
        if is_increase and report[j] > report[j + 1]:
            return 0
        if not is_increase and report[j] < report[j + 1]:
            return 0
        
        if j == len(report) - 2:
            return 1
    return 0

def second_chance(report:list):
    for i in range(len(report)):
        reduced_list = report.copy()
        reduced_list.pop(i)

        if is_safe(reduced_list) == 1:
            return 1
    return 0

main()