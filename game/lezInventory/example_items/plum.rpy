# Plum is a Usable Item.
# When Used, its count increases by 20%, capping at it's stack_size, 9999.

init -800 python:

    # Class of the WMelon.
    class Plum(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.
        consumed_on_use = False

        # What happens when the Item is used.
        def used(self, Inventory):

            # Add (Current count / 5 + 1) Plums to the Inventory.
            Inventory.add( item = self, count = int(Inventory.inventory[self] / 5 + 1) )

# Plum defined.
default plum = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stack_size = 9999 )