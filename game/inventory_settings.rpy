init -920 python:

    # This is the class that contains the most important settings.
    # While you can customize a LOT of things in the styles below, 
    # if you're happy with the default layout, you can just change these
    # settings and start using the Inventory straight away.
    class InventorySettings():

        def __init__(self):

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
            self.slotFullIdle = Frame("inventory/gui/slot.png", 6, 6, 6, 6)
            self.slotFullHover = Frame("inventory/gui/slot.png", 6, 6, 6, 6)
            self.slotFullSelected = Frame("inventory/gui/slot_selected.png", 6, 6, 6, 6)
            self.slotFullSelectedHover = Frame("inventory/gui/slot_selected.png", 6, 6, 6, 6)

            # Background of an Inventory Slot that is empty.
            self.slotEmptyIdle = Frame("inventory/gui/slot.png", 6, 6, 6, 6)
            self.slotEmptyHover = Frame("inventory/gui/slot.png", 6, 6, 6, 6)

    InventorySettings = InventorySettings()