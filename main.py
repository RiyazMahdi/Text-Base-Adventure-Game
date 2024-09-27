from room import Room
from character import Enemy

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_room = Room("Dining Room")

kitchen.set_description("A cozy, dimly lit kitchen filled with an assortment of ingredients.")
ballroom.set_description("A bright, colorful ballroom with large windows overlooking the garden.")
dining_room.set_description("A grand, opulent dining room with high ceilings and ornate chandeliers.")


kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
ballroom.link_room(dining_room, "east")

wolf = Enemy("Wolf", "A wild, peculiar creature with eerie, blue eyes.")
wolf.set_conversation("Howl!")
wolf.set_weakness("silver sword")

dining_room.set_character(wolf)

current_room = kitchen

print("Available commands (All in lowercase :) ):")
print("- talk: Initiate a conversation with the character in the room.")
print("- fight: Engage in a battle with the character in the room.")
print("- run away: Attempt to escape from the character in the room.")
print("- north, south, east, west: Move to the adjacent room in the specified direction.")

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        inhabitant.talk()
        command = input("> ")
        if command == "fight":
            print("What will you fight with?")
            fight_with = input()
            inhabitant.fight(fight_with)
            if inhabitant.is_defeated():
                current_room.remove_character(inhabitant)
                print("You have defeated the wolf!")
                print("You can now move freely in the room.")
                break
        elif command == "run away":
            print(f"You successfully ran away from the wolf\nHint: The wolf is weak to a {wolf.weakness}.")
            current_room = kitchen  
    else:
        command = input("> ")
        if command in ["north", "south", "east", "west"]:
            next_room = current_room.move(command)
            if next_room is not None:
                current_room = next_room
            else:
                print("You can't go that way.")
        else:
            print("Invalid command.")
 

    


    