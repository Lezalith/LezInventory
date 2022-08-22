# Dragon Fruit is a Usable Item.
# When used, it will show a simple screen with some trivia.

# Screen that we'll show by Using the Item.
screen figScreen( trans ):

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)
        
        # Transition.r
        at trans

        # Short trivia text.
        text "Something Something Fig!"

    timer 3.0 action Hide("figScreen")

# Transition, for smooth appear and disappear
transform figTrans1():

    on show:
        alpha 1.0
        align (0.5, 1.0)
        yoffset 100
        
        parallel:
            linear 4.0 alpha 0.0

        parallel:
            linear 3.0 yoffset -700

transform figTrans2():

    on show:
        alpha 1.0
        align (0.0, 0.0)
        xoffset -100
        yoffset -100
        
        parallel:
            linear 4.0 alpha 0.0

        parallel:
            linear 3.0 xoffset 2000 yoffset 1000

init -800 python:

    from random import choice

    # Class of the Dragon Fruit.
    class Fig(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            t = choice( [figTrans1, figTrans2] )

            # Show a screen.
            return renpy.show_screen("figScreen", trans = t)

        # TODO: The Fig will have a cooldown between uses! ....Hopefully.
        def reload(self):
            pass

    # Dragon Fruit defined.
    fig = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png", stackable = True, stacksize = 3 )