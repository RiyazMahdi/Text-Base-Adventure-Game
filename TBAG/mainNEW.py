import pyfiglet
from room import Room
from character import Enemy, Friend, Inventory
from item import Key, Chest, Goldcoins, Goldencrown

class Game:
    def __init__(self):
        self.current_room = None
        self.inventory = Inventory()
        self.chest = None  # Define chest as an instance variable
        self.wolf = None   # Define the wolf as an instance variable
        self.setup_game()

    def setup_game(self):
        #* Create and link rooms
        kitchen, ballroom, dining_room, hidden_room, overworld = self.create_rooms()

        #* Set initial room
        self.kitchen = kitchen
        self.current_room = kitchen
        self.overworld = overworld

        #* Create characters and items
        self.wolf = Enemy("Wolf", "A wild, peculiar creature with eerie, blue eyes.")
        self.wolf.set_conversation("Howl!")
        self.wolf.set_weakness("silver sword")
        dining_room.set_character(self.wolf)

        friendly_npc = Friend()
        ballroom.set_character(friendly_npc)

        self.chest = Chest()  # Store chest as an instance variable
        hidden_room.add_item(self.chest)

        # Create key, gold coins, and golden crown as instance variables
        self.key = Key()
        self.gold_coins = Goldcoins(100)
        self.golden_crown = Goldencrown()

        #* Display available commands
        self.print_commands()

    def create_rooms(self):
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
        overworld.set_description("A vast, open field stretching as far as the eye can see.")

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

    def print_commands(self):
        print("\n\033[1;37mAvailable commands (All in lowercase :) ):")
        print("\n- talk: Initiate a conversation with the character in the room.")
        print("- fight: Engage in a battle with the character in the room.")
        print("- run away: Attempt to escape from the character in the room.")
        print("- north, south, east, west: Move to the adjacent room in the specified direction.")
        print("- open: Attempt to open chest in hidden room.")
        print("- inventory: To view player's inventory.\033[0m\n")

    def play(self):
        while True:
            self.current_room.get_details()
            inhabitant = self.current_room.get_character()

            if inhabitant:
                inhabitant.describe()
                inhabitant.talk()

            command = input("> ").strip().lower()
            print()
            self.process_command(command, inhabitant)

    def process_command(self, command, inhabitant):
        if command in ["north", "south", "east", "west"]:
            self.move_player(command)
        elif command == "talk" and inhabitant:
            inhabitant.talk()
        elif command == "fight" and inhabitant:
            self.fight_enemy(inhabitant)
        elif command == "run away":
            self.run_away()
        elif command == "inventory":
            self.show_inventory()
        elif command == "open":
            self.open_chest()
        else:
            print("Invalid command.")

    def move_player(self, direction):
        next_room = self.current_room.move(direction)
        if next_room:
            self.current_room = next_room

            # Check if the player has entered the Overworld room
            if self.current_room == self.overworld:
                end = pyfiglet.figlet_format("The  End ", font="caligraphy", width=400)
                print("\033[1;36m"+ end +"\033[0m")
                exit()  # End the game
        else:
            print("You can't go that way.")

    def fight_enemy(self, enemy):
        print("What will you fight with?")
        fight_with = input("> ").strip().lower()
        result = enemy.fight(fight_with)

        if result:
            self.current_room.remove_character(enemy)
            victory = pyfiglet.figlet_format("You   have   slain   the   wolf  !", font="Standard", width=200)
            print("\033[1;32m" + victory + "\033[0m")
            print("You can now move freely in the room.")

            self.current_room.add_item(self.key)
            self.inventory.add_item(self.key)
            print("\033[1;33mYou have received a key!\033[0m\n")

    def run_away(self):
        if self.current_room.get_character() == self.wolf:
            print(f"You successfully ran away from the wolf\n\033[1;46mHint: The wolf is weak to a {self.wolf.weakness}.\033[0m\n")
            self.current_room = self.kitchen  # Correctly change to kitchen
        else:
            print("There's nothing to run away from.\n")

    def show_inventory(self):
        print("Your inventory:")
        for item in self.inventory.get_items():
            print(f"- {item.name}\n")

    def open_chest(self):
        if self.current_room.name.lower() == "hidden room":
            if "key" in [item.name.lower() for item in self.inventory.get_items()]:
                if self.chest in self.current_room.get_items():
                    print("You have opened the chest!")
                    print("\033[1;33mYou have received 100 gold coins and a golden crown!\033[0m")
                    self.current_room.remove_item(self.chest)
                    self.inventory.remove_item(self.key)
                    self.inventory.add_item(self.gold_coins)
                    self.inventory.add_item(self.golden_crown)
                else:
                    print("There is no chest in this room.\n")
            else:
                print("You do not have a key.\n")
        else:
            print("You can't open the chest here.\n")

if __name__ == "__main__":
    game = Game()
    game.play()
