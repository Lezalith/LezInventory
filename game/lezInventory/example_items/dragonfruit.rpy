# Dragon Fruit is a Usable Item.
# When used, it will show a simple screen with some trivia.

# Screen that we'll show by Using the Item.
screen dragonScreen():

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)
        
        # Transition, for smooth appear and disappear
        at dragonTrans

        # Short trivia text, as well as a button to close this screen.
        vbox:
            text "Did you know that Dragon Fruit is actually called Pitahaya?"
            textbutton "Glad to know!" action Hide("dragonScreen") xalign 0.5

# Transition, for smooth appear and disappear
transform dragonTrans():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

init -800 python:

    # Class of the Dragon Fruit.
    class dragonF(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Show a screen.
            return renpy.show_screen("dragonScreen")

    # Dragon Fruit defined.
    dragonFruit = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )