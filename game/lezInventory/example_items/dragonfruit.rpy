# Dragon Fruit is a Usable Item.
# When used, it will show a simple screen with some trivia.

init -800 python:

    # Class of the Dragon Fruit.
    class dragonF(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Show a screen.
            return renpy.show_screen("dragon_screen")

# Dragon Fruit defined.
default dragonFruit = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png")

# Screen that we'll show by Using the Item.
screen dragon_screen():

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)

        # Short trivia text, as well as a button to close this screen.
        vbox:
            text "Did you know that Dragon Fruit is actually called Pitahaya?"
            textbutton "Glad to know!" action Hide("dragon_screen") xalign 0.5
