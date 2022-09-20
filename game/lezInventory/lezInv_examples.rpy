default add_which_items = "basic"

init -750 python:

    # Because Inventory is created with the help of
    # the "default" statement, we can't interact with it during the init phase.

    # Because of that, we'll prepare this function to insert all
    # the example items, and add it to a callback so it gets automatically
    # ran when the game starts.

    def add_example_items():

        if store.add_which_items == "basic" or store.add_which_items == "both":
            add_basic_items() 

        if store.add_which_items == "advanced" or store.add_which_items == "both":
            add_advanced_items()

    def add_basic_items():

        # Equippables
        inventory.add(durian)
        inventory.add(apple)

        # Passives
        inventory.add(orange, count = 2579)

        inventory.add(kiwi)
        inventory.add(strawberry)

        # Usables
        inventory.add(dragonFruit)
        inventory.add(passionFruit)
        inventory.add(plum, count = 2)
        inventory.add(pear)
        inventory.add(grapefruit)

    def add_advanced_items():

        # Equippables
        inventory.add(grapes)
        inventory.add(lemon)

        # Both Equippable and Usable
        inventory.add(cranberries)

        # Usables
        inventory.add(cherries, count = 250)
        inventory.add(guava)
        inventory.add(apricot)
        inventory.add(wmelon)
        inventory.add(peach1)
        inventory.add(peach2)
        inventory.add(peach3)
        inventory.add(fig)

    def reset_inventory():

        inventory.clear()

        add_example_items()

    if add_example_items not in config.start_callbacks:
        config.start_callbacks.append(reset_inventory)