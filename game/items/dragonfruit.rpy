screen dragonScreen():

    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)
        
        at dragonTrans

        vbox:
            text "Did you know that Dragon Fruit is actually called Pitahaya?"
            textbutton "Glad to know!" action Hide("dragonScreen") xalign 0.5

transform dragonTrans():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

init -800 python:

    class dragonF(UsableItem):

        "Class for a Hemlet."

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
            super(dragonF, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self):

            return renpy.show_screen("dragonScreen")

    dragonFruit = dragonF( "Dragon Fruit" , "White as snow on the inside." , "images/07_Dragonfruit.png" )