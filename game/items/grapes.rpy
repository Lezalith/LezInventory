screen grapesScreen():

    frame:

        background None
        xysize (1250, 1250)
        align (0.5, 0.5)
        padding (10, 10)
        
        at frameCC, frameAlpha

        add "images/11_Grapes_Green.png" align (0.125, 0.125) at grapesC
        add "images/11_Grapes_Green.png" align (0.5, 0.0) at grapesC
        add "images/11_Grapes_Green.png" align (0.875, 0.125) at grapesC
        add "images/11_Grapes_Green.png" align (0.0, 0.5) at grapesC
        add "images/11_Grapes_Green.png" align (1.0, 0.5) at grapesC
        add "images/11_Grapes_Green.png" align (0.125, 0.875) at grapesC
        add "images/11_Grapes_Green.png" align (0.5, 1.0) at grapesC
        add "images/11_Grapes_Green.png" align (0.875, 0.875) at grapesC

    frame:

        background None
        xysize (2000, 2000)
        align (0.5, 0.5)
        padding (10, 10)
        
        at frameC, frameAlpha

        add "images/11_Grapes_Green.png" align (0.125, 0.125) at grapesCC
        add "images/11_Grapes_Green.png" align (0.5, 0.0) at grapesCC
        add "images/11_Grapes_Green.png" align (0.875, 0.125) at grapesCC
        add "images/11_Grapes_Green.png" align (0.0, 0.5) at grapesCC
        add "images/11_Grapes_Green.png" align (1.0, 0.5) at grapesCC
        add "images/11_Grapes_Green.png" align (0.125, 0.875) at grapesCC
        add "images/11_Grapes_Green.png" align (0.5, 1.0) at grapesCC
        add "images/11_Grapes_Green.png" align (0.875, 0.875) at grapesCC


transform frameAlpha():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        easeout 1.0 alpha 0.0 yoffset 300

transform frameC():

    rotate 0.0
    linear 15.0 rotate 360.0
    linear 15.0 rotate 0.0
    repeat

transform frameCC():

    rotate 0.0
    linear 15.0 rotate -360.0
    linear 15.0 rotate 0.0
    repeat

transform grapesC():

    rotate 0.0
    linear 3.0 rotate 360.0
    linear 3.0 rotate 0.0
    repeat

transform grapesCC():

    rotate 0.0
    linear 3.0 rotate -360.0
    linear 3.0 rotate 0.0
    repeat


init -800 python:

    class Grapes(EquippableItem):

        "Class for usable Items."

        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less
            # arguments that should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(Grapes, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )


        def equipped(self):

            return renpy.show_screen("grapesScreen")

        def unequipped(self):

            return renpy.hide_screen("grapesScreen")

    grapes = Grapes( "Grapes" , "So many balls..." , "images/11_Grapes_Green.png" )