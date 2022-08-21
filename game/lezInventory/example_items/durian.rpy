# Durian is an Equippable Item.
# While Equipped, there is a dark green overlay over the player's screen.

init -800 python:

    # Class of the Durian.
    class Durian(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as Apple doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Show a Solid color over the entire screen, with 33% opacity.
            return renpy.show( "NoTag", layer = "screens", zorder = 20, what = Solid( "32CD3233" ) , tag = "durTag" )

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Remove the Solid color.
            return renpy.hide("durTag", "screens")

    # Durian defined.
    durian = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )