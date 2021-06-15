# Grapefruit is a Usable Item.
# When used, it will delete all of the Inventory's contents.

init -800 python:

    # Class of the Grapefruit.
    class Grapefruit(UsableItem):

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
            super(Grapefruit, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):
            
            # Wipe the Inventory clean.
            InventoryObject.clear()

    # Grapefruit defined.
    grapefruit = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )