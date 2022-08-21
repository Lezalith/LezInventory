# Apple is an Equippable Item.
# When equipped, it will show a message.
# When unequipped, it will show a different message.

init -800 python:

    # Class of the Apple.
    class Apple(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Create a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Create a Notify with a custom text.
            return renpy.notify("Long live the king...")

    # Apple defined.
    apple = Apple( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )