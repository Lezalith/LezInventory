init -800 python:

    class Apple(EquippableItem):

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
            super(Apple, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )


        def equipped(self, InventoryObject):

            return renpy.notify("I have been crowned the King of all Fruits!")

        def unequipped(self, InventoryObject):

            return renpy.notify("Long live the king...")

    apple = Apple( "Apple" , "The King of all the fruits." , "images/16_Apple.png" )