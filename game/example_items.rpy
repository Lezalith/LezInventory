
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

init -849:

    define helmet = Item( "Iron Helmet" , "Keeps your head safe." )
    define helmetEQ = EquippableItem( "Iron Helmet EQ" , "Keeps your head safe EQ." , "images/tile001.png")
    define cowl = Item( "Leather Cowl" , "Covers your face." , "images/tile014.png" )
    define cowlUS = UsableItem( "Leather Cowl US" , "Covers your face US." , "images/tile014.png" )
    define silverCrown = Item( "Silver Crown" , "A valuable crown." , "images/tile018.png" )
    define goldenCrown = Item( "Golden Crown" , "A very valuable crown." , "images/tile020.png" )
    define amulet = Item( "Magic Amulet" , "Holds magic properties." , "images/tile023.png" )
    define boots = Item( "Leather Boots" , "Tough boots." , "images/tile033.png" )
    define tunic = Item( "Cloth Tunic" , "A simple tunic." , "images/tile048.png" )

init -848 python:

    # -(1)- ...running this straight away would give us "Inventory" not defined.
    # Which is why we're only setting it up here, and we'll run this when
    # we start the game.

    def addExampleItems():
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(helmet)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(cowl)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(silverCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(amulet)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(boots)
        Inventory.add(tunic)
        Inventory.add(tunic)
        Inventory.add(tunic)
        Inventory.add(tunic)