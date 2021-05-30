init -800 python:

    from random import shuffle

    class Guava(UsableItem):

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
            super(Guava, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self):

            badIndex = Inventory.inventory.index(self)

            # 5 Tries to generate a different slot than the current one.
            for x in range(5):

                generated = randint( 0 , len(Inventory.inventory) - 1 )

                if not generated == badIndex:
                    break

            Inventory.remove()
            Inventory.inventory.insert( generated , self )

    guava = Guava( "Guava" , "Kinda random, to be honest." , "images/13_Guava.png" )