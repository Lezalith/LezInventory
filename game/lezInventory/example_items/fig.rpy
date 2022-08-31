# Fig is an equippable Item.
# Equipping it will bring up a screen, hinting at the fact that it will be consumed upon being unequipped.

# Overlay to darken Inventory behind the frame.
define figOverlay = At( Solid("000"), Transform(alpha = 0.5) )

# Screen shown when the Item is equipped.
screen figScreen():

    # Add the overlay.
    add figOverlay

    # Frame in the middle of the screen
    frame:

        align (0.5, 0.5)
        padding (10, 10)

        vbox:
            text "As you bite into the fig, a sweet taste fills your mouth."
            text "Savour the flavour while you can!"
    
    # So that player cannot interact with stuff below this screen.
    modal True

    # Hide the screen on click.
    key "dismiss" action Hide("figScreen")

init -800 python:

    # Class of the Dragon Fruit.
    class Fig(Item):

        # This marks the Item as equippable.
        equippable = True

        # Remove the Item once it's unequipped.
        consumedOnUnequip = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is equipped.
        def equipped(self, InventoryObject):

            # Show the screen.
            return renpy.show_screen("figScreen")

        # What happens when the Item is unequipped.
        def unequipped(self, InventoryObject):

            # Message showing the removal.
            return renpy.notify("The flavour fades away...")

    # Fig defined.
    fig = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png" )