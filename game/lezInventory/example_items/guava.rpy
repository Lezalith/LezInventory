# Guava is a Usable Item.
# When used, it is placed into a random slot within the Inventory.

init -800 python:

    # randint lets us choose a random number.
    from random import randint
    from collections import OrderedDict

    # Class of the Guava.
    class Guava(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # Keep this Item in Inventory even after using it.
        consumedOnUse = False

        # What happens when the Item is used.
        def used(self, InventoryObject):

            l = list(InventoryObject.inventory.keys())

            # Find out where the Item currently is.
            badIndex = l.index(self)

            # 5 Tries to generate a different index than the current one.
            for x in range(5):

                # Generated Index
                newIndex = randint( 0 , len(InventoryObject.inventory.keys()) - 1 )

                # If it's the same index as the original one, use it.
                # Otherwise, try the roll again.
                if newIndex != badIndex:
                    break            

            l.pop(badIndex)
            l.insert(newIndex, self)

            d = OrderedDict()
            for key in l:
                d[key] = InventoryObject.inventory[key]

            InventoryObject.inventory = d
            InventoryObject.unselect()

    # Guava defined.
    guava = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )