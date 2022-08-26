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

init -920 python:

    # This is the class that contains the most important settings.
    # While you can customize a LOT of things in the styles below, 
    # if you're happy with the default layout, you can just change these
    # settings and start using the Inventory straight away.
    class InventorySettings():

        def __init__(self):

            ############################
            ## Variables of the Inventory screen.
            ############################

            # How the grid of Inventory Slots looks.
            # Tuple in the form of (width, height), a 3x3 grid by default.
            self.grid = (3, 3)

            # Size of the Inventory
            self.mainFrameSize = (1280, 720)

            # Size of one Inventory Slot
            self.slotSize = (180, 180)

            # Background of the whole Inventory
            self.mainFrame = "gui/frame.png"

            # Backgrounds of an Inventory Slot that contains an Item.
            self.slotFullIdle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
            self.slotFullHover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
            self.slotFullSelected = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)
            self.slotFullSelectedHover = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)

            # Background of an Inventory Slot that is empty.
            self.slotEmptyIdle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
            self.slotEmptyHover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)

            # A highlight effect that the Inventory Slot which holds a currently
            # equipped item will have.
            # Is shown *below* the item.
            self.equippedHighlight = "lezInventory/gui/equippedHighlight.png"

            # A highlight effect that the Equipped Item Slot always has.
            # Is shown *below* the item.
            self.equippedHighlightSlot = "lezInventory/gui/equippedHighlightSlot.png"

            # Variables that control what is showed on the Inventory screen.
            # This allows the user to quickly reduce the Inventory's functionality,
            # should they desire to do so.
            self.showEquippedLabel = True
            self.showEquippedSlot = True
            self.showInfo = True
            self.showEquipButton = True
            self.showUseButton = True
            self.showThrowAwayButton = True

            ############################
            ## Variables of Item functionality
            ############################

            # Whatever these values are, they can be overwritten in a specific Item.

            # If True, usable items get removed upon use by default.
            self.defaultUseConsume = True

            # If True, equippable items get removed upon unequip by default.
            self.defaultUnequipConsume = True

            # If True, Items are stackable by default.
            self.defaultStack = False

            # Int. Used if an Item is stackable and stacksize isn't given.
            # Don't set this to 
            self.defaultStackSize = 3

    InventorySettings = InventorySettings()