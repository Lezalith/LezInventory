# Durian is an Equippable Item.
# While Equipped, there is a dark green overlay image displayed over the screen.

init -800 python:

    # Class of the Durian.
    class Durian(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Show a Solid color over the entire screen.
            return renpy.show( "NoTag", layer = "screens", zorder = 20, what = Solid( "32CD3233" ) , tag = "durTag", at_list = [ Transform(alpha = 0.33) ] )

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Remove the Solid color.
            return renpy.hide("durTag", "screens")

    # Durian defined.
    durian = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )