# Guava is a Usable Item.
# When used, it is placed into a random slot within the Inventory.

init -800 python:

    # randint lets us choose a random number.
    from random import randint

    # Class of the Guava.
    class Guava(Item):

        # This marks the Item as usable.
        usable = True

        # Item removed after being used.
        consumedOnUse = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Find out where the Item currently is.
            badIndex = InventoryObject.inventory.index(self)

            # 5 Tries to generate a different slot than the current one.
            for x in range(5):

                # Generated Index
                generated = randint( 0 , len(InventoryObject.inventory) - 1 )

                # If it's the same index as the original one, use it.
                # Otherwise, try the roll again.
                if not generated == badIndex:
                    break

            # Removes this Item from the Inventory...
            InventoryObject.remove()
            # ...Before inserting it in the new spot.
            InventoryObject.inventory.insert( generated , self )

    # Guava defined.
    guava = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )