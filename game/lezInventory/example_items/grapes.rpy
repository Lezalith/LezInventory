# Grapes are an Equippable Item.
# When equipped, a screen will appear with all kinds of confusion.
# When unequipped, it will hide the screen again.

init -800 python:

    # Class of the Grapes.
    class Grapes(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Show the grapes_screen screen.
            return renpy.show_screen("grapes_screen")

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Hide the grapes_screen screen.
            return renpy.hide_screen("grapes_screen")

# Grapes defined.
default grapes = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )
    

# Screen that we'll show by Using the Item.
screen grapes_screen():

    # Inner frame of the Balls.
    frame:

        background None
        xysize (1250, 1250)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move counter-clockwise,
        # as well as a transform for smooth appear and disappear
        at frame_CC, frame_alpha

        # All the different Balls, spinning clockwise themselves.
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.125) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 0.0) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.125) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.0, 0.5) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (1.0, 0.5) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.875) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 1.0) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.875) at grapes_C

    # Outer frame of the Balls.
    frame:

        background None
        xysize (2000, 2000)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move clockwise,
        # as well as a transform for smooth appear and disappear
        at frame_C, frame_alpha

        # All the different Balls, spinning counter-clockwise themselves.
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.125) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 0.0) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.125) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.0, 0.5) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (1.0, 0.5) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.875) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 1.0) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.875) at grapes_CC

# Transform for smooth appear and disappear
transform frame_alpha():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        easeout 1.0 alpha 0.0 yoffset 300

# Clockwise spin on a frame
transform frame_C():

    rotate 0.0
    linear 15.0 rotate 360.0
    linear 15.0 rotate 0.0
    repeat

# Counter-clockwise spin on a frame
transform frame_CC():

    rotate 0.0
    linear 15.0 rotate -360.0
    linear 15.0 rotate 0.0
    repeat

# Clockwise spin on a grape
transform grapes_C():

    rotate 0.0
    linear 3.0 rotate 360.0
    linear 3.0 rotate 0.0
    repeat

# Counter-clockwise spin on a grape
transform grapes_CC():

    rotate 0.0
    linear 3.0 rotate -360.0
    linear 3.0 rotate 0.0
    repeat