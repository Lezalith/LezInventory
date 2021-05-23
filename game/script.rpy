# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # TODO: Add Items of all types.

    python:
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(tunic)
        Inventory.add(tunic)
        Inventory.add(tunic)
        Inventory.add(tunic)

    call screen inventoryScreen

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
