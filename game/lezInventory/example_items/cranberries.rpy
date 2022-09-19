# Cranberries is a a both Usable and Equippable Item.
# When equipped, it displays a message. Does nothing when unequipped.
# When used, it will show a simple screen, displaying how many times Cranberries were equipped.

init -800 python:

    # Class of the Dragon Fruit.
    class Cranberries(Item):

        # This marks the Item as equippable.
        equippable = True

        # This marks the Item as usable.
        usable = True

        # Do not remove this item on use.
        consumed_on_use = False

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # In this case we need to set up the variable that counts times equipped.
        def __init__(self, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Cranberries, self).__init__( *args, **kwargs )

            self.counter = 0

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            self.counter += 1

            # Bring up a Notify with a custom text.
            return renpy.notify("You eat one berry as you pick the cranberries up.")

        # What happens when the Item is used.
        def used(self, Inventory):

            # Show a screen.
            return renpy.show_screen("cranberries_screen")

# Cranberries defined.
default cranberries = Cranberries( "Cranberries" , "A handful of red berries." , "lezInventory/example_items/images/03_Cranberry.png" )

# Screen that we'll show by Using the Item.
# Basically the same as Dragon Fruit's screen.
screen cranberries_screen():

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)

        # Short trivia text, as well as a button to close this screen.
        vbox:
            text "You've had [cranberries.counter] cranberry berries so far!"
            textbutton "(Hide this)" action Hide("cranberries_screen") xalign 0.5