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
        inventory.add(durian)
        inventory.add(apple)

        # Passives
        inventory.add(orange, count = 2579)

        inventory.add(cherries)
        # inventory.add(cranberries)
        inventory.add(kiwi)
        inventory.add(strawberry)

        # Usables
        inventory.add(dragonFruit)
        inventory.add(passionFruit)
        inventory.add(plum, count = 2)
        inventory.add(grapefruit)

    def addAdvancedItems():

        # Equippables
        inventory.add(grapes)
        inventory.add(lemon)

        # Passives

        # Usables
        inventory.add(guava)
        inventory.add(apricot)
        inventory.add(wmelon)
        inventory.add(peach1)
        inventory.add(peach2)
        inventory.add(peach3)
        inventory.add(fig)

    def resetInventory():

        inventory.clear()

        addExampleItems()

    if addExampleItems not in config.start_callbacks:
        config.start_callbacks.append(resetInventory)