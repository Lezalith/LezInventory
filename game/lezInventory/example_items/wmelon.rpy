# Watermelon is a Usable Item.
# When Used, it randomly shuffles all of the Inventory Items.

# TODO: FIX

init -800 python:

    # Shuffle randomly shuffles a list.
    from random import shuffle

    # Class of the WMelon.
    class WMelon(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Randomly shuffle the list.
            shuffle(Inventory.inventory)

            # Set this Item as selected again,
            # so rest of Inventory code can be executed properly.
            Inventory.selectedSlot = Inventory.inventory.index( self )

    # Watermelon defined.
    wmelon = WMelon( "Watermelon" , "Bouncy enough to hit other items." , "lezInventory/example_items/images/23_Watermelon.png" )