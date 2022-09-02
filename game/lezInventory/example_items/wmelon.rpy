# Watermelon is a Usable Item.
# When Used, it randomly shuffles all of the Inventory Items and is consumed.

init -800 python:

    # Shuffle randomly shuffles a list.
    from random import shuffle
    # Inventory is an OrderedDict, we need it to recreate it.

    # Class of the WMelon.
    class WMelon(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Create a list that we can shuffle, since we cannot
            # change order of items in OrderedDict.
            l = list(Inventory.inventory.keys())

            # Shuffle the list with the items.
            shuffle(l)

            # Prepare a new OrderedDict.
            d = OrderedDict()

            # Insert everything into the prepared OrderedDict.
            # keys are taken from the list which has had order of items changed,
            # values are taken from the original Inventory.
            for key in l:
                d[key] = Inventory.inventory[key]

            # Update Inventory to the new OrderedDict.
            Inventory.inventory = d

    # Watermelon defined.
    wmelon = WMelon( "Watermelon" , "Bouncy enough to hit other items." , "lezInventory/example_items/images/23_Watermelon.png" )