# Copyright 2021 - 2xxx Jan "Lezalith" Mašek <lezalith@gmail.com>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
##############################################################################
#
# Hey! 
# Welcome to the Docs that tell you how to define your own items.
#
# If you're here, it means you've probably visited lezInv_startup.rpy already.
# If not, I highly recommend you start there.
#
# There are three types of Items in LezInventory by default:
# - Regular Items, which don't do anything
# - Usable Items, which can be Used, triggering an effect
# - Equippable Item, which can be equipped into the Equip Slot the Inventory has
#
# Let's go over them one by one.
#
##############################################################################
#
# For regular items, you can simply define an Item object.
# Items take 2 positional arguments which have to be given,
# and three optional keyword arguments.
#
# This is the bare minimum:
define docCherries = Item( "Cherries" , "Spit the seeds at your foes!" )
#
# The positional arguments, the two that have to be provided, are the name and the description.
# `name` and `description` both have to be strings.
#
# This Item has *all* the possible arguments provided:
default docOrange = Item( "Orange" , "Lezalith's massive stash of oranges for making juice." , image = "lezInventory/example_items/images/17_Orange.png" , stackable = True, stacksize = 2579)
#
# `image`
# The image of the Item. This follows the same rules as Ren'Py when it comes to images:
# it can be a string with a filename, string with a defined image (through the image statement), or a Displayable. 
# If it's the default of None, a Text displayable with the Item's name is created to represent it.  
# 
# `stackable`
# Whether the Item is stackable or not. It can be True or False, and is False by default.
# Stackable means that multiples of the same Item are stored in a single Inventory Slot.
#
# `stacksize`
# Has to be an int (a number), is 1 by default, and is ignored completely if stackable is False.
# How many of the same Item can be in the Inventory Slot. 
# This cannot be exceeded. Should more of the Item be added after reaching max stacksize,
# the extra Items will be discarded.
#
##############################################################################
#
# Moving onto Items that *do* do stuff, let's look at Usable Items. These can be used inside the Inventory, triggering an effect.
# To define your own Usable Items, you will need to define a new Class for the Item. 
#
# This is done in pure Python, but it's not as scary as it sounds.
# Here is what the simplest Usable Item can look like:


# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # Class of the Dragon Fruit.
    #### You of course have to give it a different name.
    class DocDragonF(Item):

        # This marks the Item as usable.
        usable = True

        # __init__ got ommited, as this Item doesn't take/need any extra arguments.
        #### (I'll explain this in just a moment)

        # What happens when the Item is used.
        #### This is where you want to put your own functionality.
        def used(self, Inventory):

            # Show a screen that's defined somewhere.
            return renpy.show_screen("dragonScreen")


# First, the Item has to know that it's usable.
# For this, it has to have the `usable` class variable set to `True`.
# Class variables are put directly under the class name.
#
# After that, we can ommit __init__, unless we need some special setup for this Item.
# If it's ommited, this Item sticks to what the regular Item has defined.
# Out of all the Example Items, the only one with __init__ is the Lemon, because that one stores the current state
# of the Inventory, and it has to have a variable prepared for it.
#
# Finally, the `used` method is what is called when the Item is used in the Inventory.
# There's where you put anything and everything you want the Item to do.
#
# With the class defined, we can now define the Item itself that can be added to the Inventory.

default docDragonFruit = DocDragonF( "Dragon Fruit" , "White as snow on the inside." , image = "lezInventory/example_items/images/07_Dragonfruit.png" )

###################
#
# Of course, there are more options to your own defined Items, which I'll show you in just a moment.
# However, let me first show you Equippable Items, since they are defined in the exact same way.
#
# Here is what the simplest Equippable Item can look like:


# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # Class of the Apple.
    #### You of course have to give it a different name.
    class DocApple(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        #### This is where you want to put your own functionality.
        def equipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        #### This is where you want to put your own functionality.
        def unequipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("Long live the king...")


# Again, we state that the Item can do something, with the `equippable` class var this time, set to `True`.
#
# After that, there are two different methods for functionality this time:
# `equipped`, which is called when the Item is equipped.
# `unequipped`, which is called when the Item is unequipped.
# 
# You might think that both HAVE to be given, but if you want an Item to do something only on being equipped, 
# you can ommit unequipped just without issues.
#
# With the class prepared, we again define an Item that can be added to the Inventory.

default docApple = DocApple( "Apple" , "The King of all the fruits." , image = "lezInventory/example_items/images/16_Apple.png" )

###################
#
# With the simplest possible codes out of the way, let's now look at the most complex one.
#
# Not only does this include all the class variables to show all the settings that you can change,
# it also shows the __init__ you might need, and shows that Items can be both usable and equippable.
#
# TODO: ?
# It's a monster stitched from Dragon Fruit and Apple, not found as an Example in the Inventory Preview.

# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # Class stitched from dragon fruit and apple.
    #### You of course have to give it a different name.
    class DocMonster(Item):

        # This marks the Item as usable.
        # It is False by default.
        usable = True

        # This marks the Item as equippable.
        # It is False by default.
        equippable = True

        # States whether the Item should be removed upon being used.
        # Default is taken from lezInv.settings.rpy 
        consumedOnUse = True

        # States whether the Item should be removed upon being unequipped.
        # Default is taken from lezInv.settings.rpy 
        consumedOnUnequip = True

        # __init__ that takes care of setting up the default Item stuff,
        # while allowing us to add our own functionality, like a new argument.
        def __init__(self, exampleArgument, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            #### The class given to `super` has to be the same as this class. 
            super(DocMonster, self).__init__( *args, **kwargs )

            #### Custom functionality can follow. If no functionality is needed, __init__ can be ommited completely.
            #### I just store the exampleArgument in a variable that does nothing.
            self.exampleVariable = exampleArgument

        # What happens when the Item is used.
        #### This is where you want to put your own functionality.
        def used(self, Inventory):

            # Show a screen that's defined somewhere.
            return renpy.show_screen("dragonScreen")

        # What happens when the Item is Equipped
        #### This is where you want to put your own functionality.
        def equipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        #### This is where you want to put your own functionality.
        def unequipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("Long live the king...")


# With all that code done, we can once again define the Item itself.
# I'm not giving it an image because, uh, I don't have one.

default docMonster = DocMonster(name = "Dragon Apple", desc = "Igor! Fetch me the brain!", exampleArgument = "something")

######################################################################################
#
# When you're done reading this, you should be able to define your own items!
#
# I still highly recommend checking out the codes of (at least) the basic Items.
# Basic Items show the most common functionality, like showing a screen, showing an image or entering a label.
# These are the files of Items classified as basic:
#
# Equippables:
# durian.rpy - shows/hides an image.
# apple.rpy - uses a function on both equip and unequip.
#
# Passives:
# orange.rpy - does nothing but there's a lot of them.
# cherries.rpy - does nothing.
# kiwi.rpy - does nothing.
# strawberry.rpy - does nothing.
#
# Usables:
# dragonfruit.rpy - shows a screen.
# passionfruit.rpy - calls a label.
# plum.rpy - adds multiple counts of one Item into the Inventory.
# grapefruit.rpy - wipes the inventory clean.
#
# Go check them out, they're commented and very simple to understand!
#
######################################################################################
#
# I can't wait to see what amazing Items people can create with this!