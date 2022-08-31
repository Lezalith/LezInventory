# Apricot is a Usable item. 
# When used, it will take you to a label, where you can choose a fruit to transform 
# the Apricot into. Since it's a transform and not remove-then-add, it will keep it's Inventory Slot.

# Label that we'll enter by Using the Item.
label apricotLabel(selfItem):

    # All of the Menu options define a new Item that will be added.

    menu(screen = "apricotMenu"):
        "Apricot has the ability to transform into any fruit.\nIt will keep it's place in the inventory."

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

        # "Cranberries.":

        #     $ r = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "lezInventory/example_items/images/03_Cranberry.png" )

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

        "Fig.":
            $ r = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png" )

        "Plum.":
            $ r = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stacksize = 9999 )


    # Note: Similar functionality to Guava.
    python:

        # We cannot change the order of OrderedDict, which is what the Inventory is.
        # So, we'll create a list, copy stuff over there, deal with the Guava functionality, then update the OrderedDict.
        l = list(Inventory.inventory.keys())

        # Find out where the Apricot currently is.
        currentIndex = l.index(selfItem)

        # Prepare a new OrderedDict for the Inventory.
        d = OrderedDict()

        # Insert everything into the prepared OrderedDict.
        # keys are taken from the list which has had order of items changed,
        # values are taken from the original Inventory.
        for key in l:

            # Once we encounter the index where Apricot is, replace it with the selected item.
            if key == selfItem:
                d[r] = 1

            # Otherwise just copy over the info from the original Inventory.
            else:
                d[key] = Inventory.inventory[key]

        # Update Inventory to the new OrderedDict.
        Inventory.inventory = d

        # Aside from the fact that we don't want the new item selected anyway,
        # finishing of Inventory.used() will throw an error, because of not being able to remove it.
        # Unselecting it prevents this.
        Inventory.unselect()

    # Return back to the Inventory.
    return

# A custom choice screen that is used instead of the default one.
# The choices look nicer and are way smaller, since there's so many of them.
screen apricotMenu(items):

    # Still has the same style as default choice screen though
    style_prefix "choice"

    default oddItems = items[::2]
    default evenItems = items[1::2]

    # Vbox for all the buttons.
    vbox:

        align (0.5, 0.2)
        spacing 20

        for i, entry in enumerate(evenItems):

            hbox:

                spacing 20

                textbutton oddItems[i].caption action oddItems[i].action text_color "000" xsize 700
                textbutton entry.caption action entry.action text_color "000" xsize 700

        # If there was a solo item at the end
        if len(oddItems) > len(evenItems):

            hbox:

                xalign 0.5
                
                textbutton oddItems[-1].caption action oddItems[-1].action text_color "000" xsize 700

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