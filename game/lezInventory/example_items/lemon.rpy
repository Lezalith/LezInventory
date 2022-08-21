# Lemon is an Equippable Item.
# When equipped, it hides all the other Items in the Inventory.
# When unequipped, it returns it back to the original.

init -800 python:

    # Class of the Lemon.
    class Lemon(Item):

        # This marks the Item as equippable.
        equippable = True

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # But in this case, we do - we need the memory.
        def __init__(self, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Lemon, self).__init__( *args, **kwargs )

            # Prepares a little memory that will temporarily remember the Inventory's state. 
            self.selectedSlot = None
            self.equippedSlot = None
            self.inventory = None

        # What happens when the Item is Equipped
        def equipped(self, InventoryObject):

            # Remembers the current Inventory state...
            self.selectedSlot = InventoryObject.selectedSlot
            self.equippedSlot = InventoryObject.equippedSlot
            self.inventory = InventoryObject.inventory

            # ...before clearing it out.
            InventoryObject.selectedSlot = 0
            InventoryObject.equippedSlot = 0
            InventoryObject.inventory = [self]

        # What happens when the Item is Unequipped
        def unequipped(self, InventoryObject):

            # Loads up the original Inventory state back into the Inventory.
            
            InventoryObject.selectedSlot = self.selectedSlot
            # Inventory.equippedSlot will get changed by Inventory.unequip anyway
            InventoryObject.inventory = self.inventory

    # Lemon defined.
    lemon = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" )