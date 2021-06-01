label apricotLabel(selfItem):

    menu(screen = "apricotMenu"):
        "You can transform Apricot into any fruit. It will keep it's place in the inventory."

        "Durian.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Durian( "Durian" , "World's smelliest fruit, supposedly." , "images/08_Durian.png" )
            $ Inventory.unselect()

        "Grapes.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapes( "Grapes" , "So many balls..." , "images/11_Grapes_Green.png" )
            $ Inventory.unselect()

        "Lemon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Lemon( "Lemon" , "Not good in combination with other fruits." , "images/15_Lemon.png" ) 
            $ Inventory.unselect()

        "Cherries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cherries" , "Spit the seeds at your foes!" , "images/01_Cherry_Red.png" )
            $ Inventory.unselect()

        "Orange.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "images/17_Orange.png" )
            $ Inventory.unselect()

        "Apple.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Apple" , "The King of all the fruits." , "images/16_Apple.png" )
            $ Inventory.unselect()

        "Cranberries.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "images/03_Cranberry.png" )
            $ Inventory.unselect()

        "Kiwi.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Kiwi" , "Great as a tea with strawberries." , "images/14_Kiwi.png" )
            $ Inventory.unselect()

        "Strawberry.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Item( "Strawberry" , "Great as a tea with kiwis." , "images/22_Strawberry.png" )
            $ Inventory.unselect()

        "Dragon fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = dragonF( "Dragon Fruit" , "White as snow on the inside." , "images/07_Dragonfruit.png" )
            $ Inventory.unselect()

        "Guava.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Guava( "Guava" , "Kinda random, to be honest." , "images/13_Guava.png" )
            $ Inventory.unselect()

        "Apricot.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "images/21_Apricot.png" )
            $ Inventory.unselect()

        "Watermelon.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "images/23_Watermelon.png" )
            $ Inventory.unselect()

        "Passion fruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = passionF( "Passion Fruit" , "About as tropical as you can get." , "images/20_Passionfruit.png" )
            $ Inventory.unselect()

        "Grapefruit.":

            $ Inventory.inventory[ Inventory.selectedSlot ] = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "images/12_Grapefruit.png" )
            $ Inventory.unselect()

    return

# TODO: Create a custom menu to display all items
screen apricotMenu(items):
    style_prefix "choice"

    vbox:

        for x, y in pairwise(items):

            hbox:

                textbutton x.caption action x.action
                textbutton y.caption action y.action

        if (len(items) % 2 ):

            hbox:
                xalign 0.5
                textbutton items[-1].caption action items[-1].action

# Grapes( "Grapes" , "So many balls..." , "images/11_Grapes_Green.png" )
# Durian( "Durian" , "World's smelliest fruit, supposedly." , "images/08_Durian.png" )
# passionF( "Passion Fruit" , "About as tropical as you can get." , "images/20_Passionfruit.png" )
# WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "images/23_Watermelon.png" )
# dragonF( "Dragon Fruit" , "White as snow on the inside." , "images/07_Dragonfruit.png" )
# Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "images/17_Orange.png" )
# Item( "Apple" , "The King of all the fruits." , "images/16_Apple.png" )

init -800 python:    

    from itertools import izip

    def pairwise(iterable):
        a = iter(iterable)
        return izip(a, a)

    class Apricot(UsableItem):

        "Class for a Hemlet."

        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less
            # arguments that should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(Apricot, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self):

            return renpy.call_in_new_context("apricotLabel", selfItem = self)

    apricot = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "images/21_Apricot.png" )