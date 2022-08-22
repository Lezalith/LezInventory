# Watermelon is a Usable Item.
# When Used, it randomly shuffles all of the Inventory Items.

# TODO: FIX

init -800 python:

    # Shuffle randomly shuffles a list.
    from random import shuffle
    from collections import OrderedDict

    # Class of the WMelon.
    class WMelon(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            l = list(InventoryObject.inventory.keys())

            shuffle(l)

            d = OrderedDict()
            for key in l:
                d[key] = InventoryObject.inventory[key]

            InventoryObject.inventory = d

    # Watermelon defined.
    wmelon = WMelon( "Watermelon" , "Bouncy enough to hit other items." , "lezInventory/example_items/images/23_Watermelon.png" )