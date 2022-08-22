# Plum is a Usable Item.
# When Used, its stack doubles, capping at it's stacksize, 9999.

# TODO: FIX

init -800 python:

    # Class of the WMelon.
    class Plum(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.
        consumedOnUse = False

        # What happens when the Item is used.
        def used(self, InventoryObject):

            InventoryObject.add( Item = self, count = InventoryObject.inventory[self] / 5 + 1 )

            # if InventoryObject.inventory[self] >= self.stackSize:
            #     InventoryObject.inventory[self] = 1

    # Watermelon defined.
    plum = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stacksize = 9999 )