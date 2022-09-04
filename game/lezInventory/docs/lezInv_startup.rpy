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
# Hi there! So glad to see you!
#
# Welcome to my LezInventory, an Inventory framework. 
# This code's purpose is to let other creators code an Inventory into their game(s),
# an Inventory that I think is easy to set up, to use, to customize and relatively to understand.
#
# I've tried to comment every piece of code in these files, so while some knowledge of
# Python classes will prove useful, an amateur should be able to get as far as an expert will.
#
##############################################################################
#
# First, I will tell you some basic functionalities, and where to find all of them in files.
# 
# 95% of all the functionality is found in the inventory_class.rpy file. As there is
# only one object that handles the whole Inventory, all of the functions are tied to it.
#
# Inventory is defined once, at the bottom of the inventory_class.rpy file.
# It is called "inventory" (lowercase i is important!), however you can change it's name
# to whatever suits you, or even delete the default altogether and define it yourselves somewhere else.
#
# After the Inventory is defined, we can use all the different functions/methods. 
# Some are used directly by the Inventory screen, and some you will be using yourself.
# 
# Here's an overview of all the functions that you might need.
#
# inventory.add(Item) - adds an Item to the Inventory.
# inventory.remove(Item) - removes an Item from the Inventory. Item can be ommited, 
#                          in which case the currently selected Item is removed (if one is selected).
# inventory.use(Item) - triggers the .use method of Item. Item can be ommited, 
#                       in which case the currently selected Item is used (if one is selected).
# inventory.equip(Item) - Places the Item into Inventory's equip slot and triggers Item's .equip method.
#                       Item can be ommited, in which case the currently selected Item is equipped (if one is selected).
# inventory.use(Item) - Removes the Item from Inventory's equip slot and triggers Item's .unequip method.
# inventory.clear() - Removes all Items currently in the Inventory.
# inventory.is_in_inventory(Item), to check whether Item is in the Inventory
# inventory.getEquippedItem() or inventory.is_equipped(Item) to see which Item is currently equipped
#
#
# I think you should only need more of them if you decide to do big changes to the Inventory screen,
# but if that's up your alley, go for it. All the functions are documented as well as can be, 
# all in the inventory_class.rpy file.
#
###############################################################################
#
# Second, you should learn how to define some Items to place into your Inventory.
#
# As might be expected, that's kind of a big topic in itself, so if you want to
# learn how to do that (And you probably should, Items are kinda an important part
# of an Inventory), jump over to lezInv_items.rpy, in the docs folder.
#
# It's the same folder as this doc file is in, so you should've
# encountered it already!
#
################################################################################
#
# Finally, for the basic customization, visit two more files:
#
# inventory_screen.rpy
# On top of that file (all the way up until about half of the file) are all the styles
# used in the screen. They are commented so you know exactly what style controls what,
# and once you change something in the style, it will change on the Inventory screen.
# 
# The names are written logically, as they go deeper.
# If we take one of the complex examples...
# 
# inventory_ is a prefix all styles here have
# side_menu is a frame containing everything on the right side.
# vbox_interaction is a name I chose for the vbox containing most buttons.
# throwaway_textbutton finally points at the textbutton of "Throw Away".
# style inventory_side_menu_vbox_interaction_throwaway_textbutton
#
# The second file is inventory_settings.rpy
# This file has a InventorySettings class.
# No functions here, you won't be using this one yourselves at all.
#
# It is there to control some of the most basic things about the Inventory,
# for example how the Slots grid looks.
# Just open the file, read what the variables inside the class do, change what you need.  
#
################################################################################
#
# After the Inventory is set up, it is ready to be shown!
#
# It can be shown either from a screen, a label, as demonstrated in the
# LezInventory project, to suit all your needs.
#
# To show it through a label, simply use "call screen inventory_screen".
#
# To show it through a screen, use the action Show("inventory_screen", howToLeave = "both").
# As you can see, it has one argument, howToLeave. This determines what happens when
# the Return button is clicked, being "both" in the LezInventory project. 
# "return" will Return(), "hide" will Hide("inventory_screen"), and "both" will first Hide(), then Return().
#
# You can also use the Ren'Py function for showing or calling a screen,
# renpy.show_screen("inventory_screen") for showing it,
# renpy.call_screen("inventory_screen") for calling it.
#
#################################################################################
#
# There you go! If you go through all of this, you should understand the basics of LezInventory.
#
# Well... All of it, hopefully. 
# I really tried my best to write this Inventory to be as simple but at the same time
# as powerful as can be. Hopefully I've achieved this.
#
# Do let me know of your experience on my Discord, "Lezalith (LezCave.com)#2853".
# I will always be happy to hear from you.
#
# Godspeed, pilgrim.
# (I randomly remembered this when I was writing this file for the first time.
# In my world, that quote is said by Josh, at the beginning of Until Dawn.)