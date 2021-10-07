class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.reachable_rooms = {}

    def entered_room(self):
        print("You have entered the {}.".format(self.name))
        print("{}.".format(self.description))
        print("You found the following item(s): {}\n".format(", ".join(self.items)))

    def next_room(self):
        print("You can reach the following rooms: {}".format(", ".join(self.reachable_rooms.keys())))
        next_room = input("Which room would you like to enter? (Please spell it exactly how it is listed)\n")
        return next_room

    def set_reachable_rooms(self, rooms):
        self.reachable_rooms = rooms
