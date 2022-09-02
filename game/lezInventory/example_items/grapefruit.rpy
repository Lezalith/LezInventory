# Grapefruit is a Usable Item.
# When used, it will delete all of the Inventory's contents.

init -800 python:

    # Class of the Grapefruit.
    class Grapefruit(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):
            
            # Wipe the Inventory clean.
            Inventory.clear()

    # Grapefruit defined.
    grapefruit = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )