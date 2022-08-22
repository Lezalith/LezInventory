# Plum is a Usable Item.
# When Used, its stack doubles, capping at it's stacksize, 264.

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

            InventoryObject.add( Item = self, count = InventoryObject.inventory[self] )

    # Watermelon defined.
    plum = Plum( "Plum" , "Evergrowing in power,\ndark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stacksize = 264 )