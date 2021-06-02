label passionFLabel():

    "Lezalith" "How tropical are you feeling today?"

    menu:

        "Very tropical!":

            "Lezalith" "Awesome! Have some more fruit then!"
            $ Inventory.add( passionF( "Passion Fruit" , "About as tropical as you can get." , "images/20_Passionfruit.png" ) )

        "Not tropical at all.":

            "Lezalith" "Aww. That's okay, it will come eventually!"

    return

init -800 python:

    class passionF(UsableItem):

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
            super(passionF, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        def used(self, InventoryObject):

            return renpy.call_in_new_context("passionFLabel")

    passionFruit = passionF( "Passion Fruit" , "About as tropical as you can get." , "images/20_Passionfruit.png" )