# Apple is an Equippable Item.
# When equipped, it will show a message.
# When unequipped, it will show a different message.

init -800 python:

    # Class of the Apple.
    class Apple(EquippableItem):

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
            super(Apple, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Create a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Create a Notify with a custom text.
            return renpy.notify("Long live the king...")

    # Apple defined.
    apple = Apple( "Apple" , "The King of all the fruits." , "inventory/images/16_Apple.png" )