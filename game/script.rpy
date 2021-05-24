# The game starts here.

label start:

    # From example_items.rpy, adds pre-defined Items.
    $ addExampleItems()

    # Call the Inventory Screen.
    call screen inventoryScreen

    return
