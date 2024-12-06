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

    for i in range(len(entry)):
        if "^" in entry[i]:
            y = i
            x = entry[i].index('^')
            entry[i][x] = "X"
            break

    # Create player object
    player = Player(x=x, y=y, max_x=len(entry), max_y=len(entry[0]), direction="up", entry=entry, stop_flag=False)
    
    # Move player
    while not player.stop_flag:
        if player.direction == "up":
            move_up(player)
        elif player.direction == "right":
            move_right(player)
        elif player.direction == "down":
            move_down(player)
        elif player.direction == "left":
            move_left(player)

    # Get occurence of X in 2D array
    total_X = 0
    for i in player.entry:
        total_X += i.count('X')

    print(total_X)

def move_up(player:object):
    if player.y - 1 < 0:
        player.stop_flag = True
        return 0
    if player.entry[player.y - 1][player.x] == "#":
        player.direction = "right"
    else:
        player.y -= 1
        player.entry[player.y][player.x] = "X"
        
def move_right(player:object):
    if player.x + 1 >= player.max_x:
        player.stop_flag = True
        return 0
    if player.entry[player.y][player.x + 1] == "#":
        player.direction = "down"
    else:
        player.x += 1
        player.entry[player.y][player.x] = "X"

def move_down(player:object):
    if player.y + 1 >= player.max_y:
        player.stop_flag = True
        return 0
    if player.entry[player.y + 1][player.x] == "#":
        player.direction = "left"
    else:
        player.y += 1
        player.entry[player.y][player.x] = "X"

def move_left(player:object):
    if player.x - 1 < 0:
        player.stop_flag = True
        return 0
    if player.entry[player.y][player.x - 1] == "#":
        player.direction = "up"
    else:
        player.x -= 1
        player.entry[player.y][player.x] = "X"

main()