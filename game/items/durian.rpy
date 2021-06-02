init -800 python:

    class Durian(EquippableItem):

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
            super(Durian, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )


        def equipped(self, InventoryObject):

            return renpy.show( "NoTag", layer = "screens", zorder = 20, what = Solid( "32CD3233" ) , tag = "durTag" )

        def unequipped(self, InventoryObject):

            return renpy.hide("durTag", "screens")

    durian = Durian( "Durian" , "World's smelliest fruit, supposedly." , "images/08_Durian.png" )