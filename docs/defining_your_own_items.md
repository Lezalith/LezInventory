# Passive Items
For Items that aren't usable or equippable, you can simply define a new **Item** object.
```py
default cherries = Item( "Cherries" , "Spit the seeds at your foes!")
```
There are two arguments that always have to be provided, the name and description of the Item.
**Item** can additionally be given several keyword arguments.
```py
default orange = Item( "Orange" , "Lezalith's massive stash of oranges for making juice." , 
	                  image = "lezInventory/example_items/images/17_Orange.png" ,
	                  stackable = True, 
	                  stack_size = 2579)
```
- **image** is the image representing the item. The argument follows usual Ren'Py image rules - it can be a Displayable, a string with a path to an image file, or a string corresponding to an **image** statement. It is **None** by default, which creates a Text displayable with the Item's **name**.
- **stackable** is **False** by default. Setting it to **True** makes the Item stackable, meaning multiples of it can be in one inventory slot.
- **stack_size** is **1** by default and ignored completely if **stackable** is **False**. It sets how many of this Item can be on the stack. EXCESS ITEMS ARE DISCARDED.

# Functional Items
For Items that are usable, equippable or both, you need to define a new Class, subclassed from **Item**. This involves Python code, however I've simplified it to a point where even a Python beginner can do it with their eyes closed!

## Simplest Usable Item
This is an example of the simplest usable Item possible. First, we create a new class, after which we can define the Item with that class.
You can use this as a template when creating your own Items.
```py
# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # New class for the custom Item.
    #### You have to give it a different name. It can be anything,
    #### since the Item's name is provided once it's defined.
    class ExampleItem(Item):

        # This marks the Item as usable.
        usable = True

        # __init__ got ommited, as this Item doesn't take/need any extra arguments.
        #### (Explained below.)

        # What happens when the Item is used.
        #### This is where you want to put your own functionality.
        def used(self, Inventory):

            # Show a screen that's defined somewhere.
            return renpy.show_screen("dragonScreen")
            
default exampleVersionDragonFruit = ExampleItem( "Dragon Fruit" , "White as snow on the inside.", 
                                    image = "lezInventory/example_items/images/07_Dragonfruit.png" )
```
Inside an **init python** block, a new class is defined. Having the **usable** class variable set to **True** allows the Item to be **Used** inside the Inventory screen. 
When the Item is used, it's **used** method is called - that's where you put everything the Item does! It does have to be Python code only - check all the example Fruit Items, they'll show you the Python way of doing the basic stuff, like calling a label or showing a screen.
- The **used** method is given the **Inventory** argument. This is the **Inventory** object that used the Item, and is passed to allow for easier interaction with the Inventory.

There are more variables usable Items can utilize, they are described below.
## Simplest Equippable Item
Equippable items are created in the exact same way - a new class subclassed from **Item**. Here is an example of the simplest possible equippable Item.
Once again, this can be used as a template for your own use.
```py
# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # New class for the custom Item.
    #### You have to give it a different name.
    class ExampleItem(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.
        #### (Explained below.)

        # What happens when the Item is Equipped
        #### This is where you want to put your own functionality.
        def equipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        #### This is where you want to put your own functionality.
        def unequipped(self, Inventory):

            # Bring up a Notify with a different custom text.
            return renpy.notify("Long live the king...")
            
default exampleVersionApple = ExampleItem( "Apple" , "The King of all the fruits.", 
                                    image = "lezInventory/example_items/images/16_Apple.png" )
```
You should instantly see the similarity. The only difference is that this time, the **equippable** class variable is set to **True** instead. Once that's done, it can be equipped inside the Inventory screen.
Equipping it inside the Inventory screeen calls the Item's **equipped** method, and unequipping it calls the **unequipped** method. They function in the same way as **used** method does - Python code only, Inventory object passed.

If you don't want the Item to do anything on being unequipped, the **unequipped** method can be omitted. It's possible to do the opposite, too - omit the **equipped** method and have the Item only do something on being unequipped.
## Full Item Class
As you may have figured by now, the custom Item is basically put together like a puzzle. Here is the entirety of the class - it covers everything that the Item can do, and what it does by default. Simply take anything you need and overwrite it in your own class, like we did in the two examples above. 

The entire block is explained below.
```py
# init python is python code that runs when the game is launched (init stands for initialization).
init python:

    # New class for the custom Item.
    #### You have to give it a different name.
    class ExampleItem(Item):

        # This marks the Item as usable.
        usable = False

        # This marks the Item as equippable.
        equippable = False

        # States whether the Item should be removed upon being used.
        consumed_on_use = lezInv_settings.consumed_on_use

        # States whether the Item should be removed upon being unequipped.
        consumed_on_unequip = lezInv_settings.consumed_on_unequip

        # __init__ that takes care of setting up the default Item stuff, while allowing custom functionality.
        #  If no custom functionality is needed, __init__ can be ommited completely.
        # Here is how you would allow for this Item to take a new argument.
        def __init__(self, exampleArgument, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            #### Class name given to `super` has to be the same name as is this class. 
            super(ExampleItem, self).__init__( *args, **kwargs )

            #### I just store the exampleArgument in a variable that does nothing.
            self.exampleVariable = exampleArgument

        # What happens when the Item is used.
        #### Does nothing by default.
        def used(self, Inventory):
            pass

        # What happens when the Item is Equipped
        #### Does nothing by default.
        def equipped(self, Inventory):
            pass

        # What happens when the Item is Unequipped
        #### Does nothing by default.
        def unequipped(self, Inventory):
            pass
```
While commented, here is an overview of the code:
- **usable** class variable can be set to **True**. This allows the Item to be used inside the Inventory screen, which calls the **used** method. It needs to be overwritten, as it does nothing by default.
- **equippable** class variable can be set to **True**. This allows the Item to be equipped and unequipped inside the Inventory screen, calling the **equipped** and **unequipped** methods, respectively.
- **consumed_on_use** can be set to **True** or **False**. This determines whether the Item is removed from the Inventory once its **used** method is called. Default is taken from the **lezInv_settings.consumed_on_use** variable, defined in **lezInv_settings.rpy**. 
- **consumed_on_unequip** can be set to **True** or **False**. This determines whether the Item is removed from the Inventory once its **unequipped** method is called. Default is taken from the **lezInv_settings.consumed_on_unequip** variable, defined in **lezInv_settings.rpy**. 
- The **__init__** method can often be omitted. It is called when the Item is defined, and needs to be included only when you need additional functionality, like allowing for a new argument (like in the block above) or setting up complicated stuff (The **Lemon** Fruit Item is an example of this).