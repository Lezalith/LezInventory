# The game starts here.

label start:

    # From example_items.rpy, adds pre-defined Items.
    $ addExampleItems()

    "This is a line the Inventory."

    # Call the Inventory Screen.
    call screen inventoryScreen

    "This is a line after the Inventory."

    return
