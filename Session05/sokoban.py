
map = { "size_x":5, 
        "size_y":5 }


player = {  "player_x":3,
            "player_y":4 }

boxes = [
    {"x":1,"y":1},
    {"x":2,"y":2},
    {"x":3,"y":3}
]

destionary = [
    {"x":2,"y":1},
    {"x":3,"y":2},
    {"x":4,"y":3}
]
playing = True 
while playing:
# print map
# check win
    win = True
    for box in boxes:
        if box not in destionary:
            win = False
    if win:
        print("you win")
        break

    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here = False
            if y == player["player_y"] and x == player["player_x"]:
                player_is_here = True
            box_is_here = False
            for box in boxes:
                if y == box["y"] and x == box["x"]:
                    box_is_here = True
            
            dest_is_here = False
            for dest in destionary:
                if y == dest["y"] and x == dest["x"]:
                    dest_is_here = True

            
            if player_is_here:
                print("P ",end="")
            elif box_is_here:
                print("B ", end="")
            elif dest_is_here:
                print("D ", end="")
            else:
                print("- ", end="")
            
        
        print()


    move = input("Your move:").upper()
    dx = 0
    dy = 0

    if move == "W":
        dy = -1
    elif move == "S":
        dy = 1
    elif move == "A":
        dx = -1
    elif move == "D":
        dx = 1
    else:
        playing = False


    if 0 <= player["player_x"] + dx <=4 and 0 <= player["player_y"] + dy <=4:


        player["player_x"] += dx
        player["player_y"] += dy 
    for box in boxes:
            if box["x"] == player["player_x"] and box["y"] == player["player_y"]:
                box["x"] += dx
                box["y"] += dy
