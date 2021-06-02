# Guava is a Usable Item.
# When used, it is placed into a random slot within the Inventory.

init -800 python:

    # randint lets us choose a random number.
    from random import randint

    # Class of the Guava.
    class Guava(UsableItem):

        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less arguments than should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(Guava, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Find out where the Item currently is.
            badIndex = InventoryObject.inventory.index(self)

            # 5 Tries to generate a different slot than the current one.
            for x in range(5):

                # Generated Index
                generated = randint( 0 , len(InventoryObject.inventory) - 1 )

                # If it's the same index as the original one, use it.
                # Otherwise, take another change.
                if not generated == badIndex:
                    break

            # Removes this Item from the Inventory...
            InventoryObject.remove()
            # ...Before inserting it in the new spot.
            InventoryObject.inventory.insert( generated , self )

    # Guava defined.
    guava = Guava( "Guava" , "Kinda random, to be honest." , "images/13_Guava.png" )