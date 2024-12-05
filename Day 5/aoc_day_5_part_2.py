def main():
    with open("input.txt", "r") as val:
        page_order = []
        page_numbers = []
        entry = val.read().split("\n")
        separate = False
        
        for i in entry:
            if i == '':
                separate = True
                continue
            if not separate:
                page_order.append(i)
            else:
                page_numbers.append(i.split(","))
        
        update_list = is_valid(page_order, page_numbers)
        print(compute_middle(update_list))


def is_valid(page_order:list, page_numbers:list):
    update_list = []

    for i in page_numbers:
        valid_bool = True
        for j in range(len(i) - 1):
            for k in range(len(i) - 1 - j):
                if f"{i[j]}|{i[k + j + 1]}" not in page_order:
                    valid_bool = False
                    temp = i[j]
                    i[j] = i[k + j + 1]
                    i[k + j + 1] = temp
        if not valid_bool:
            update_list.append(i)

    return update_list

def compute_middle(update_list:list):
    total = 0

    for i in update_list:
        total += int(i[len(i) // 2])

    return total

main()