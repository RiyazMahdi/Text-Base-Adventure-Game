class Room():
    def __init__ (self, name):
        self.name = (name)
        self.description = (None)
        self.linked_rooms = {}
        self.character = None
        self.items = []

    def get_description(self):
        return self.description
    
    def set_description(self, description):
        self.description = description

    def describe(self):
        print(self.description)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(f"You are in the {self.name},")
        print("--------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is to the {direction} from here.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self
    
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def remove_character(self, character):
        self.character = None

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items

    
