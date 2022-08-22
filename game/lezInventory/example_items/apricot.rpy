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

            $ r = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )

        "Grapes.":

            $ r = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )

        "Lemon.":

            $ r = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" ) 

        "Apple.":

            $ r = Item( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )

        "Cherries.":

            $ r = Item( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png" )

        "Orange.":

            $ r = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "lezInventory/example_items/images/17_Orange.png" )

        "Cranberries.":

            $ r = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "lezInventory/example_items/images/03_Cranberry.png" )

        "Kiwi.":

            $ r = Item( "Kiwi" , "Great as a tea with strawberries." , "lezInventory/example_items/images/14_Kiwi.png" )

        "Strawberry.":

            $ r = Item( "Strawberry" , "Great as a tea with kiwis." , "lezInventory/example_items/images/22_Strawberry.png" )

        "Dragon fruit.":

            $ r = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )

        "Guava.":

            $ r = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )

        "Apricot.":

            $ r = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )

        "Watermelon.":

            $ r = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "lezInventory/example_items/images/23_Watermelon.png" )

        "Passion fruit.":

            $ r = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )

        "Grapefruit.":

            $ r = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )

        "Peach...?":

            $ r = Peach( "Peachpricot" , "An intriguing combination\nof peach and apricot.", image = "lezInventory/example_items/images/0X_Peachpricot.png" )


    python:

        l = list(Inventory.inventory.keys())

        currentIndex = l.index(selfItem)

        d = OrderedDict()
        for key in l:

            if key == selfItem:
                d[r] = 1

            else:
                d[key] = Inventory.inventory[key]

        Inventory.inventory = d

    # Apricot is still selected, and finishing up of Inventory.used() will throw an error,
    # because of not being able to remove it.
    # Unselecting it prevents this.
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