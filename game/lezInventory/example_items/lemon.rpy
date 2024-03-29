# Lemon is an Equippable Item.
# When equipped, it hides all the other Items in the Inventory.
# When unequipped, it returns it back to the original.

init -800 python:

    # Inventory is an OrderedDict, we need it to recreate it.
    from collections import OrderedDict

    # Class of the Lemon.
    class Lemon(Item):

        # This marks the Item as equippable.
        equippable = True

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # In this case, we need the prepare the variable that remembers the inventory state.
        def __init__(self, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Lemon, self).__init__( *args, **kwargs )

            # Prepares a little memory that will temporarily remember the Inventory's state. 
            self.inventory = OrderedDict()

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Remembers the current Inventory state...
            self.inventory = Inventory.inventory

            # ...before clearing it...
            Inventory.inventory = OrderedDict()

            # ...and keeping only the lemon.
            Inventory.inventory[self] = 1

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Loads up the original Inventory state back into the Inventory.
            Inventory.inventory = self.inventory

# Lemon defined.
default lemon = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" )