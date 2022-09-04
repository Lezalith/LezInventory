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


# This is where all the different settings variables are defined.
# They affect mostly the visuals of the Inventory screen and the default
# functionality of Items, like whether Usables are consumed by default.

# It has to be defined before it is used in any of the Inventory classes.
# (At the time of writing, closest is Inventory at -900)
# It also can't be below -999, that's where Ren'Py Internals are.
init offset = -966

############################
## Variables of the Inventory screen.
############################

# How many slots is the Inventory wide and high.
# It is 3 by 3 slots by default.
define lezInv_settings.width = 3
define lezInv_settings.height = 3

# Size of the Inventory
define lezInv_settings.main_frame_size = (1280, 720)

# Size of one Inventory Slot
define lezInv_settings.slot_size = (180, 180)

# Background of the whole Inventory
define lezInv_settings.main_frame_image = "gui/frame.png"

# Backgrounds of an Inventory Slot that contains an Item.
define lezInv_settings.slot_full_idle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_hover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_selected = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_selected_hover = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)

# Background of an Inventory Slot that is empty.
define lezInv_settings.slot_empty_idle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_empty_hover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)

# Background of the Equipped Slot.
define lezInv_settings.slot_equipped_image = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)

# A highlight effect that the Inventory Slot which holds a currently
# equipped item will have.
# Is shown *below* the item.
define lezInv_settings.equipped_highlight_image = "lezInventory/gui/equipped_highlight_image.png"

# A highlight effect that the Equipped Item Slot always has.
# Is shown *below* the item.
define lezInv_settings.equipped_highlight_slot_image = "lezInventory/gui/equipped_highlight_imageSlot.png"

# Variables that control what is showed on the Inventory screen.
# This allows the user to quickly reduce the Inventory's functionality,
# should they desire to do so.
define lezInv_settings.show_equipped_label = True
define lezInv_settings.show_equipped_slot = True
define lezInv_settings.show_description = True
define lezInv_settings.show_equip_button = True
define lezInv_settings.show_use_button = True
define lezInv_settings.show_throw_away_button = True

############################
## Variables of Item functionality
############################

# Whatever these values are, they can be overwritten in a specific Item.

# If True, usable items get removed upon use by default.
define lezInv_settings.consumed_on_use = True

# If True, equippable items get removed upon unequip by default.
define lezInv_settings.consumed_on_unequip = False

# If True, Items are stackable by default.
define lezInv_settings.stackable = False

# Int. Used if an Item is stackable and stack_size isn't given.
# stack_size is ignored completely by Items that aren't stackable.
define lezInv_settings.stack_size = 3