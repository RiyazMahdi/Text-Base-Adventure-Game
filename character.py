from room import Room
import pyfiglet
class Character():
    #* Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.is_alive = True

    #* Describe the character
    def describe(self):
        print(f"A {self.name} is here!")
        print(f"{self.description}")

    #* Set the character's conversation
    def set_conversation(self, conversation):
        self.conversation = conversation

    #* Talk to the character
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print("{self.name} doesnt want to talk to you")

    #* Attempt to fight the character
    def fight(self, combat_item):
        print(f"{self.name} doesnt want to fight with you")
        return True

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness.lower():
            print(f"{self.name} has successfully been defeated!")
            self.is_alive = False
            return True
        else:
            death = pyfiglet.figlet_format(f"{self.name}    defeats    you  !", font="Standard", width=200)
            print("\033[1;31m" + death + "\033[0m")
            print("Respawning in last known location\n\033[1;46mHint:The wolf is weak to a silver sword.\033[0m")
            return False
    
    def is_defeated(self):
        return not self.is_alive

    def remove_character(self, room):
        room.remove_character(self)

class Inventory():
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def view_inventory(self):
        if len(self.items) == 0:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for item in self.items:
                print(f"- {item.name}")

    def get_items(self):
        return self.items
    
class Friend(Character):
    def __init__(self):
        super().__init__("Friendly NPC", "A majestic, wise owl with gleaming amber eyes, perched silently. ")
        self.conversation = "Greetings, traveler! I am here to congratulate on beating this game."

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print("{self.name} doesnt want to talk to you")
