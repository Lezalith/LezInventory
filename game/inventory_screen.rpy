
##########################
## The Main Frame
##########################

# Main window of the Inventory.
style inventory_main_frame:

    xysize (1280, 720)
    align (0.5, 0.5)

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
    background Frame("inventory/gui/slot.png", 6, 6, 6, 6)
    selected_background Frame("inventory/gui/slot_selected.png", 6, 6, 6, 6)
    xysize (180, 180)

# One Slot for an Item inside the grid, when the slot is empty.
style inventory_slot_empty:
    background Frame("inventory/gui/slot.png", 6, 6, 6, 6)
    xysize (180, 180)

##########################
##  Side Menu
##########################

# Frame that contains everything in the Side Menu.
style side_menu_frame:
    background None
    xysize(400, 660)
    align (1.0, 0.5)
    xoffset -30

# Vbox that contains the "Equipped Item" label, 
# and the Equipped Slot.
style side_menu_vbox_equipped:
    align (0.5, 0.06)
    spacing 5

# The "Equipped Item" label.
# Has no properties at the time of writing.
# style side_menu_vbox_equipped_text:
#     example 123

# The Equipped Slot.
style side_menu_vbox_equipped_slot:
    background Frame("inventory/gui/slot.png", 6, 6, 6, 6)
    xysize (200, 200)
    xalign 0.5



##########################
## 
##########################

style inventory_pages_text:

    size 42

style inventory_pages_button_text:

    size 42

###########################################
###########################################
#
# Inventory Screen
#
###########################################
###########################################

screen inventoryScreen():

    # You cannot interact with other shown screens below.
    # This means not even clicking to continue dialogue.
    modal True

    # Background. Used just for testing.
    # TODO: Remove Test BG.
    add Solid("c0c0c0")

    # Frame of the Inventory
    frame: 

        style_prefix "inventory"
        style_suffix "main_frame" # Style: inventory_main_frame

        # Grid of all the Inventory Slots.
        # The grid size depends on the defined "grid" of an inventory.
        grid Inventory.grid["width"] Inventory.grid["heigth"]:

            style_suffix "slots_grid" # Style: inventory_slots_grid

            # .getPageItems() fetches items that are supposed 
            # to be shown on the current inventory page.
            #
            # Enumerate gives us a tuple of (index, item) for every iteration.
            for index, item in enumerate( Inventory.getPageItems() ):

                # One Slot.
                # Has a background to also function as a frame around the item.
                button:

                    style_suffix "slot" # Style: inventory_slot

                    # Test whether this slot is Equipped.
                    if Inventory.isEquipped(index):

                        # Custom screen statement. Check 01marker.rpy.
                        marker:
                            color "fc1"
                            xysize (155, 155)

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
                    selected Inventory.isSelected(index)

                    # Triggers .selectToggle(), a method which manages
                    # selecting and deselecting items.
                    action Function( Inventory.selectToggle , index )
                    
                    # An Image of the item inside the frame.
                    add item.getImage():

                        # Normally I would put style_suffix "slot_image" here, but
                        # as it turns out, add cannot have a style.
                        # So this is one of the few properties we have to manually write here. 
                        align (0.5, 0.5)
                        
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

            style_prefix "side_menu"
            style_suffix "frame" # Style: side_menu_frame

            # A vertical box. This one contains:
            # 1) The "Equipped Item:" label 
            # 2) Slot with an equipped Item
            vbox:

                style_suffix "vbox_equipped" # Style: side_menu_vbox_equipped

                # Label
                text "Equipped Item:" style_suffix "vbox_equipped_text" # Style: side_menu_vbox_equipped_text

                # Frame around the Slot.
                frame:

                    style_suffix "vbox_equipped_slot" # Style: side_menu_vbox_equipped_slot

                    # If there is an Equipped Item, add its Image in the middle.
                    if Inventory.getEquippedItem():
                        add Inventory.getEquippedItem().getImage():

                            # Normally I would put style_suffix "vbox_equipped_slot_image" here, but
                            # as it turns out, add cannot have a style.
                            # So this is one of the few properties we have to manually write here. 
                            align (0.5, 0.5)


                    # If there is an Equipped Item, create a marker around it.
                    # Makes more clear how the equipped item is marked in the Inventory slots.
                    # if Inventory.getEquippedItem():

                    # Custom screen statement. Check 01marker.rpy.
                    marker:
                        color "fc1"
                        xysize (175, 175) 

            # A vertical box. This one contains:
            # 1) Text of Item's name
            # 2) Text of Item's description
            vbox:

                align (0.5, 0.56)
                spacing 5
                xsize 500

                # Item's Name.
                # Underlined to create a line between this and...
                text ( Inventory.getSelectedItem().name if Inventory.getSelectedItem() else "Nothing selected." ):
                    xalign 0.5
                    underline True

                # Item's Description.
                # Smaller Size.
                text ( Inventory.getSelectedItem().description if Inventory.getSelectedItem() else "Nothing selected." ):
                    xalign 0.5
                    size 24

            # A vertical box. This one contains:
            # 1) A horizontal box with the Equip, Unequip and Use buttons
            # 2) The Throw Away button
            vbox:

                align (0.5, 0.83)
                xsize 400
                spacing 8

                # A horizontal box. This one contains:
                # 1) The Equip button (If Unequip is hidden)
                # 2) The Unequip button (If Equip is hidden)
                # 3) The Use button.
                hbox:
                    xalign 0.5
                    spacing 50

                    # Checks whether the player can Unequip an item.
                    # This means that NOT ONLY does an item have to be equipped,
                    # that same item also has to in a selected slot.
                    if Inventory.canUnequip():

                        textbutton "Unequip":

                            action Function(Inventory.unequip)

                    # If you can't Unequip stuff, automatically show the Equip button.
                    else:

                        textbutton "Equip": 

                            # .canEquip() decides whether you can actually click the button.
                            # Depends on whether an Equippable is Selected.
                            sensitive Inventory.canEquip()
                            action Function(Inventory.equip)

                    # Either way, the Use button is shown.
                    textbutton "Use": 
                        
                        # .canUse() decides whether you can click this button,
                        # and this one depends on the Item being Usable. 
                        sensitive Inventory.canUse()
                        action Function(Inventory.use)

                # The Throw Away button.
                textbutton "Throw Away":

                    # Can be clicked if an item is Selected.
                    sensitive Inventory.getSelectedItem()
                    xalign 0.5
                    action Function(Inventory.remove)

            # The Return button. Closes the Inventory.
            textbutton "Return":

                align (0.5, 1.0)
                action Return()

        # A horizontal box. This one contains:
        # 1) Left Arrow for controlling Inventory Pages
        # 2) Text of the format "<Current Page> / <Total Pages>"
        hbox:

            style_prefix "inventory_pages"

            xanchor 0.5
            xpos 415
            yalign 0.965

            spacing 180

            # Left Arrow. Goes DOWN a Page.
            textbutton "<":
                action Function( Inventory.changePage, "down" )

            # Text with the current page and total pages.
            # .format expects two arguments.
            # .getPagesRepr() returns a tuple (<current page>, <total pages>),
            # which is then unpacked into two arguments by the *.
            text "{} / {}".format( *Inventory.getPagesRepr() ):
                ypos 7

            # Left Arrow. Goes UP a Page.
            textbutton ">":
                action Function( Inventory.changePage, "up" )
