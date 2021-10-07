from room import Room
from exits import Exit


def initialize_castle():
    """
    :return: List of room objects
    """

    main_room = Room(name="Main Room",
                     description="""A gigantic room with many doors""",
                     items=["Umbrella", "Coat rack", "Coat"])

    library = Room(name="Library",
                   description="""There are towering bookshelves on each wall.""",
                   items=["Book"])

    secret_room = Room(name="Secret Room",
                       description=
                       """You pulled a book from one of the shelves in the library, revealing this secret room.""",
                       items=["Knife", "Skeleton", "Treasure"])

    study = Room(name="Study",
                 description="It's a quiet place to do work.",
                 items=["Pen", "Paper", "Journal"])

    armory = Room(name="Armory",
                  description="""It is stocked full of swords and shields.""",
                  items=["Sword", "Shield", "Bow", "Arrow"])

    master_room = Room(name="Master Bedroom",
                       description="""A fire is lit, keeping the bedroom warm and cozy.""",
                       items=["Bed", "Slippers", "Night Cap"])

    guest_room = Room(name="Guest Room",
                      description="""It is dusty and dark. Clearly no one has stayed here in a while.""",
                      items=[])

    kitchen = Room(name="Kitchen",
                   description="""It smells of pastries and sweets""",
                   items=["Plate", "Rolling Pin", "Flour"])

    armory_exit = Exit(name="Exit out the cellar",
                       ending="""GAME OVER.
                       You stumbled your way out of the castle by way of the wine cellar, 
                       enjoying a few bottles on the way""")

    master_exit = Exit(name="Exit out of the window",
                       ending="""GAME OVER.
                       You fell to your death while scaling down the sid eof the castle.""")

    main_exit = Exit(name="Exit out the way you came in",
                     ending="""GAME OVER.
                     You have no sense of adventure""")

    main_room.set_reachable_rooms({"Library": library, "Study": study, "Master Room": master_room,
                                   "Guest Room": guest_room, "Kitchen": kitchen, "Main exit": main_exit})
    library.set_reachable_rooms({"Main Room": main_room, "Secret Room": secret_room, "Study": study})
    study.set_reachable_rooms({"Main Room": main_room, "Library": library, "Armory": armory})
    armory.set_reachable_rooms({"Study": study, "Master Room": master_room, "Armory Exit": armory_exit})
    master_room.set_reachable_rooms({"Main Room": main_room, "Armory": armory, "Guest Room": guest_room,
                                     "Master Exit": master_exit})
    guest_room.set_reachable_rooms({"Main Room": main_room, "Master Room": master_room, "Kitchen": kitchen})
    kitchen.set_reachable_rooms({"Main Room": main_room, "Guest Room": guest_room})

    return main_room


def main():
    room = initialize_castle()
    print("You enter a castle...\n")
    while True:
        room.entered_room()

        # Check for treasure
        if "Treasure" in room.items:
            print("Congratulations you found the treasure and the game is over!!! You win!!!")
            break

        # Ask for next room
        next_room = room.next_room()
        room = room.reachable_rooms[next_room]

        if isinstance(room, Exit):
            room.print_ending()
            break


if __name__ == '__main__':
    main()
