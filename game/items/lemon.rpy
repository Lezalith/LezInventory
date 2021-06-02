init -800 python:

    # Class of the Lemon.
    class Lemon(EquippableItem):

        # What happens upon the definition.
        def __init__(self, name, desc, image = None):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less
            # arguments that should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(Lemon, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

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
    lemon = Lemon( "Lemon" , "Not good in combination with other fruits." , "images/15_Lemon.png" )