from room import Room
from character import Enemy, Friend, Inventory
from item import Key, Chest, Goldcoins, Goldencrown
import pyfiglet

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_room = Room("Dining Room")
hidden_room = Room("Hidden Room")
#overworld = Room("Overworld")

kitchen.set_description("A cozy, dimly lit kitchen filled with an assortment of ingredients.")
ballroom.set_description("A bright, colorful ballroom with large windows overlooking the garden.")
dining_room.set_description("A grand, opulent dining room with high ceilings and ornate chandeliers.")
hidden_room.set_description("A dark, smoky room filled with dusty tomes and ancient artifacts.There is a chest in the center of the room")
#overworld.set_description("A vast, open field stretching as far as the eye can see.")

kitchen.link_room(dining_room, "south")
dining_room.link_room(kitchen, "north")
dining_room.link_room(ballroom, "west")
ballroom.link_room(dining_room, "east")
dining_room.link_room(hidden_room, "south")
hidden_room.link_room(dining_room, "north")
#ballroom.link_room(overworld, "west")
#overworld.link_room(ballroom, "east")

wolf = Enemy("Wolf", "A wild, peculiar creature with eerie, blue eyes.")
wolf.set_conversation("Howl!")
wolf.set_weakness("silver sword")

dining_room.set_character(wolf)
chest = Chest()
key = Key()
gold_coins = Goldcoins(100)
golden_crown = Goldencrown()
inventory = Inventory()
friendly_npc = Friend()
ballroom.set_character(friendly_npc)
hidden_room.add_item(chest)
current_room = kitchen

print("\n\033[1;37mAvailable commands (All in lowercase :) ):")
print("\n- talk: Initiate a conversation with the character in the room.")
print("- fight: Engage in a battle with the character in the room.")
print("- run away: Attempt to escape from the character in the room.")
print("- north, south, east, west: Move to the adjacent room in the specified direction.")
print("- open: Attempt to open chest in hidden room.")
print("- inventory: To view player's inventory.\033[0m")

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
                victory = pyfiglet.figlet_format("You   have   slain   the   wolf  !", font="Standard", width=200)
                print("\033[1;32m" + victory + "\033[0m")
                print("You can now move freely in the room.")
                current_room.add_item(key)
                if inventory is not None:
                    inventory.add_item(key)
                print("\033[1;33mYou have received a key!\033[0m")

        elif command == "run away":
            print(f"You successfully ran away from the wolf\n\033[1;46mHint: The wolf is weak to a {wolf.weakness}.\033[0m")
            current_room = kitchen  
        
    else:
        command = input("> ")
        if command in ["north", "south", "east", "west"]:
            next_room = current_room.move(command)
           
            if next_room is not None:
                current_room = next_room

            else:
                print("You can't go that way.")

        elif command == "inventory":
            print("Your inventory:")
            for item in inventory.get_items():
                print("- " + item.name)

        else:
            if command == "open":
                if current_room.name.lower() == "hidden room":
                    if "key" in [item.name.lower() for item in inventory.get_items()]:
                        if chest in current_room.get_items():
                            print("You have opened the chest!")
                            print("\033[1;33mYou have received 100 gold coins and a golden crown!\033[0m")
                            current_room.remove_item(chest)
                            inventory.remove_item(key)
                            inventory.add_item(gold_coins)
                            inventory.add_item(golden_crown)
                        else:
                            print("There is no chest in this room.")
                    else:
                        print("You do not have a key.")
                else:
                    print("You can't open the chest here.")
            else:
                print("Invalid command.")




    


    