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
    # Inventory Class
    #
    ###########################################
    ###########################################

    # Inventory uses Indexes. 
    # Indexes are counted from 0 rather than from 1.
    #
    # Index 0 in the inventory means 1st item, 
    # Index 1 second item, 2 third item and so on...
    # 
    # Same thing for pages. In here, page = 0 means the first page,
    # page 1 is the second, 2 is the third.
    # 
    # The ONLY time when this is not true is in the get_pages_repr method,
    # which gives you the "real" number rather than the index.
    # That is the one that should be used for printing purposes.

    class Inventory(object):

        "Inventory that holds all the items and manages them."

        def __init__(self):
 
            # In slots, width and height of the Inventory.
            self.width = lezInv_settings.width
            self.height = lezInv_settings.height

            # INDEX of the page that we're on.
            self.page = 0

            # OrderedDict. Keys are Item objects, Values are Ints representing a count.
            self.inventory = OrderedDict()

            # Currently selected Item (Key of self.inventory).
            self.selected_item = None

            # Currently equipped Item (Key of self.inventory)
            self.equipped_item = None

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

            # Check whether the count hasn't gone over Item's stack_size.
            if self.inventory[item] > item.stack_size:

                # Set it to max value if it has.
                self.inventory[item] = item.stack_size

        # Removes an Item from the inventory.
        # If item is not specified, it will remove the selected item,
        # unless there isn't one selected, in which case it does nothing.
        # If count is not 0 and the item is stackable, it will instead remove
        # the stacks, and only the Item if the stack goes below 1.
        def remove(self, item = None, count = 1):

            # Attempt to use the SelectedItem if item is not provided.
            if item == None:

                # Do nothing if nothing is selected
                if self.selected_item == None:
                    return

                item = self.selected_item

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
                    self.check_pages()

            # Unstackable Item
            else:

                # Unequip if this Item was equipped
                if item == self.equipped_item:
                    self.unequip()

                # # Unselect this item
                # print("Unselected.")
                self.unselect()

                # Completely remove the Item from the inventory.
                del self.inventory[item]

            # Check pages whether we don't have
            # (an) empty one(s) after the removal.
            self.check_pages()

        # Clears the whole inventory.
        def clear(self):

            self.inventory = OrderedDict()
            self.equipped_item = None
            self.selected_item = None
            self.page = 0

        # Lets us read inventory with Inventory.items
        @property
        def items(self):
            return self.inventory

        ####################################################################
        ## Selection of Items
        ####################################################################

        # Selects an Item.
        def select(self, item):

            # If given item is already selected.
            if self.selected_item == item:

                # Unselect it, and with that end this function.
                return self.unselect()

            # Set the item as selected.
            self.selected_item = item

        # Unselects the selected item.
        def unselect(self):

            self.selected_item = None

        # Lets us read selected_item with Inventory.selected
        @property
        def selected(self):
            return self.selected_item

        ###############################
        ## Equipping and Using of Items
        ###############################

        # Equips an Item.
        # If item is not given, tries to equip currently selected_item.
        # If item is given, a specific item is Equipped, being added into
        # inventory in the process if it's not already present.
        def equip(self, item = None):

            # Specific item not given.
            if not item:

                # Do nothing if nothing is selected.
                if not self.selected_item:
                    return

                # Refer to the selected_item.
                item = self.selected_item

            # Specific item given.
            else:

                # Add it to the Inventory, if it's not present.
                if not item in self.inventory.keys():
                    self.add(item)

            # (Continue with the equip process.)

            # Something was already equipped.
            if self.equipped_item != None:

                # Unequip it first.
                self.unequip()

            # Call Item's equipped() method.
            item.equipped(Inventory = self)

            # Set the Item as equipped.
            self.equipped_item = item

        # Unequip currently equipped Item.
        def unequip(self):

            # Do nothing if nothing is equipped.
            if self.equipped_item == None:
                return

            # Call Item's unequipped() method.
            self.equipped_item.unequipped(self)

            # Store the item so we can unequip it.***
            i = self.equipped_item

            # Set Item equipped to None.
            self.equipped_item = None

            # Check if the item is supposed to be consumed.
            if i.consumed_on_unequip:

                # Remove the Item from the Inventory.
                # *** It cannot just be self.equipped_item, since remove() will call unequip() again.
                self.remove(i)

                # TODO: Create an example on consumed_on_unequip.

        # Use an Item.
        # If item is not given, tries to use currently selected_item.
        # If item is given, a specific item is Used. It doesn't have to be present in the Inventory.
        def use(self, item = None):

            # Specific item given.
            if item:

                # Call Item's used() method.
                return item.used(self)

            # Do nothing if nothing is selected.
            if not self.selected_item:
                return

            # Call Item's used() method.
            self.selected_item.used(self)

            # An extra check whether an Item is still selected, in case the Item's
            # effect messed around with it. Guava Item is a good example of that.
            if self.selected_item:

                # Check if the item is supposed to be consumed.
                if self.selected_item.consumed_on_use:

                    # Remove the Item from the Inventory.
                    self.remove()

        # Lets us read equipped_item with Inventory.equipped
        @property
        def equipped(self):
            return self.equipped_item

        ##################################################
        ## Checks, used mostly in the Inventory Screen
        ##################################################

        # Whether an item is present in inventory.
        def is_in_inventory(self, item):

            return item in self.inventory.keys()

        # Whether given item is currently selected.
        def is_selected(self, item):
            
            return self.selected_item == item

        # Whether given item is currently equipped.
        def is_equipped(self, item):
            
            return self.equipped_item == item

        # Whether currently equipped item can be unequipped.
        # Returns True if the equipped item is also the one currently selected.
        def can_unequip(self):

            return self.selected_item == self.equipped_item

        # Whether an item can be equipped.
        # Returns True if an equippable item is currently selected.
        def can_equip(self):

            # If an Item is selected.
            if self.selected_item != None:

                # Check the equippable property.
                return self.selected_item.is_equippable()

            # If an Item isn't selected.
            return False 

        # Whether an item can be used.
        # Returns True if a usable item is currently selected.
        def can_use(self):

            # If an Item is selected.
            if self.selected_item != None:

                # Check the usable property.
                return self.selected_item.is_usable()

            # If an Item isn't selected.
            return False 

        ###################
        ## Page Functions
        ###################

        # Returns the index of the current page.
        def get_current_page(self):
            return self.page

        # Returns tuple of two ints - (Current Page INDEX, Final Page INDEX ).
        def get_pages(self):

            # Calculate how many pages are there.
            last_page = (len(self.inventory) - 1) // self.get_size()

            # A safe check. 
            if last_page < 0:
                last_page = 0

            # First is the current page index, second is the last page index.
            return ( self.page, last_page )

        # Check whether we've not stayed on an empty page.
        def check_pages(self):

            pages = self.get_pages()

            # If the page we're on currently is over the total amount of pages...
            if pages[0] > pages[1]:

                # ...put us onto the last page.
                self.page = pages[1]

        # Moving up or down between pages. 1 goes up a page, -1 down a page.
        # You can move multiple pages, but it won't let you go to an empty one.
        def change_page(self, direction):

            # Check whether the move can be executed.
            if not self.can_change_page(direction):
                return None

            # Change the page.
            self.page += direction

            # Finally, unselect whatever's selected.
            # This is debatable, but I don't think Item's name and description should be
            # shown if you can't see the selected Item, since it's on a different page.
            self.unselect()

        # Checks whether we can move between pages.
        # Moving is possible as long as we're not going past the first
        # or past the final page.
        def can_change_page(self, direction):

            # Only on one page - Cannot move anywhere.
            if self.get_pages()[1] == 0:
                return False

            # Try changing the page.
            try:

                # Checks for going up.
                if direction > 0:

                    # Can move, unless it would lead us further than the last page.
                    if not (self.page + direction) > self.get_pages()[1]:
                        return True

                # Checks for going down.
                elif direction < 0:

                    # Can move, unless we'd go below the first page.
                    if self.page > 0:
                        return True

            # Not given a number.
            except TypeError:
                raise Exception("change_page() got invalid direction.")

            # If we get here, it means the check did not pass
            # and the page cannot be changed.
            return False

        # Returns tuple of two ints - (Current Page, Final Page).
        # This shows the page indexes when counting from 1 rather than 0,
        # for the purposes of printing.
        def get_pages_repr(self):

            first_page, last_page = self.get_pages()

            return (first_page + 1, last_page + 1)

        ################################################
        ## Calculations used by the Inventory Screen
        ################################################

        # Calculates how many cells on a page by doing
        # width * height of the grid.
        def get_size(self):

            return self.width * self.height

        # Returns Items from the current page.
        def get_page_items(self):

            # bottom_limit_index is the Index of the first item on the page.
            # Simply put, it's 0 on page 0, 8 on page 1, 17 on page 2 etc...
            bottom_limit_index = self.page * self.get_size()

            # top_limit_index is the last possible index that can be included in the slice.
            # Slicing past the last index throws an IndexError.
            # Usually, the top_limit_index is just the size of a page...
            top_limit_index = self.page * self.get_size() + self.get_size()

            # ...Unless the page is not full, which can happen only on the last page.
            # That means it will only get the remaining items. 
            if top_limit_index > len(self.inventory.keys()) - 1:
                top_limit_index = len(self.inventory.keys()) - 1 + 1

            # Returns Items between bottom_limit_index and top_limit_index.
            #
            # For example:
            # On a full page with index 1, the slice is [9 : 18].
            # (Returns indexes 10 to 18 due to slice rules.)
            #
            # Another example:
            # On the last page with index 2 that has 4 items, 
            # the slice is [18 : 22], indexes 19, 20, 21 and 22.
            return list(self.inventory.keys())[ bottom_limit_index : top_limit_index ]

        # Takes the amount of Items on the current page and calculates
        # how many slots on the page will be empty.
        def get_empty_cells(self):

            # Get the current and the last page.
            pages = self.get_pages()

            # Unless this is the only page...
            if not pages[0] == 0:

                # ...only the last page can be not full.
                # As such, we can ignore other pages:
                if pages[0] != pages[1]:
                    return 0

            # Otherwise:
            return self.get_size() - len( self.get_page_items() )

        # Returns how many of given item are in present inventory.
        # int, 0 if the item isn't present.
        def get_item_count(self, item):

            # If the Item is present in the Inventory...
            if item in self.inventory.keys():

                # ...return it's count.
                return self.inventory[item]

            # 0 if the Item given isn't present.
            return 0

init -850:

    # Default of the Inventory.
    # The Alpha and Omega.
    # The Beginning and the End.
    # ...
    # (Warwarneverchanges)
    default inventory = Inventory()