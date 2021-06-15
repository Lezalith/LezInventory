# Watermelon is a Usable Item.
# When Used, it randomly shuffles all of the Inventory Items.

init -800 python:

    # Shuffle randomly shuffles a list.
    from random import shuffle

    # Class of the WMelon.
    class WMelon(UsableItem):

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
            super(WMelon, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Randomly shuffle the list.
            shuffle(Inventory.inventory)

            # Set this Item as selected again,
            # so rest of Inventory code can be executed properly.
            Inventory.selectedSlot = Inventory.inventory.index( self )

    # Watermelon defined.
    wmelon = WMelon( "Watermelon" , "Bouncy enough to hit other items." , "lezInventory/example_items/images/23_Watermelon.png" )