# Passion Fruit is a Usable item.
# When used, it will take you to a label, where I personally ask you how tropical you're feeling.
# If you say very tropical, I add one more Passion Fruit into your Inventory.

# Label that we'll enter by Using the Item.
label passionF_label():

    "Lezalith" "How tropical are you feeling today?"

    menu:

        "Very tropical!":

            "Lezalith" "Great! I'll add some more passion fruit to your Inventory then!"

            # Adds one more Passion Fruit into the Inventory.
            $ inventory.add( passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" ) )

        "Not tropical at all.":

            "Lezalith" "Aww. That's okay, it will come to you eventually!"

    # Return back to the Inventory.
    return

init -800 python:

    # Class of the Passion Fruit.
    class passionF(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Enter the passionF_label label defined above.
            # The function might look scary, but to us, it's like a regular call.
            return renpy.call_in_new_context("passionF_label")

    # Passion Fruit defined.
    passionFruit = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )