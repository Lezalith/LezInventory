init -800 python:

    from random import shuffle

    class Grapefruit(UsableItem):

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
            super(Grapefruit, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self):
            
            Inventory.selectedSlot = None
            Inventory.equippedSlot = None
            Inventory.inventory = []
            Inventory.page = 0


    grapefruit = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "images/12_Grapefruit.png" )