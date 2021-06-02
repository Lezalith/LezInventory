# Grapes are an Equippable Item.
# When equipped, a screen will appear with all kinds of confusion.
# When unequipped, it will hide the screen again.

# Screen that we'll show by Using the Item.
screen grapesScreen():

    # Inner frame of the Balls.
    frame:

        background None
        xysize (1250, 1250)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move counter-clockwise,
        # as well as a transform for smooth appear and disappear
        at frameCC, frameAlpha

        # All the different Balls, spinning clockwise themselves.
        add "images/11_Grapes_Green.png" align (0.125, 0.125) at grapesC
        add "images/11_Grapes_Green.png" align (0.5, 0.0) at grapesC
        add "images/11_Grapes_Green.png" align (0.875, 0.125) at grapesC
        add "images/11_Grapes_Green.png" align (0.0, 0.5) at grapesC
        add "images/11_Grapes_Green.png" align (1.0, 0.5) at grapesC
        add "images/11_Grapes_Green.png" align (0.125, 0.875) at grapesC
        add "images/11_Grapes_Green.png" align (0.5, 1.0) at grapesC
        add "images/11_Grapes_Green.png" align (0.875, 0.875) at grapesC

    # Outer frame of the Balls.
    frame:

        background None
        xysize (2000, 2000)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move clockwise,
        # as well as a transform for smooth appear and disappear
        at frameC, frameAlpha

        # All the different Balls, spinning counter-clockwise themselves.
        add "images/11_Grapes_Green.png" align (0.125, 0.125) at grapesCC
        add "images/11_Grapes_Green.png" align (0.5, 0.0) at grapesCC
        add "images/11_Grapes_Green.png" align (0.875, 0.125) at grapesCC
        add "images/11_Grapes_Green.png" align (0.0, 0.5) at grapesCC
        add "images/11_Grapes_Green.png" align (1.0, 0.5) at grapesCC
        add "images/11_Grapes_Green.png" align (0.125, 0.875) at grapesCC
        add "images/11_Grapes_Green.png" align (0.5, 1.0) at grapesCC
        add "images/11_Grapes_Green.png" align (0.875, 0.875) at grapesCC

# Transform for smooth appear and disappear
transform frameAlpha():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        easeout 1.0 alpha 0.0 yoffset 300

# Clockwise spin on a frame
transform frameC():

    rotate 0.0
    linear 15.0 rotate 360.0
    linear 15.0 rotate 0.0
    repeat

# Counter-clockwise spin on a frame
transform frameCC():

    rotate 0.0
    linear 15.0 rotate -360.0
    linear 15.0 rotate 0.0
    repeat

# Clockwise spin on a grape
transform grapesC():

    rotate 0.0
    linear 3.0 rotate 360.0
    linear 3.0 rotate 0.0
    repeat

# Counter-clockwise spin on a grape
transform grapesCC():

    rotate 0.0
    linear 3.0 rotate -360.0
    linear 3.0 rotate 0.0
    repeat


init -800 python:

    # Class of the Grapes.
    class Grapes(EquippableItem):

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
            super(Grapes, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )


        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Show the grapesScreen screen.
            return renpy.show_screen("grapesScreen")

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Hide the grapesScreen screen.
            return renpy.hide_screen("grapesScreen")

    # Grapes defined.
    grapes = Grapes( "Grapes" , "So many balls..." , "images/11_Grapes_Green.png" )