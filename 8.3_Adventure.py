"""
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

"""
room_list = []
bag = []
Meat = []
Large_Key = []
medicine = []
# create room and add to room list
room = ["You are on the front porch", 2, None, None, None]
room_list.append(room)
room = ["You are in Bedroom 2", 4, 2, None, None]
room_list.append(room)
room = ["You are in the South Hall", 5, 3, 0, 1]
room_list.append(room)
room = ["You are in the Dining Room", None, None, None, 2]
room_list.append(room)
room = ["You are in Bedroom 1", None, 5, 1, None]
room_list.append(room)
room = ["You are in the North Hall", 7, 6, 2, 4]
room_list.append(room)
room = ["You are in the kitchen", None, None, 3, 5]
room_list.append(room)
room = ["You are on the Balcony", None, None, 5, None]
room_list.append(room)
current_room = 0
last_room = 0
Done = False
print("Your goal is to make it to the balcony and escape")
print("Try your best and don't die")
Small_Key = []
while not Done:
    print(room_list[current_room][0])
    bing = input("Type N,E,W,S as the direction you want to go or type y for yes and n for no to interact or B to view your Backpack and Q to quit")
    print()

    # NORTH
    if bing.lower() == "n" or bing.lower() == "north":
        last_room = current_room
        next_room = room_list[current_room][1]
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    # EAST
    elif bing.lower() == "e" or bing.lower() == "east":
        last_room = current_room
        next_room = room_list[current_room][2]
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    # SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        last_room = current_room
        next_room = room_list[current_room][3]
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    # WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        last_room = current_room
        next_room = room_list[current_room][4]
        if next_room is None:
            print("You can't go that way")
        else:
            current_room = next_room
    elif bing.lower() == "b" or bing.lower() == "bag":
        print(bag)
    # QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        Done = True
    else:
        print("not sure you know what you are doing")

    # Medicine
    if current_room == 1:
        Rooms = input("There are drawers do you want to open them?")
        if Rooms.lower() == "y" or Rooms.lower() == "yes":
            print("you found some medicine")
            medicine = ["Medicine"]
            bag.append(medicine)
            print(" ")
        elif Rooms.lower() == "no" or Rooms.lower() == "n":
            print("you did not check the drawers")
            print(" ")
        else:
            print("that was not an option")
            Rooms = input("There are drawers do you like to open them?")
            current_room = [1]
            print(" ")
    # SMALL KEY
    elif current_room == 2:
        Rooms = input("You are in the South Hall there is a closet would you like to figure out what is inside?")
        if Rooms.lower() == "y" and bag is not Small_Key:
            print("You found a coat inside and you found a key inside the coat")
            Small_Key = ["Small_Key"]
            bag.append(Small_Key)
        elif Rooms.lower() == "y" and bag is Small_Key:
            print("You already have the Small Key")
        elif Rooms.lower() == "n" or Rooms.lower() == "no":
            print("You did not check the closet and moved on")
            print(" ")
        else:
            print("That is not an option")
            current_room = [2]
            Rooms = input("There is a closet would you like to figure out what is inside?")

    # MEAT
    elif current_room == 3:
        Rooms = input("You are in the Dining Room there is food on the plates do you want to take the food")
        if Rooms.lower() == "y" and bag is not Meat:
            print("you got a piece of meat")
            Meat = ["Meat"]
            bag.append(Meat)
            print("You have taken the food")
            print(" ")
        elif Rooms.lower() == "y" and bag is Meat:
            print("You already have the meat from this room")
        elif Rooms.lower() == "n" or Rooms.lower() == "no":
            print("you didn't grab anything off of the plates")
            print(" ")
        else:
            print("That was not an option")
            current_room = [3]
            Rooms = input("There is food on the plates do you want to take the food")
    # WOOD
    elif current_room == 4:
        Rooms = input("You have found your self in Bedroom 1 you see some broken wood and you think you might be able to break it")
        if Rooms.lower() == "y" and bag is medicine or Rooms.lower() == "yes" and bag is medicine:
            print("You used the medicine and are able to break off the wood and you got the sharpest point of the wood")
            bag.remove(medicine)
            Wood = ["Wood"]
            bag.append(Wood)
            print("You have acquired the wood")
        elif Rooms.lower() == "y" and bag is not medicine:
            print("you tried but it hurt to much and you let go")
            print(" ")
        else:
            print("you have not tried to break the wood")
            current_room = [4]
            Rooms = input("You see some broken wood and you think you might be able to break it")
            print(" ")
    # DOG AND ESCAPE ROOM
    elif current_room == 5:
        Rooms = input("you enter the North Hall and see a dog and it looks vicious would you like to see the dog")
        if Rooms.lower() == "y" and bag is Meat or Rooms.lower == "yes" and bag is Meat:
            print("You have given the dog the meat and he lets you by")
            bag.remove(Meat)
            print(" ")
        elif Rooms.lower() == "y" and bag is Large_Key:
            Rooms = input("You have found the key and gotten to the North Hall leading to the Balcony would you like to use the key and escape from this crazy house")
            if Rooms.lower() == "y" or Rooms.lower() == "yes":
                print("You win the game Conglaturations")
                Done = True
            elif Rooms.lower() == "no" or Rooms.lower() == "no":
                print("you see the ghost of the people that have lived their and they take you away")
                Done = True
            else:
                print("That was not an option")
                current_room = [5]
                Rooms = input("You have found the key and gotten to the North Hall leading to the Balcony would you like to use the key and escape from this crazy house")
        elif Rooms.lower() == "y" and bag is not Meat:
            print("you tried to get by the dog and got eaten by him but you were not strong enough and died")
            print(" ")
            Done = True
        else:
            print("you decided to not get past the dog and moved back to", last_room)
            current_room = last_room
            print(" ")
    # LARGE KEY
    elif current_room == 6:
        Rooms = input("you are in the kitchen and you see a fridge covered in ice do you open it?")
        if Rooms.lower() == "y" and bag is Wood or Rooms.lower() == "yes" and bag is Wood:
            print("You use the wood and you get rid of all of the ice and you find the key to get to the balcony")
            bag.remove(Wood)
            Large_Key = ["Large_Key"]
            bag.append(Large_Key)
            print(" ")
        elif Rooms.lower() == "y" and bag is not Wood:
            print("You tried to get rid of the ice with your own hands and you stop when they start feeling cold")
            print(" ")
        elif Rooms.lower() == "n" or Rooms.lower() == "no":
            print("you didn't try to open the fridge and wait to try later with a sharp object")
            print(" ")
        else:
            print("that was not an option")
            current_room = [6]
            Rooms = input("you are in the kitchen and you see a fridge covered in ice do you open it?")
    # YOU WIN
    if current_room == 7 and bag == Large_Key:
        print("You Win")
        Done = True
    else:
        print(" ")
print("Thanks for playing")
