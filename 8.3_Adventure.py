"""
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

"""
room_list = []
# create room and add to room list
room = ["You are on the front porch", 2, None, None, None]
room_list.append(room)
room = ["You are in Bedroom 2", 4, 2, None, None]
room_list.append(room)
room = ["You are in the South Hall", 5, 3, 0, 1]
room_list.append(room)
room = ["You are in the Dining Room", 6, None, None, 2]
room_list.append(room)
room = ["You are in Bedroom 1", None, 5, 1, None]
room_list.append(room)

current_room = 0
Done = False
while not Done:
    print()
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S as the direction you want to go or Q to quit")

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way")
        else:
            current_room = next_room
    #QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        Done = True
    else:
        print("not sure you know what you are doing")

print("Thanks for playing")
