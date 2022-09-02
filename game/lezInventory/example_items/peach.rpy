# Peach is a Usable item.
# When used, it shows a message stating how many peaches have been used so far.
# This means that multiple different Peaches can be defined, but they all share the same counter.

# A little secret label that can be shown instead of peach's renpy.notify.
label peachLabel():

    "Lezalith" "Did you..."
    "Lezalith" "Did you just...{p=1.0}Eat a peach number 4..?"
    "Lezalith" "But how? I put just three into the inventory!"

    "Lezalith" "..."
    "Lezalith" "Oh right, the Apricot."
    "Lezalith" "That's clever. I completely forgot about that."

    "Lezalith" "(...I didn't really.{p=1.0}I'm the one who wrote this dialogue.)"

    # Return back to the Inventory.
    return


init -800 python:

    # Class of the Peach.
    class Peach(Item):

        # This marks the Item as usable.
        usable = True

        # Signature function of Peach.
        # How many times an Item of the Peach class has been used.
        howManyTimesUsed = 0

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Up the class variable counter.
            Peach.howManyTimesUsed += 1

            # Show the count.
            if Peach.howManyTimesUsed != 4:
                renpy.notify("*Munching sounds...*\nYou just ate a peach number {}!".format(Peach.howManyTimesUsed))

            # Special message in a label instead, on the 4th peach used.
            else:
                renpy.call_in_new_context("peachLabel")


    # Three different peaches defined.
    peach1 = Peach( "Shiny Peach" , "It tastes really sweet!" , image = "lezInventory/example_items/images/19_Peach.png" )
    peach2 = Peach( "Shimmering Peach" , "It smells of an update." , image = "lezInventory/example_items/images/19_Peach.png" )
    peach3 = Peach( "Glistening Peach" , "Both tastes sweet {i}and{/i}\nsmells of an update." , image = "lezInventory/example_items/images/19_Peach.png" )