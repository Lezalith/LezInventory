# Plum is a Usable Item.
# When Used, its count increases by 20%, capping at it's stacksize, 9999.

init -800 python:

    # Class of the WMelon.
    class Plum(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.
        consumedOnUse = False

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Add (Current count / 5 + 1) Plums to the Inventory.
            InventoryObject.add( item = self, count = int(InventoryObject.inventory[self] / 5 + 1) )

    # Watermelon defined.
    plum = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stacksize = 9999 )