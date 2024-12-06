import copy 

class Player:
    def __init__(self, x, y, max_x, max_y, direction, entry, stop_flag):
        self.x = x
        self.y = y
        self.max_x = max_x
        self.max_y = max_y
        self.direction = direction
        self.entry = entry
        self.stop_flag = stop_flag

def main():
    with open("input.txt" ,"r") as val:
        tmp = val.read().split("\n")
        entry = []

        # Split them to 2D array
        for i in tmp:
            entry.append(list(i))
        
        traverse(entry)

def traverse(entry:list):
    # Get the intial position
    y = 0
    x = 0

    # Get total possible infinite loop to set blocker
    total_infinite = 0

    for i in range(len(entry)):
        if "^" in entry[i]:
            y = i
            x = entry[i].index('^')
            entry[i][x] = "X"
            break
    
    for i in range(len(entry)):
        for j in range(len(entry[0])):
            entry_copy = copy.deepcopy(entry)
            
            if entry_copy[i][j] == ".":
                entry_copy[i][j] = "O"

                # Create player object
                player = Player(x=x, y=y, max_x=len(entry_copy), max_y=len(entry_copy[0]), direction="up", entry=entry_copy, stop_flag=False)
                # Get player steps
                previous_steps = []
                

                # Move player
                counter = 0
                while not player.stop_flag:
                    if counter == player.max_y * player.max_y:
                        total_infinite += 1
                        print(total_infinite)
                        break

                    if player.direction == "up":
                        move_up(player)
                    elif player.direction == "right":
                        move_right(player)
                    elif player.direction == "down":
                        move_down(player)
                    elif player.direction == "left":
                        move_left(player)

                    counter += 1

    # Print the possible obstacle positions to make guard spin infinitely
    print(total_infinite)

def move_up(player:object):
    if player.y - 1 < 0:
        player.stop_flag = True
        return 0
    if player.entry[player.y - 1][player.x] in ["#", "O"]:
        player.direction = "right"
    elif player.entry[player.y - 1][player.x] == ".":
        player.y -= 1
        player.entry[player.y][player.x] = "X"
    elif player.entry[player.y - 1][player.x] == "X":
        player.y -= 1


def move_right(player:object):
    if player.x + 1 >= player.max_x:
        player.stop_flag = True
        return 0
    if player.entry[player.y][player.x + 1] in ["#", "O"]:
        player.direction = "down"
        
    elif player.entry[player.y][player.x + 1] == ".":
        player.x += 1
        player.entry[player.y][player.x] = "X"
    elif player.entry[player.y][player.x + 1] == "X":
        player.x += 1
        

def move_down(player:object):
    if player.y + 1 >= player.max_y:
        player.stop_flag = True
        return 0
    if player.entry[player.y + 1][player.x] in ["#", "O"]:
        player.direction = "left"
    elif player.entry[player.y + 1][player.x] == ".":
        player.y += 1
        player.entry[player.y][player.x] = "X"
    elif player.entry[player.y + 1][player.x] == "X":
        player.y += 1

def move_left(player:object):
    if player.x - 1 < 0:
        player.stop_flag = True
        return 0
    if player.entry[player.y][player.x - 1] in ["#", "O"]:
        player.direction = "up"
    elif player.entry[player.y][player.x - 1] == ".":
        player.x -= 1
        player.entry[player.y][player.x] = "X"
    elif player.entry[player.y][player.x - 1] == "X":
        player.x -= 1        

main()