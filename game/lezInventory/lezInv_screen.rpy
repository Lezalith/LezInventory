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

###########################################
###########################################
#
# Inventory Screen Styles
#
###########################################
###########################################

# Here are all the Styles used by the Inventory Screen,
# which allow you to heavily customize it,
# without having to touch the screen's code.
# 
# The names are written logically, as they go deeper.
# If we take one of the complex examples...
# 
# style inventory_side_menu_vbox_interaction_throwaway_textbutton
# 
# inventory_ is a prefix all styles here have
# side_menu is a frame containing everything on the right side.
# vbox_interaction is a name I chose for the vbox containing most buttons.
# throwaway_textbutton finally points at the textbutton of "Throw Away".

#---------------

# Also, a big note.
# There are some styles that say "# Has no properties at the time of writing."
# This means that the style is ready for you, should you need it, but
# I haven't needed it in my default Inventory.
# 
# These split into two different types:
#
# A) Those that are commented out
# These are commented out. To use them, simply uncomment them
# and go ahead with adding properties.
#
# B) Those that have to be defined.
# Some of the styles *have* to be defined, for a reason I won't go into.
# (I'm not even sure whether it's the correct reason, to be fair, but I do have a clue.)
# Those styles already contain *something*, a placeholder that doesn't matter.
# Most of the time, this is the "background" property set to "None", used in places
# where the background is already None anyway, so it essentially doesn't change anything.

##########################
## The Main Frame
##########################

# Main window of the Inventory.
style inventory_main_frame:
    xysize InventorySettings.mainFrameSize
    align (0.5, 0.4)

##########################
## The Grid with Slots
##########################

# Grid of the Item Slots
style inventory_slots_grid:
    xpos 100
    yalign 0.5
    yoffset -35
    xspacing 50
    yspacing 15

# One Slot for an Item inside the grid, when the slot is full.
style inventory_slot:
    idle_background InventorySettings.slotFullIdle
    hover_background InventorySettings.slotFullHover
    selected_idle_background InventorySettings.slotFullSelected
    selected_hover_background InventorySettings.slotFullSelectedHover
    xysize InventorySettings.slotSize

# One Slot for an Item inside the grid, when the slot is empty.
style inventory_slot_empty:
    idle_background InventorySettings.slotEmptyIdle
    hover_background InventorySettings.slotEmptyHover
    xysize InventorySettings.slotSize

# Text - Number of items on the stack.
style inventory_slot_text:
    align (1.0, 1.0)
    offset (-10, -5)
    bold True
    size 48
    color "000"
    outlines [ (absolute(4), "ffcc11", absolute(0), absolute(0)) ]

##########################
##  Side Menu
##########################

# Frame that contains everything in the Side Menu.
style inventory_side_menu_frame:
    # background Solid("000") # Great for testing, shows the Frame.
    background None
    xysize(400, 660)
    align (1.0, 0.5)
    xoffset -50

#-----------------------------------------------------
# Vbox of Equipped Item and its Slot.
#-----------------------------------------------------

# Vbox that contains the "Equipped Item" label, 
# and the Equipped Slot.
style inventory_side_menu_vbox_equipped:
    xalign 0.5
    spacing 5
    ypos 30

# The "Equipped Item" label.
# Has no properties at the time of writing.
# style inventory_side_menu_vbox_equipped_text:
#     example 123

# The Equipped Slot.
style inventory_side_menu_vbox_equipped_slot:
    background Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
    xysize (200, 200)
    xalign 0.5

#-----------------------------------------------------
# Vbox of Name and Description.
#-----------------------------------------------------

# Vbox that contains the Name and Description,
# of the selected item.
style inventory_side_menu_vbox_info:
    xsize 400 # Same size as the inventory_side_menu_frame.
    xalign 0.5
    spacing 5
    ypos 330

# Selected Item's Name.
style inventory_side_menu_vbox_info_name:
    xalign 0.5
    underline True

# Selected Item's Description.
style inventory_side_menu_vbox_info_description:    
    xalign 0.5
    size 26

#-----------------------------------------------------
# Vbox of Interactables (Buttons)
#-----------------------------------------------------

# Vbox that contains:
# Hbox containing Equip and Unequip buttons 
# Use button
# Throw Away button.
style inventory_side_menu_vbox_interaction:   
    xsize 400 # Same size as the inventory_side_menu_frame.
    xalign 0.5
    ypos 460
    spacing 8

# Hbox containing Equip and Unequip buttons.
style inventory_side_menu_vbox_interaction_equip_box:
    xalign 0.5
    spacing 30
    xoffset -12

#---------------

# The Unequip textbutton.
style inventory_side_menu_vbox_interaction_unequip_textbutton:
    xsize 140

# The Unequip textbutton - Text part.
style inventory_side_menu_vbox_interaction_unequip_textbutton_text:
    xalign 0.5
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

#---------------

# The Equip textbutton.
style inventory_side_menu_vbox_interaction_equip_textbutton:
    xsize 140

# The Equip textbutton - Text part.
style inventory_side_menu_vbox_interaction_equip_textbutton_text:
    xalign 0.5
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

#---------------

# The Use textbutton.
# Has no properties at the time of writing.
# style inventory_side_menu_vbox_interaction_use_textbutton:
#     example 123

# The Use textbutton - Text part.
style inventory_side_menu_vbox_interaction_use_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

#---------------

# The Throw Away textbutton.
style inventory_side_menu_vbox_interaction_throwaway_textbutton:
    xalign 0.5

# The Throw Away textbutton - Text part.
style inventory_side_menu_vbox_interaction_throwaway_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

#-----------------------------------------------------
# Others
#-----------------------------------------------------

# The Return textbutton.
style inventory_side_menu_return_textbutton:
    align (0.5, 1.0)
    yoffset -10

# The Return textbutton - Text part.
style inventory_side_menu_return_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

##########################
## Pages 
##########################

# Hbox containing:
# Left Arrow
# Text Current/Last page
# Right Arrow
style inventory_pages_hbox:
    xanchor 0.5
    xpos 415
    ypos 630
    spacing 180

# The Left Arrow textbutton. 
# Has no properties at the time of writing, 
# but has to be defined. Background already is None.
style inventory_pages_hbox_left:
    background None    

# The Left Arrow textbutton - Text part. 
style inventory_pages_hbox_left_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
    size 42

#---------------

# The Current/Last Page text. 
style inventory_pages_hbox_text:
    ypos 7

#---------------

# The Right Arrow textbutton. 
# Has no properties at the time of writing, 
# but has to be defined. Background already is None.
style inventory_pages_hbox_right:
    background None

# The Right Arrow textbutton - Text part. 
style inventory_pages_hbox_right_text:
    size 42
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"

###########################################
###########################################
#
# Inventory Screen
#
###########################################
###########################################

# Takes one argument, howToLeave. This specifies what
# the Inventory does when the Return button is clicked.
# "return" will Return(), "hide" will Hide("inventoryScreen"),
# or "both" which will do both, first Hide, then Return.

screen inventoryScreen( howToLeave = "return" ):

    # You cannot interact with other shown screens below.
    # This means not even clicking to continue dialogue.
    modal True

    # Frame of the Inventory
    frame: 

        style_prefix "inventory"
        style_suffix "main_frame" # Style: inventory_main_frame

        # Grid of all the Inventory Slots.
        # The grid size depends on the defined "grid" of an inventory.
        grid Inventory.grid["width"] Inventory.grid["height"]:

            style_suffix "slots_grid" # Style: inventory_slots_grid

            # .getPageItems() fetches items that are supposed 
            # to be shown on the current inventory page.
            #
            # Enumerate gives us a tuple of (index, item) for every iteration.
            # TODO: index no longer used. Keep it? It doesn't harm anything rn.
            for index, item in enumerate( Inventory.getPageItems() ):

                # One Slot.
                # Has a background to also function as a frame around the item.
                button:

                    style_suffix "slot" # Style: inventory_slot

                    # Test whether this slot is Equipped.
                    if Inventory.isEquipped(item):

                        add InventorySettings.equippedHighlightSlot align (0.5, 0.5)

                    #######################################################################
                    # Used before Slots got different backgrounds through "selected" below.
                    # Adds the same marker from Equipped slot
                    # to a Selected slot, in different color.
                    #
                    # # Test whether this slot is Selected.
                    # if Inventory.isSelected(index):
                    #
                    #     # Custom screen statement. Check 01marker.rpy.
                    #     marker:
                    #         color "f00"
                    #         xysize (150, 150)
                    ##################################

                    # We further use .isSelected as means of telling Ren'Py
                    # when the button is selected, for example for background purposes.
                    selected Inventory.isSelected(item)

                    # Triggers .select(), a method which manages
                    # selecting and deselecting items.
                    action Function( Inventory.select , item )
                    
                    # An Image of the item inside the frame.
                    add item.image:

                        # Normally I would put style_suffix "slot_image" here, but
                        # as it turns out, add cannot have a style.
                        # So this is one of the few properties we have to manually write here. 
                        align (0.5, 0.5)

                    $ itemCount = Inventory.getItemCount(item)
                    if itemCount <= 1:
                        $ itemCount = ""

                    text str(itemCount):
                        style_suffix "slot_text"
                        
            # .getEmptyCells() fetches the number of cells that have
            # been left empty on a non-full page and fills them with empty space.
            #
            # This is necessary because Ren'Py requires grids to have all cells filled.
            for x in range( Inventory.getEmptyCells() ):

                # One Empty Slot.
                # Also has a background to function as a frame around the "item".
                button:

                    style_suffix "slot_empty" # Style: inventory_slot_empty                    

                    # Unselects the selected item.
                    action Function( Inventory.unselect )

        #########################
        # Buttons and text
        #########################

        # Frame, without a background.
        frame:

            style_prefix "inventory_side_menu"
            style_suffix "frame" # Style: inventory_side_menu_frame

            # A vertical box. This one contains:
            # 1) The "Equipped Item:" label 
            # 2) Slot with an equipped Item
            vbox:

                style_suffix "vbox_equipped" # Style: inventory_side_menu_vbox_equipped

                if InventorySettings.showEquippedLabel:

                    # Label
                    text "Equipped Item:":

                        style_suffix "vbox_equipped_text" # Style: inventory_side_menu_vbox_equipped_text

                if InventorySettings.showEquippedSlot:

                    # Frame around the Slot.
                    frame:

                        style_suffix "vbox_equipped_slot" # Style: inventory_side_menu_vbox_equipped_slot

                        # If there is an Equipped Item, create a marker around it.
                        # Makes more clear how the equipped item is marked in the Inventory slots.
                        # if Inventory.equipped:

                        add InventorySettings.equippedHighlight align (0.5, 0.5)
                        # If there is an Equipped Item, add its Image in the middle.
                        if Inventory.equipped:
                            add Inventory.equipped.image:

                                # Normally I would put style_suffix "vbox_equipped_slot_image" here, but
                                # as it turns out, add cannot have a style.
                                # So this is one of the few properties we have to manually write here. 
                                align (0.5, 0.5)

            if InventorySettings.showInfo:

                # A vertical box. This one contains:
                # 1) Text of Item's name
                # 2) Text of Item's description
                vbox:

                    style_suffix "vbox_info" # Style: inventory_side_menu_vbox_info

                    # Item's Name.
                    # Underlined to create a line between this and...
                    text ( Inventory.selected.name if Inventory.selected else "Nothing selected." ):

                        style_suffix "vbox_info_name" # Style: inventory_side_menu_vbox_info_name

                    # Item's Description.
                    # Smaller Size.
                    text ( Inventory.selected.description if Inventory.selected else "Nothing selected." ):

                        style_suffix "vbox_info_description" # Style: inventory_side_menu_vbox_info_description

            # A vertical box. This one contains:
            # 1) A horizontal box with the Equip, Unequip and Use buttons
            # 2) The Throw Away button
            vbox:

                style_suffix "vbox_interaction" # Style: inventory_side_menu_vbox_interaction

                # A horizontal box. This one contains:
                # 1) The Equip button (If Unequip is hidden)
                # 2) The Unequip button (If Equip is hidden)
                # 3) The Use button.
                hbox:

                    style_suffix "vbox_interaction_equip_box" # Style: inventory_side_menu_vbox_interaction_equip_box

                    if InventorySettings.showEquipButton:

                        # Checks whether the player can Unequip an item.
                        # This means that NOT ONLY does an item have to be equipped,
                        # that same item also has to in a selected slot.
                        if Inventory.canUnequip():

                            textbutton "Unequip":

                                style_suffix "vbox_interaction_unequip_textbutton" # Style: inventory_side_menu_vbox_interaction_unequip_textbutton

                                action Function(Inventory.unequip)

                        # If you can't Unequip stuff, automatically show the Equip button.
                        else:

                            textbutton "Equip": 

                                style_suffix "vbox_interaction_equip_textbutton" # Style: inventory_side_menu_vbox_interaction_equip_textbutton

                                # .canEquip() decides whether you can actually click the button.
                                # Depends on whether an Equippable is Selected.
                                sensitive Inventory.canEquip()
                                action Function(Inventory.equip)

                    if InventorySettings.showUseButton:

                        # Either way, the Use button is shown.
                        textbutton "Use": 

                            style_suffix "vbox_interaction_use_textbutton" # Style: inventory_side_menu_vbox_interaction_use_textbutton
                            
                            # .canUse() decides whether you can click this button,
                            # and this one depends on the Item being Usable. 
                            sensitive Inventory.canUse()
                            action Function(Inventory.use)

                if InventorySettings.showThrowAwayButton:

                    # The Throw Away button.
                    textbutton "Throw Away":

                        style_suffix "vbox_interaction_throwaway_textbutton" # Style: inventory_side_menu_vbox_interaction_throwaway_textbutton

                        # Can be clicked if an item is Selected.
                        sensitive Inventory.selected
                        action Function(Inventory.remove)

            # The Return button. Closes the Inventory.
            textbutton "Return":

                style_suffix "return_textbutton" # Style: inventory_side_menu_return_textbutton

                if howToLeave == "return":
                    action Return()
                elif howToLeave == "hide":
                    action Hide("inventoryScreen")
                elif howToLeave == "both":
                    action Hide("inventoryScreen"), Return()

        # A horizontal box. This one contains:
        # 1) Left Arrow for controlling Inventory Pages
        # 2) Text of the format "<Current Page> / <Total Pages>"
        hbox:

            style_prefix "inventory_pages"
            style_suffix "hbox" # Style: inventory_pages_hbox

            # Left Arrow. Goes DOWN a Page.
            textbutton "<":

                style_suffix "hbox_left" # Style: inventory_pages_hbox_left

                sensitive Inventory.canChangePage( -1 )
                action Function( Inventory.changePage, -1 )

            # Text with the current page and total pages.
            # .format expects two arguments.
            # .getPagesRepr() returns a tuple (<current page>, <total pages>),
            # which is then unpacked into two arguments by the *.
            text "{} / {}".format( *Inventory.getPagesRepr() ):

                style_suffix "hbox_text" # Style: inventory_pages_hbox_text

            # Left Arrow. Goes UP a Page.
            textbutton ">":

                style_suffix "hbox_right" # Style: inventory_pages_hbox_right

                sensitive Inventory.canChangePage( 1 )
                action Function( Inventory.changePage, 1 )
