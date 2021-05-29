init -800 python:

    class Lemon(EquippableItem):

        "Class for usable Items."

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

            self.selectedSlot = None
            self.equippedSlot = None
            self.inventory = None

        def equipped(self):

            self.selectedSlot = Inventory.selectedSlot
            self.equippedSlot = Inventory.equippedSlot
            self.inventory = Inventory.inventory

            Inventory.selectedSlot = 0
            Inventory.equippedSlot = 0
            Inventory.inventory = [self]

        def unequipped(self):

            Inventory.selectedSlot = self.selectedSlot
            # Inventory.equippedSlot will get changed by Inventory.unequip anyway
            Inventory.inventory = self.inventory

    lemon = Lemon( "Lemon" , "Not good in combination with other fruits." , "images/15_Lemon.png" )