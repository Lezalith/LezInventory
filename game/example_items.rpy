
# We execute inits in the logical order: Inventory -> Items -> ...
# Lower numbers execute first. 
#
# This would be important if, for example, Items used some parts of the Inventory,
# we'd need to make sure Inventory was defined before Items.
#
# At the time of writing this comment, there are no such connections present.
# However, they are common, so I want to keep the practice going. 
#
init -850:

    # Default sets the variable when the game Start()s. As such,
    # we won't be able to call it until the game starts. This means that... -(1)-
    default Inventory = InventoryObject( (3, 3) )

    default orange = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "images/17_Orange.png" )
    default apple = Item( "Apple" , "The King of all the fruits." , "images/16_Apple.png" )

init -750 python:

    # -(1)- ...running this straight away would give us "Inventory" not defined.
    # Which is why we're only setting it up here, and we'll run this when
    # we start the game.

    def addExampleItems():
        Inventory.add(dragonFruit)
        Inventory.add(durian)
        Inventory.add(orange)
        Inventory.add(wmelon)
        Inventory.add(apple)
        Inventory.add(grapes)