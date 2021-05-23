
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

init -849 python:

    class Helmet(EquippableItem):

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
            super(Helmet, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def equipped(self):

            print("I feel safer already!")
            return renpy.notify("I feel safer already!") 

        def unequipped(self):

            print("Ahh, fresh air.") 
            return renpy.notify("Ahh, fresh air.") 

    class MagicalAmulet(UsableItem):

        "Class for usable Items."

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
            super(MagicalAmulet, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self):
            print("I think I've gained some magical properties!")
            return renpy.notify("I think I've gained some magical properties!") 
init -848:

    define helmet = Item( "Iron Helmet" , "Keeps your head safe." )
    define cowl = Item( "Leather Cowl" , "Covers your face." , "images/tile014.png" )
    define silverCrown = Item( "Silver Crown" , "A valuable crown." , "images/tile018.png" )
    define goldenCrown = Item( "Golden Crown" , "A very valuable crown." , "images/tile020.png" )
    define amulet = Item( "Magical Amulet" , "Holds magic properties." , "images/tile023.png" )
    define boots = Item( "Leather Boots" , "Tough boots." , "images/tile033.png" )
    define tunic = Item( "Cloth Tunic" , "A simple tunic." , "images/tile048.png" )

    define helmetEQ = Helmet( "Iron Helmet EQ" , "Keeps your head safe EQ." , "images/tile001.png")
    define amuletUS = MagicalAmulet( "Magical Amulet US" , "Holds magic properties." , "images/tile023.png" )

init -847 python:

    # -(1)- ...running this straight away would give us "Inventory" not defined.
    # Which is why we're only setting it up here, and we'll run this when
    # we start the game.

    def addExampleItems():
        Inventory.add(cowl)
        Inventory.add(boots)
        Inventory.add(tunic)
        Inventory.add(helmetEQ)
        Inventory.add(silverCrown)
        Inventory.add(amuletUS)
        Inventory.add(goldenCrown)
        Inventory.add(goldenCrown)
        Inventory.add(boots)
        Inventory.add(tunic)
        Inventory.add(cowl)
        Inventory.add(helmetEQ)
        Inventory.add(amuletUS)