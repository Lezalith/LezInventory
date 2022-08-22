# Apricot is a Usable item. 
# When used, it will take you to a label, where you can choose a fruit to transform 
# the Apricot into. Since it's a transform and not remove-then-add, it will keep it's Inventory Slot.

# TODO: FIX

# Label that we'll enter by Using the Item.
label apricotLabel(selfItem):

    # All of the Menu options replaces the current Item with the selected one,
    # before Unselecting it, so it is then not removed by the Inventory.

    menu(screen = "apricotMenu"):
        "You can transform Apricot into any fruit.\nIt will keep it's place in the inventory."

        "Durian.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )

        "Grapes.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )

        "Lemon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" ) 

        "Apple.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )

        "Cherries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png" )

        "Orange.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "lezInventory/example_items/images/17_Orange.png" )

        "Cranberries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "lezInventory/example_items/images/03_Cranberry.png" )

        "Kiwi.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Kiwi" , "Great as a tea with strawberries." , "lezInventory/example_items/images/14_Kiwi.png" )

        "Strawberry.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Strawberry" , "Great as a tea with kiwis." , "lezInventory/example_items/images/22_Strawberry.png" )

        "Dragon fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )

        "Guava.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )

        "Apricot.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )

        "Watermelon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "lezInventory/example_items/images/23_Watermelon.png" )

        "Passion fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )

        "Grapefruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )

        "Peach...?":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Peach( "Peachpricot" , "An intriguing combination\nof peach and apricot.", image = "lezInventory/example_items/images/0X_Peachpricot.png" )

    # After the transform, the new Item stays selected.
    # Unselecting it prevents it from being consumed when this function is finished.
    $ Inventory.unselect()

    # Return back to the Inventory.
    return

# A custom choice screen that is used instead of the default one,
# since there are too many items for the default one to display all of them.
screen apricotMenu(items):

    # Still has the same style as default choice screen though
    style_prefix "choice"

    default oddItems = items[::2]
    default evenItems = items[1::2]

    vbox:

        align (0.5, 0.2)
        spacing 20

        for i, entry in enumerate(oddItems):

            hbox:

                spacing 20

                textbutton entry.caption action entry.action text_color "000" xsize 700
                textbutton evenItems[i].caption action evenItems[i].action text_color "000" xsize 700

        # If there was a solo item at the end
        if len(evenItems) > len(oddItems):

            hbox:

                xalign 0.5
                
                textbutton evenItems[-1].caption action evenItems[-1].action text_color "000" xsize 700

init -800 python:    

    # Class of the Apricot.
    class Apricot(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Enter the apricotLabel label defined above.
            # The function might look scary, but to us, it's like a regular call.
            # We pass it this Item, so that the label can figure out which Item to replace in the Inventory.
            return renpy.call_in_new_context("apricotLabel", selfItem = self)

    # Apricot defined.
    apricot = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )