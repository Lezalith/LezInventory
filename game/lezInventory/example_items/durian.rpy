# Durian is an Equippable Item.
# While Equipped, there is a dark green overlay over the player's screen.

init -800 python:

    # Class of the Durian.
    class Durian(EquippableItem):

        # What happens upon the definition.
        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less arguments than should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(Durian, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Show a Solid color over the entire screen, with 33% opacity.
            return renpy.show( "NoTag", layer = "screens", zorder = 20, what = Solid( "32CD3233" ) , tag = "durTag" )

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Remove the Solid color.
            return renpy.hide("durTag", "screens")

    # Durian defined.
    durian = Durian( "Durian" , "World's smelliest fruit, supposedly." , "inventory/example_items/images/08_Durian.png" )