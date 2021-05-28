init -800 python:

    from random import randint

    class WMelon(UsableItem):

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
            super(WMelon, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self):

            Inventory.remove()
            Inventory.inventory.insert( randint( 0 , len(Inventory.inventory) - 1 ) , self )

    wmelon = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "images/23_Watermelon.png" )