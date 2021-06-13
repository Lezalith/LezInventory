# Passion Fruit is a Usable item.
# When used, it will take you to a label, where I personally ask you how tropical you're feeling.
# If you say very tropical, I add one more Passion Fruit into your Inventory.

# Label that we'll enter by Using the Item.
label passionFLabel():

    "Lezalith" "How tropical are you feeling today?"

    menu:

        "Very tropical!":

            "Lezalith" "Awesome! Have some more fruit then!"

            # Adds one more Passion Fruit into the Inventory.
            $ Inventory.add( passionF( "Passion Fruit" , "About as tropical as you can get." , "inventory/example_items/images/20_Passionfruit.png" ) )

        "Not tropical at all.":

            "Lezalith" "Aww. That's okay, it will come eventually!"

    # Return back to the Inventory.
    return

init -800 python:

    # Class of the Passion Fruit.
    class passionF(UsableItem):

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
            super(passionF, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

        # What happens when the Item is used.
        def used(self, InventoryObject):

            # Enter the passionFLabel label defined above.
            # The function might look scary, but to us, it's like a regular call.
            return renpy.call_in_new_context("passionFLabel")

    # Passion Fruit defined.
    passionFruit = passionF( "Passion Fruit" , "About as tropical as you can get." , "inventory/example_items/images/20_Passionfruit.png" )