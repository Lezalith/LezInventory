# Guava is a Usable Item.
# When used, it is moved into a random slot within the Inventory.

init -800 python:

    # randint lets us choose a random number.
    from random import randint
    # Inventory is an OrderedDict, we need it to recreate it.
    from collections import OrderedDict

    # Class of the Guava.
    class Guava(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # Keep this Item in Inventory even after using it.
        consumed_on_use = False

        # What happens when the Item is used.
        def used(self, Inventory):

            # We cannot change the order of OrderedDict, which is what the Inventory is.
            # So, we'll create a list, copy stuff over there, deal with the Guava functionality, then update the OrderedDict.
            l = list(Inventory.inventory.keys())

            # Find out where the Guava currently is.
            old_index = l.index(self)

            # 5 Tries to generate a different index than where it currently is.
            # Only 8 tries to not affect performance, in case we'd get REALLY unlucky.
            for x in range(8):

                # Generated Index
                new_index = randint( 0 , len(Inventory.inventory.keys()) - 1 )

                # If it's the same index as the original one, try the roll again.
                # If not, use it.
                if new_index != old_index:
                    break        

                # Keep the index if 8 rolls weren't enough.

            # Get rid of original Guava.
            l.pop(old_index)

            # Insert Guava at the generated index..
            l.insert(new_index, self)

            # Prepare a new OrderedDict for the Inventory.
            d = OrderedDict()

            # Insert everything into the prepared OrderedDict.
            # keys are taken from the list which has had order of items changed,
            # values are taken from the original Inventory.
            for key in l:
                d[key] = Inventory.inventory[key]

            # Update Inventory to the new OrderedDict.
            Inventory.inventory = d

            # Unselect the Item, since selection depends on index:
            # If the order changed, a different item would be in place and kept selected.
            Inventory.unselect()

# Guava defined.
default guava = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )