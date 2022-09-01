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

init -900 python:

    # Holds the Inventory.
    from collections import OrderedDict

    ###########################################
    ###########################################
    #
    # InventoryObject Class
    #
    ###########################################
    ###########################################

    # InventoryObject uses Indexes. 
    # Indexes are counted from 0 rather than from 1.
    #
    # Index 0 in the inventory means 1st item, 
    # Index 1 second item, 2 third item and so on...
    # 
    # Same thing for pages. In here, page = 0 means the first page,
    # page 1 is the second, 2 is the third.
    # 
    # The ONLY time when this is not true is in the getPagesRepr method,
    # which gives you the "real" number rather than the index.
    # That is the one that should be used for printing purposes.

    class InventoryObject(object):

        "Inventory that holds all the items and manages them."

        def __init__(self):
 
            # In slots, width and height of the Inventory.
            self.width = lezInvSettings.width
            self.height = lezInvSettings.height

            # INDEX of the page that we're on.
            self.page = 0

            # OrderedDict. Keys are Item objects, Values are Ints representing a count.
            self.inventory = OrderedDict()

            # Currently selected Item (Key of self.inventory).
            self.selectedItem = None

            # Currently equipped Item (Key of self.inventory)
            self.equippedItem = None

        ##########################################
        ## Inventory - Add, Remove and Clear Functions
        ##########################################

        # Adds an Item to inventory.
        # If the Item is stackable, count can be given to add more than one.
        def add(self, item, count = 1):

            # Item is not stackable.
            if not item.stackable:

                # Put one into the Inventory.
                self.inventory[item] = 1

            # Item is stackable.
            else:

                # Item is already in the Inventory.
                if item in self.inventory.keys():

                    # Increment the Item count.
                    self.inventory[item] = self.inventory[item] + count

                # Item is not already in the Inventory.
                else:

                    # Set the Item count.
                    self.inventory[item] = count

            # Check whether the count hasn't gone over Item's stacksize.
            if self.inventory[item] > item.stacksize:

                # Set it to max value if it has.
                self.inventory[item] = item.stacksize

        # Removes an Item from the inventory.
        # If item is not specified, it will remove the selected item,
        # unless there isn't one selected, in which case it does nothing.
        # If count is not 0 and the item is stackable, it will instead remove
        # the stacks, and only the Item if the stack goes below 1.
        def remove(self, item = None, count = 1):

            # item not provided.
            # Attempting to use the SelectedItem instead.
            if item == None:

                # Do nothing if nothing is selected
                if self.selectedItem == None:
                    return

                item = self.selectedItem

            # Item is stackable.
            if item.stackable:

                # Item is present in the Inventory.
                if item in self.inventory.keys():

                    # Decrement the count.
                    self.inventory[item] -= count

                    # If the count has gone below 1.
                    if self.inventory[item] < 1:

                        # Unequip the Item if it's equipped.
                        if item == self.equipped:

                            self.unequip()

                        # Unselect the Item if it's selected.
                        if item == self.selected:
                            self.unselect()

                        # Completely remove the Item from the inventory.
                        del self.inventory[item]

                    # Check pages whether we don't have
                    # (an) empty one(s) after the removal.
                    self.checkPages()

            # Unstackable Item
            else:

                # Unequip if this Item was equipped
                if item == self.equippedItem:
                    self.unequip()

                # Unselect this item
                print("Unselected.")
                self.unselect()

                del self.inventory[item]

                # If we try to remove it straight away before unselecting it,
                # the screen manages to render one more time, and throws
                # an error because it doesn't find the selected item
                # inside the inventory.

            # Check pages whether we don't have
            # (an) empty one(s) after the removal.
            self.checkPages()

        # Clears the whole inventory.
        def clear(self):

            self.inventory = OrderedDict()
            self.equippedItem = None
            self.selectedItem = None
            self.page = 0

        # Lets us read inventory with InventoryObject.items
        @property
        def items(self):
            return self.inventory

        ####################################################################
        ## Selection of Items
        ####################################################################

        # Selects an Item.
        def select(self, item):

            # If given item is already selected.
            if self.selectedItem == item:

                # Unselect it, and with that end this function.
                return self.unselect()

            # Set the item as selected.
            self.selectedItem = item

        # Unselects the selected item.
        def unselect(self):

            self.selectedItem = None

        # Lets us read selectedItem with InventoryObject.selected
        @property
        def selected(self):
            return self.selectedItem

        ###############################
        ## Equipping and Using of Items
        ###############################

        # Equips an Item.
        # If item is not given, tries to equip currently selectedItem.
        # If item is given, a specific item is Equipped, being added into
        # inventory in the process if it's not already present.
        def equip(self, item = None):

            # Specific item not given.
            if not item:

                # Do nothing if nothing is selected.
                if not self.selectedItem:
                    return

                # Refer to the selectedItem.
                item = self.selectedItem

            # Specific item given.
            else:

                # Add it to the Inventory, if it's not present.
                if not item in self.inventory.keys():
                    self.add(item)

            # (Continue with the equip process.)

            # Something was already equipped.
            if self.equippedItem != None:

                # Unequip it first.
                self.unequip()

            # Call Item's equipped() method.
            item.equipped(InventoryObject = self)

            # Set the Item as equipped.
            self.equippedItem = item

        # Unequip currently equipped Item.
        def unequip(self):

            # Do nothing if nothing is equipped.
            if self.equippedItem == None:
                return

            # Call Item's unequipped() method.
            self.equippedItem.unequipped(self)

            # Store the item so we can unequip it.***
            i = self.equippedItem

            # Set Item equipped to None.
            self.equippedItem = None

            # Check if the item is supposed to be consumed.
            if i.consumedOnUnequip:

                # Remove the Item from the Inventory.
                # *** It cannot just be self.equippedItem, since remove() will call unequip() again.
                self.remove(i)

                # TODO: Create an example on consumedOnUnequip.

        # Use an Item.
        # If item is not given, tries to use currently selectedItem.
        # If item is given, a specific item is Used. It doesn't have to be present in the Inventory.
        def use(self, item = None):

            # Specific item given.
            if item:

                # Call Item's used() method.
                return item.used(self)

            # Do nothing if nothing is selected.
            if not self.selectedItem:
                return

            # Call Item's used() method.
            self.selectedItem.used(self)

            # An extra check whether an Item is still selected, in case the Item's
            # effect messed around with it. Guava Item is a good example of that.
            if self.selectedItem:

                # Check if the item is supposed to be consumed.
                if self.selectedItem.consumedOnUse:

                    # Remove the Item from the Inventory.
                    self.remove()

        # Lets us read equippedItem with InventoryObject.equipped
        @property
        def equipped(self):
            return self.equippedItem

        ##################################################
        ## Checks, used mostly in the Inventory Screen
        ##################################################

        # Whether given item is currently selected.
        def isSelected(self, item):
            
            return self.selectedItem == item

        # Whether given item is currently equipped.
        def isEquipped(self, item):
            
            return self.equippedItem == item

        # Whether currently equipped item can be unequipped.
        # Returns True if the equipped item is also the one currently selected.
        def canUnequip(self):

            return self.selectedItem == self.equippedItem

        # Whether an item can be equipped.
        # Returns True if an equippable item is currently selected.
        def canEquip(self):

            # If an Item is selected.
            if self.selectedItem != None:

                # Check the equippable property.
                return self.selectedItem.isEquippable()

            # If an Item isn't selected.
            return False 

        # Whether an item can be used.
        # Returns True if a usable item is currently selected.
        def canUse(self):

            # If an Item is selected.
            if self.selectedItem != None:

                # Check the usable property.
                return self.selectedItem.isUsable()

            # If an Item isn't selected.
            return False 

        # Whether an item is present in inventory.
        def isInInventory(self, item):

            return item in self.inventory.keys()

        ###################
        ## Page Functions
        ###################

        # Returns the index of the current page.
        def getCurrentPage(self):
            return self.page

        # Returns tuple of two ints - (Current Page INDEX, Final Page INDEX ).
        def getPages(self):

            # Calculate how many pages are there.
            lastPage = (len(self.inventory) - 1) // self.getSize()

            # A safe check. 
            if lastPage < 0:
                lastPage = 0

            # First is the current page index, second is the last page index.
            return ( self.page, lastPage )

        # Check pages whether we don't have (an) empty one(s)
        def checkPages(self):

            pages = self.getPages()

            if pages[0] > pages[1]:

                self.page = pages[1]

        # Moving up or down between pages. 1 goes up a page, -1 down a page.
        # You can move multiple pages, but it won't let you go to an empty one.
        def changePage(self, direction):

            # Check whether the move can be executed.
            if not self.canChangePage(direction):
                return None

            try:

                self.page += direction

            # Not given a number.
            except TypeError:
                raise Exception("changePage() got invalid direction.")


            # Finally, unselect whatever's selected.
            self.unselect()

        # Checks whether we can move between pages.
        # Moving is possible as long as we're not going past the first
        # or past the final page.
        def canChangePage(self, direction):

            # Only on one page - Cannot move anywhere.
            if self.getPages()[1] == 0:
                return False

            try:

                # Checks for going up.
                if direction > 0:

                    # Can move, unless it would lead us further than the last page.
                    if not (self.page + direction) > self.getPages()[1]:
                        return True

                # Checks for going down.
                elif direction < 0:

                    # Can move, unless we're on the first page.
                    if self.page > 0:
                        return True

            # Not given a number.
            except TypeError:
                raise Exception("changePage() got invalid direction.")

            # If we get here, it means the check did not pass.
            return False

        # Returns tuple of two ints - (Current Page, Final Page).
        # This shows the page indexes when counting from 1 rather than 0,
        # for the purposes of printing.
        def getPagesRepr(self):

            firstPage, lastPage = self.getPages()

            return (firstPage + 1, lastPage + 1)

        ################################################
        ## Calculations used by the Inventory Screen
        ################################################

        # Calculates how many cells on a page by doing
        # width * height of the grid.
        def getSize(self):

            return self.width * self.height

        # Returns Items from the current page.
        def getPageItems(self):

            # bottomLimitIndex is the Index of the first item on the page.
            # Simply put, it's 0 on page 0, 8 on page 1, 17 on page 2 etc...
            bottomLimitIndex = self.page * self.getSize()

            # topLimitIndex is the last possible index that can be included in the slice.
            # Slicing past the last index throws an IndexError.
            # Usually, the topLimitIndex is just the size of a page...
            topLimitIndex = self.page * self.getSize() + self.getSize()

            # ...Unless the page is not full, which can happen only on the last page.
            # That means it will only get the remaining items. 
            if topLimitIndex > len(self.inventory.keys()) - 1:
                topLimitIndex = len(self.inventory.keys()) - 1 + 1

            # Returns Items between bottomLimitIndex and topLimitIndex.
            #
            # For example:
            # On a full page with index 1, the slice is [9 : 18].
            # (Returns indexes 10 to 18 due to slice rules.)
            #
            # Another example:
            # On the last page with index 2 that has 4 items, 
            # the slice is [18 : 22], indexes 19, 20, 21 and 22.
            return list(self.inventory.keys())[ bottomLimitIndex : topLimitIndex ]

        # Takes the amount of Items on the current page and calculates
        # how many slots on the page will be empty.
        def getEmptyCells(self):

            # Get the current and the last page.
            pages = self.getPages()

            # Unless this is the only page...
            if not pages[0] == 0:

                # ...only the last page can be not full.
                # As such, we can ignore other pages:
                if pages[0] != pages[1]:
                    return 0

            # Otherwise:
            return self.getSize() - len( self.getPageItems() )

        # Returns how many of given item are in present inventory.
        # int, 0 if the item isn't present.
        def getItemCount(self, item):

            if item in self.inventory.keys():

                return self.inventory[item]

            return 0

init -850:

    # Default of the Inventory.
    default Inventory = InventoryObject()