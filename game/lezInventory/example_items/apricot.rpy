# Apricot is a Usable item. 
# When used, it will take you to a label, where you can choose a fruit to transform 
# the Apricot into. Since it's a transform and not remove-then-add, it will keep it's Inventory Slot.

init -800 python:    

    # Class of the Apricot.
    class Apricot(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Enter the apricot_label label defined above.
            # The function might look scary, but to us, it's like a regular call.
            # We pass it this Item, so that the label can figure out which Item to replace in the Inventory.
            return renpy.call_in_new_context("apricot_label", self_item = self)

# Apricot defined.
default apricot = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )


# Label that we'll enter by Using the Item.
label apricot_label(self_item):

    # All of the Menu options define a new Item that will be added.

    menu(screen = "apricot_menu"):
        "Apricot has the ability to transform into any fruit.\nIt will keep it's place in the inventory."

        "Durian.":
            $ r = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )

        "Apple.":
            $ r = Apple( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )

        "Orange.":
            $ r = Item( "Orange" , "Lezalith's massive stash of oranges for making juice." , image = "lezInventory/example_items/images/17_Orange.png" , stackable = True, stack_size = 2579)

        "Kiwi.":
            $ r = Item( "Kiwi" , "Great as a tea with strawberries." , "lezInventory/example_items/images/14_Kiwi.png" )

        "Strawberry.":
            $ r = Item( "Strawberry" , "Great as a tea with kiwis." , "lezInventory/example_items/images/22_Strawberry.png" )

        "Dragon fruit.":
            $ r = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )

        "Passion fruit.":
            $ r = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )

        "Plum.":
            $ r = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stack_size = 9999 )

        "Pear.":
            $ r = Pear( name = "Pear", desc = "Every bite has a different,\nbut always sweet taste.", stackable = True, stack_size = 9999,
                        images = ["lezInventory/example_items/images/18_Pear.png",
                                  "lezInventory/example_items/images/18_Pear_1.png",
                                  "lezInventory/example_items/images/18_Pear_2.png",
                                  "lezInventory/example_items/images/18_Pear_3.png",
                                  "lezInventory/example_items/images/18_Pear_4.png",
                                  "lezInventory/example_items/images/18_Pear_5.png",
                                  "lezInventory/example_items/images/18_Pear_6.png",
                                  "lezInventory/example_items/images/18_Pear_7.png",
                                  "lezInventory/example_items/images/18_Pear_8.png"] )

        "Grapefruit.":
            $ r = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )

        "Grapes.":
            $ r = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )

        "Lemon.":
            $ r = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" ) 

        "Cranberries.":
            $ r = Cranberries( "Cranberries" , "A handful of red berries." , "lezInventory/example_items/images/03_Cranberry.png" )

        "Cherries.":
            $ r = Cherries( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png", stackable = True, stack_size = 9999 )

        "Guava.":
            $ r = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )

        "Apricot.":
            $ r = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )

        "Watermelon.":
            $ r = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "lezInventory/example_items/images/23_Watermelon.png" )

        "Peach...?":
            $ r = Peach( "Peachpricot" , "An intriguing combination\nof peach and apricot.", image = "lezInventory/example_items/images/0X_Peachpricot.png" )

        "Fig.":
            $ r = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png" )


    # Note: Similar functionality to Guava.
    python:

        # We cannot change the order of OrderedDict, which is what the Inventory is.
        # So, we'll create a list, copy stuff over there, deal with the Guava functionality, then update the OrderedDict.
        l = list(inventory.inventory.keys())

        # Prepare a new OrderedDict for the Inventory.
        d = OrderedDict()

        # Insert everything into the prepared OrderedDict.
        # keys are taken from the list which has had order of items changed,
        # values are taken from the original Inventory.
        for key in l:

            # Once we encounter the index where Apricot is, replace it with the selected item.
            if key == self_item:

                d[r] = r.stack_size

            # Otherwise just copy over the info from the original Inventory.
            else:
                d[key] = inventory.inventory[key]

        # Update Inventory to the new OrderedDict.
        inventory.inventory = d

        # Aside from the fact that we don't want the new item selected anyway,
        # finishing of Inventory.used() will throw an error, because of not being able to remove it.
        # Unselecting it prevents this.
        inventory.unselect()

    # Return back to the Inventory.
    return

# A custom choice screen that is used instead of the default one.
# The choices look nicer and are way smaller, since there's so many of them.
screen apricot_menu(items):

    # Still has the same style as default choice screen though
    style_prefix "choice"

    default odd_items = items[::2]
    default even_items = items[1::2]

    # Vbox for all the buttons.
    vbox:

        align (0.5, 0.2)
        spacing 20

        for i, entry in enumerate(even_items):

            hbox:

                spacing 20

                textbutton odd_items[i].caption action odd_items[i].action text_color "000" xsize 700
                textbutton entry.caption action entry.action text_color "000" xsize 700

        # If there was a solo item at the end
        if len(odd_items) > len(even_items):

            hbox:

                xalign 0.5
                
                textbutton odd_items[-1].caption action odd_items[-1].action text_color "000" xsize 700