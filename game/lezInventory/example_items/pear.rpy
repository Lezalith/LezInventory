# Plum is a Usable Item.
# When Used, its image will change into one of 8 random images.

init -800 python:

    from random import randrange

    # Class of the WMelon.
    class Pear(Item):

        # This marks the Item as usable.
        usable = True

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # In this case we need it to take and remember all the images.
        def __init__(self, images = [], *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Pear, self).__init__( *args, **kwargs )

            # List of multiple possible images.
            self.images = images

            # Index of the currently selected image, always starting with the first one.
            self.current_index = 0

            # Image used by the item, picked from images via current_index.
            self.image = self.images[self.current_index]

        # consumed_on_use = False
        # This would be set, as I do not want the item being consumed,
        # however, it gets unselected in the used method, which prevents the Inventory
        # from removing it like it normally would. Guava also do this.

        # Change this item's image to a new one at random.
        def change_image(self):

            ##### Generating the new, random index #############

            # 8 Tries to generate a different image than there currently is.
            # Only 8 tries to not affect performance, in case we'd get REALLY unlucky.
            for x in range(8):

                # Index of new image from the list
                i = randrange(0, len(self.images))

                # Last image is a special case:
                # It has additionaly reduced chance of being picked.
                if i == len(self.images) - 1:

                    # Here is a 50/50 chance to keep the special image.
                    if randrange(0, 2) == 1:

                        # If it doesn't pass, reroll instantly, giving the special image
                        # one more chance to be selected.
                        i = randrange(0, len(self.images))

                # If it's different from the current one, use it.
                # Otherwise, try the roll again.
                if i != self.current_index:
                    break

            ####################################################

            # Records the new picked image index.
            self.current_index = i

            # Updates the image according to the new index.
            self.image = self.images[self.current_index]

        # What happens when the Item is used.
        def used(self, Inventory):

            # Changes its own image.
            self.change_image()

            # Unselect this item, so that it doesn't get removed.
            # consumed_on_use = False would do it, but the item would stay selected,
            # I don't want that.
            Inventory.unselect()

# Pear defined.
default pear = Pear( name = "Pear", desc = "Every bite has a different,\nbut always sweet taste.", stackable = True, stack_size = 9999,
                     images = ["lezInventory/example_items/images/18_Pear.png",
                               "lezInventory/example_items/images/18_Pear_1.png",
                               "lezInventory/example_items/images/18_Pear_2.png",
                               "lezInventory/example_items/images/18_Pear_3.png",
                               "lezInventory/example_items/images/18_Pear_4.png",
                               "lezInventory/example_items/images/18_Pear_5.png",
                               "lezInventory/example_items/images/18_Pear_6.png",
                               "lezInventory/example_items/images/18_Pear_7.png",
                               "lezInventory/example_items/images/18_Pear_8.png"] )