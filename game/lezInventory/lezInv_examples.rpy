default addWhichItems = "basic"

init -750 python:

    # Because Inventory is created with the help of
    # the "default" statement, we can't interact with it during the init phase.

    # Because of that, we'll prepare this function to insert all
    # the example items, and add it to a callback so it gets automatically
    # ran when the game starts.

    def addExampleItems():

        if store.addWhichItems == "basic" or store.addWhichItems == "both":
            addBasicItems() 

        if store.addWhichItems == "advanced" or store.addWhichItems == "both":
            addAdvancedItems()

    def addBasicItems():

        # Equippables
        Inventory.add(durian)
        Inventory.add(apple)

        # Passives
        Inventory.add(orange, count = 2579)

        Inventory.add(cherries)
        # Inventory.add(cranberries)
        Inventory.add(kiwi)
        Inventory.add(strawberry)

        # Usables
        Inventory.add(dragonFruit)
        Inventory.add(passionFruit)
        Inventory.add(plum, count = 2)
        Inventory.add(grapefruit)

    def addAdvancedItems():

        # Equippables
        Inventory.add(grapes)
        Inventory.add(lemon)

        # Passives

        # Usables
        Inventory.add(guava)
        Inventory.add(apricot)
        Inventory.add(wmelon)
        Inventory.add(peach1)
        Inventory.add(peach2)
        Inventory.add(peach3)
        Inventory.add(fig)

    def resetInventory():

        Inventory.clear()

        addExampleItems()

    if addExampleItems not in config.start_callbacks:
        config.start_callbacks.append(resetInventory)