import random
import pyfiglet
from room import Room
from character import Enemy, Friend, Inventory
from item import Key, Chest, Goldcoins, Goldencrown

class Game:
    def __init__(self):
        self.current_room = None
        self.kitchen = None
        self.wolf = None
        self.run_attempt_failed = False  #* Track whether running away failed
        self.inventory = Inventory()

    def setup_game(self):
        #* Create and link rooms
        self.kitchen, ballroom, dining_room, hidden_room, overworld = self.create_rooms()
        self.overworld = overworld

        #* Set initial room
        self.current_room = self.kitchen

        #* Create and place characters and items
        self.setup_characters_and_items(dining_room, ballroom, hidden_room)

        #* Print available commands
        self.print_available_commands()

    def create_rooms(self):
        #* Create rooms
        kitchen = Room("Kitchen")
        ballroom = Room("Ballroom")
        dining_room = Room("Dining Room")
        hidden_room = Room("Hidden Room")
        overworld = Room("Overworld")

        #* Set room descriptions
        kitchen.set_description("A cozy, dimly lit kitchen filled with an assortment of ingredients.")
        ballroom.set_description("A bright, colorful ballroom with large windows overlooking the garden.")
        dining_room.set_description("A grand, opulent dining room with high ceilings and ornate chandeliers.")
        hidden_room.set_description("A dark, smoky room filled with dusty tomes and ancient artifacts. There is a chest in the center of the room.")
        overworld.set_description("A vast, open field stretching as far as the eye can see. This is the end of your journey.") 

        #* Link rooms
        kitchen.link_room(dining_room, "south")
        dining_room.link_room(kitchen, "north")
        dining_room.link_room(ballroom, "west")
        ballroom.link_room(dining_room, "east")
        dining_room.link_room(hidden_room, "south")
        hidden_room.link_room(dining_room, "north")
        ballroom.link_room(overworld, "west") 
        overworld.link_room(ballroom, "east")  

        return kitchen, ballroom, dining_room, hidden_room, overworld 
    
    def setup_characters_and_items(self, dining_room, ballroom, hidden_room):
        #* Create characters
        self.wolf = Enemy("Wolf", "A wild, peculiar creature with eerie, blue eyes.")
        self.wolf.set_conversation("Howl!")
        self.wolf.set_weakness("silver sword")
        dining_room.set_character(self.wolf)

        friendly_npc = Friend()
        ballroom.set_character(friendly_npc)

        #* Create items and add to rooms
        chest = Chest()
        key = Key()
        hidden_room.add_item(chest)

    def print_available_commands(self):
        #* Print available commands
        print("\n\033[1;37mAvailable commands (All in lowercase :) ):")
        print("\n- talk: Initiate a conversation with the character in the room.")
        print("- fight: Engage in a battle with the character in the room.")
        print("- run away: Attempt to escape from the character in the room.")
        print("- north, south, east, west: Move to the adjacent room in the specified direction.")
        print("- open: Attempt to open chest in hidden room.")
        print("- inventory: To view player's inventory.\033[0m")

    def move_player(self, direction):
        next_room = self.current_room.move(direction)
        if next_room:
            self.current_room = next_room

            #* Check if the player has entered the Overworld room
            if self.current_room == self.overworld:
                print()
                self.current_room.get_details()
                end = pyfiglet.figlet_format("The  End ", font="caligraphy", width=400)
                print("\033[1;36m"+ end +"\033[0m")
                exit()  #* End the game
        else:
            print("You can't go that way.")

    def run_away(self):
        #! 50% chance to succeed
        if random.choice([True, False]):
            print(f"\nYou successfully ran away from the wolf!\n\033[1;46mHint: The wolf is weak to a {self.wolf.weakness}.\033[0m\n")
            self.current_room = self.kitchen  
            self.run_attempt_failed = False  
        else:
            print("\033[1;31mYou tried to run away, but the wolf caught up with you!\033[0m")
            self.run_attempt_failed = True  

    def fight(self):
        print("What will you fight with?")
        fight_with = input().strip().lower()
        self.wolf.fight(fight_with)

        #* If the character is defeated, remove them from the room and display a victory message.
        if self.wolf.is_defeated():
            self.current_room.remove_character(self.wolf)
            victory = pyfiglet.figlet_format("You   have   slain   the   wolf  !", font="Standard", width=200)
            print("\033[1;32m" + victory + "\033[0m")
            print("You can now move freely in the room.")

            #* Add the key to the inventory
            key = Key()
            self.current_room.add_item(key)
            self.inventory.add_item(key)
            print("\033[1;33mYou have received a key!\033[0m")

    #* Allows for user to use other commands 
    def process_command(self, command):
        if command == "inventory":
            print("Your inventory:")
            for item in self.inventory.get_items():
                print("- " + item.name)
        elif command == "open":
            if self.current_room.name.lower() == "hidden room":
                if "key" in [item.name.lower() for item in self.inventory.get_items()]:
                    chest = [item for item in self.current_room.get_items() if isinstance(item, Chest)]
                    if chest:
                        print("You have opened the chest!")
                        print("\033[1;33mYou have received 100 gold coins and a golden crown!\033[0m")
                        self.current_room.remove_item(chest[0])
                        self.inventory.add_item(Goldcoins(100))
                        self.inventory.add_item(Goldencrown())
                    else:
                        print("There is no chest in this room.")
                else:
                    print("You do not have a key.")
            else:
                print("You can't open the chest here.")
        else:
            print("Invalid command.")

    def game_loop(self):
        #* Main Game Loop
        while True:
            print("\n")
            self.current_room.get_details()
            inhabitant = self.current_room.get_character()

            if inhabitant is not None:
                #* If it's the Wolf (Enemy), force a fight or run
                if isinstance(inhabitant, Enemy) and inhabitant.name.lower() == "wolf":
                    print("\nYou are face to face with the Wolf! You cannot move until you deal with the wolf.")
                    if self.run_attempt_failed:
                        print("You cannot run away again. You must fight the wolf!")
                        command = "fight"  #* Force the player to fight
                    else:
                        print("Options: fight or run away.")
                        command = input("> ").strip().lower()

                    if command == "run away":
                        self.run_away()
                    elif command == "fight":
                        self.fight()  
                    else:
                        print("Invalid command. You must fight or run away!")

                #* If it's a Friendly NPC
                elif isinstance(inhabitant, Friend):
                    inhabitant.describe()
                    command = input("> ").strip().lower()

                    if command == "talk":
                        inhabitant.talk() 
                        print("You can now move or perform other actions.")
                        self.current_room.remove_character(inhabitant) 
                    else:
                        print("Invalid command. You should talk to the owl.")
                        continue

            else:
                #* No character in the room, allow free movement or other actions
                command = input("> ").strip().lower()

                if command in ["north", "south", "east", "west"]:
                    self.move_player(command)
                else:
                    self.process_command(command)


#* Start the game
game = Game()
game.setup_game()
game.game_loop()
