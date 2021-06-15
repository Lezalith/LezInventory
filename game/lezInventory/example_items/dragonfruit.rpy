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
    class dragonF(lezInv.UsableItem):

        # What happens upon the definition.
        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less arguments than should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(dragonF, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Show a screen.
            return renpy.show_screen("dragonScreen")

    # Dragon Fruit defined.
    dragonFruit = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )