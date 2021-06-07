# Apricot is a Usable item. 
# When used, it will take you to a label, where you can choose a fruit to transform 
# the Apricot into. Since it's a transform and not remove-then-add, it will keep it's Inventory Slot.

# Label that we'll enter by Using the Item.
label apricotLabel(selfItem):

    # All of the Menu options replaces the current Item with the selected one,
    # before Unselecting it, so it is then not removed by the Inventory.

    menu(screen = "apricotMenu"):
        "You can transform Apricot into any fruit. It will keep it's place in the inventory."

        "Durian.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Durian( "Durian" , "World's smelliest fruit, supposedly." , "inventory/images/08_Durian.png" )
            $ Inventory.unselect()

        "Grapes.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapes( "Grapes" , "So many balls..." , "inventory/images/11_Grapes_Green.png" )
            $ Inventory.unselect()

        "Lemon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Lemon( "Lemon" , "Not good in combination with other fruits." , "inventory/images/15_Lemon.png" ) 
            $ Inventory.unselect()

        "Apple.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Apple" , "The King of all the fruits." , "inventory/images/16_Apple.png" )
            $ Inventory.unselect()

        "Cherries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cherries" , "Spit the seeds at your foes!" , "inventory/images/01_Cherry_Red.png" )
            $ Inventory.unselect()

        "Orange.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "inventory/images/17_Orange.png" )
            $ Inventory.unselect()

        "Cranberries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "inventory/images/03_Cranberry.png" )
            $ Inventory.unselect()

        "Kiwi.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Kiwi" , "Great as a tea with strawberries." , "inventory/images/14_Kiwi.png" )
            $ Inventory.unselect()

        "Strawberry.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Strawberry" , "Great as a tea with kiwis." , "inventory/images/22_Strawberry.png" )
            $ Inventory.unselect()

        "Dragon fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = dragonF( "Dragon Fruit" , "White as snow on the inside." , "inventory/images/07_Dragonfruit.png" )
            $ Inventory.unselect()

        "Guava.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Guava( "Guava" , "Kinda random, to be honest." , "inventory/images/13_Guava.png" )
            $ Inventory.unselect()

        "Apricot.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "inventory/images/21_Apricot.png" )
            $ Inventory.unselect()

        "Watermelon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "inventory/images/23_Watermelon.png" )
            $ Inventory.unselect()

        "Passion fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = passionF( "Passion Fruit" , "About as tropical as you can get." , "inventory/images/20_Passionfruit.png" )
            $ Inventory.unselect()

        "Grapefruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "inventory/images/12_Grapefruit.png" )
            $ Inventory.unselect()

    # Return back to the Inventory.
    return

# A custom choice screen that is used instead of the default one,
# since there are too many items for the default one to display all of them.
screen apricotMenu(items):

    # Still has the same style as default choice screen though
    style_prefix "choice"

    vbox:

        # Iterates over every two items
        for x, y in pairwise(items):

            hbox:

                textbutton x.caption action x.action
                textbutton y.caption action y.action

        # If there was a solo item at the end
        if (len(items) % 2 ):

            hbox:
                xalign 0.5
                textbutton items[-1].caption action items[-1].action

init -800 python:    

    # We need this for pairwise()
    from itertools import izip

    # Lets us iterate over every two items instead of every single item.
    def pairwise(iterable):
        a = iter(iterable)
        return izip(a, a)

    # Class of the Apricot.
    class Apricot(UsableItem):

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
            super(Apricot, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Enter the apricotLabel label defined above.
            # The function might look scary, but to us, it's like a regular call.
            # We pass it this Item, so that the label can figure out which Item to replace in the Inventory.
            return renpy.call_in_new_context("apricotLabel", selfItem = self)

    # Apricot defined.
    apricot = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "inventory/images/21_Apricot.png" )