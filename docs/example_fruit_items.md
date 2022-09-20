Here is a complete overview of all the example fruit items included in this project, what they do and their complete code.

The list is in the same order as the items inside the inventory.
# Durian
![08_Durian](https://user-images.githubusercontent.com/56970124/190860059-4e5d8ae3-585e-41e4-a40e-bda869a1dd1c.png)

Durian is an equippable item, showing how an item can show a single image.

The image in question is a **Solid Displayable** with a green color, shown at 33% transparency.
The image is shown upon equipping Durian, and hidden upon unequipping it.
```py
init -800 python:

    # Class of the Durian.
    class Durian(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Show a Solid color over the entire screen.
            return renpy.show( "NoTag", layer = "screens", zorder = 20, what = Solid( "32CD3233" ) , tag = "durTag", at_list = [ Transform(alpha = 0.33) ] )

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Remove the Solid color.
            return renpy.hide("durTag", "screens")

    # Durian defined.
default durian = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )
```
# Apple
![16_Apple](https://user-images.githubusercontent.com/56970124/190860265-e5fcb435-be26-42c6-8421-a552d75e90b9.png)

Apple is the simplest equippable item there can be.

Upon being equipped, it calls the **renpy.notify** function, which shows a frame with a message.
Upon being unequipped, same function is used to display a different message.
```py
init -800 python:

    # Class of the Apple.
    class Apple(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("I have been crowned the King of all Fruits!")

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Bring up a Notify with a custom text.
            return renpy.notify("Long live the king...")

# Apple defined.
default apple = Apple( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )
```
# Orange
![17_Orange](https://user-images.githubusercontent.com/56970124/190860403-8997c4bc-0411-46ee-a277-880745cf781b.png)

Orange is a passive item, not usable nor equippable.

However, it is stackable, with many Oranges present in the inventory. I dare you to throw them all away.
```py
default orange = Item( "Orange" , "Lezalith's massive stash of oranges for making juice." , image = "lezInventory/example_items/images/17_Orange.png" , stackable = True, stack_size = 2579)
```
# Cherries
![01_Cherry_Red](https://user-images.githubusercontent.com/56970124/190860521-79a1b350-568f-4d7f-85e8-0d61c2f86f88.png)

Cherries are a passive item, not usable nor equippable.
```py
default cherries = Item( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png" )
```
# Kiwi
![14_Kiwi](https://user-images.githubusercontent.com/56970124/190860587-0eb1e321-74f3-4d9c-be6b-718bed82e939.png)

Kiwi is a passive item, not usable nor equippable.
```py
default kiwi = Item( "Kiwi" , "Great as a tea with strawberries." , "lezInventory/example_items/images/14_Kiwi.png" )
```
# Strawberry
![22_Strawberry](https://user-images.githubusercontent.com/56970124/190860623-cf2949b4-9f97-4688-a5b4-98ce7e99dc9b.png)

Strawberry is a passive item, not usable nor equippable.

```py
default strawberry = Item( "Strawberry" , "Great as a tea with kiwis." , "lezInventory/example_items/images/22_Strawberry.png" )
```
# Dragon Fruit
![07_Dragonfruit](https://user-images.githubusercontent.com/56970124/190860719-021ce385-d810-4648-a6aa-ca0c02c17442.png)

Dragon Fruit is a simple usable item.

When used, it shows a defined **screen**.

```py
init -800 python:

    # Class of the Dragon Fruit.
    class dragonF(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Show a screen.
            return renpy.show_screen("dragon_screen")

# Dragon Fruit defined.
default dragonFruit = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png")

# Screen that we'll show by Using the Item.
screen dragon_screen():

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)

        # Short trivia text, as well as a button to close this screen.
        vbox:
            text "Did you know that Dragon Fruit is actually called Pitahaya?"
            textbutton "Glad to know!" action Hide("dragon_screen") xalign 0.5
```
# Passion Fruit
![20_Passionfruit](https://user-images.githubusercontent.com/56970124/190860773-c7248a6d-9523-4476-9654-df37ed2953b1.png)

Passion Fruit is a simple usable item.

When used, it calls a **label**.

```py
init -800 python:

    # Class of the Passion Fruit.
    class passionF(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Enter the passionF_label label defined above.
            # The function might look scary, but to us, it's like a regular call.
            return renpy.call_in_new_context("passionF_label")

# Passion Fruit defined.
default passionFruit = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )

# Label that we'll enter by Using the Item.
label passionF_label():

    "Lezalith" "How tropical are you feeling today?"

    menu:

        "Very tropical!":

            "Lezalith" "Great! I'll add some more passion fruit to your Inventory then!"

            # Adds one more Passion Fruit into the Inventory.
            $ inventory.add( passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" ) )

        "Not tropical at all.":

            "Lezalith" "Aww. That's okay, it will come to you eventually!"

    # Return back to the Inventory.
    return
```
# Plum
![06_Plum](https://user-images.githubusercontent.com/56970124/190860837-3d9af9db-adc9-48e4-b76d-59dc40baeffd.png)

Plum is a stackable usable item.

When used, it checks how many of itself are in the Inventory, and adds a fraction of that number - effectively multiplying itself.

```py
init -800 python:

    # Class of the WMelon.
    class Plum(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.
        consumed_on_use = False

        # What happens when the Item is used.
        def used(self, Inventory):

            # Add (Current count / 5 + 1) Plums to the Inventory.
            Inventory.add( item = self, count = int(Inventory.inventory[self] / 5 + 1) )

    # Plum defined.
    plum = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stack_size = 9999 )
```
# Pear
![18_Pear](https://user-images.githubusercontent.com/56970124/191106028-04293ad6-4d4a-40e4-b2c1-f83b80ef2d94.png)

Pear is a simple usable item, one of the three with overwritten **__init__** method, like Cranberries or Lemon.

When used, changes the image of the item.

```py
init -800 python:

    from random import randrange

    # Class of the WMelon.
    class Pear(Item):

        # This marks the Item as usable.
        usable = True

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # In this case we need it to take and remember all the images.
        def __init__(self, images = [], *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Pear, self).__init__( *args, **kwargs )

            # List of multiple possible images.
            self.images = images

            # Index of the currently selected image, always starting with the first one.
            self.current_index = 0

            # Image used by the item, picked from images via current_index.
            self.image = self.images[self.current_index]

        # consumed_on_use = False
        # This would be set, as I do not want the item being consumed,
        # however, it gets unselected in the used method, which prevents the Inventory
        # from removing it like it normally would. Guava also do this.

        # Change this item's image to a new one at random.
        def change_image(self):

            ##### Generating the new, random index #############

            # 8 Tries to generate a different image than there currently is.
            # Only 8 tries to not affect performance, in case we'd get REALLY unlucky.
            for x in range(8):

                # Index of new image from the list
                i = randrange(0, len(self.images))

                # Last image is a special case:
                # It has additionaly reduced chance of being picked.
                if i == len(self.images) - 1:

                    # Here is a 50/50 chance to keep the special image.
                    if randrange(0, 1) == 0:

                        # If it doesn't pass, reroll instantly, giving the special image
                        # one more chance to be selected.
                        i = randrange(0, len(self.images))

                # If it's different from the current one, use it.
                # Otherwise, try the roll again.
                if i != self.current_index:
                    break

            ####################################################

            # Records the new picked image index.
            self.current_index = i

            # Updates the image according to the new index.
            self.image = self.images[self.current_index]

        # What happens when the Item is used.
        def used(self, Inventory):

            # Changes its own image.
            self.change_image()

            # Unselect this item, so that it doesn't get removed.
            # consumed_on_use = False would do it, but the item would stay selected,
            # I don't want that.
            Inventory.unselect()

# Pear defined.
default pear = Pear( name = "Pear", desc = "Every bite has a different,\nbut always sweet taste.", stackable = True, stack_size = 9999,
                     images = ["lezInventory/example_items/images/18_Pear.png",
                               "lezInventory/example_items/images/18_Pear_1.png",
                               "lezInventory/example_items/images/18_Pear_2.png",
                               "lezInventory/example_items/images/18_Pear_3.png",
                               "lezInventory/example_items/images/18_Pear_4.png",
                               "lezInventory/example_items/images/18_Pear_5.png",
                               "lezInventory/example_items/images/18_Pear_6.png",
                               "lezInventory/example_items/images/18_Pear_7.png",
                               "lezInventory/example_items/images/18_Pear_8.png"] )
```
# Grapefruit
![12_Grapefruit](https://user-images.githubusercontent.com/56970124/190860982-b365b54a-7e2c-46cb-996b-f1d725922190.png)

Grapefruit is a simple usable item.

When used, it clears the entire inventory.

```py
init -800 python:

    # Class of the Grapefruit.
    class Grapefruit(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):
            
            # Wipe the Inventory clean.
            Inventory.clear()

# Grapefruit defined.
default grapefruit = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )
```
# Grapes
![11_Grapes_Green](https://user-images.githubusercontent.com/56970124/190861052-d5819c9d-9c38-4071-a98c-ce979fe528f4.png)

Grapes are an equippable item.

Equipping it shows a very chaotic screen with many transforms. Unequipping Grapes hides it again.

```py
init -800 python:

    # Class of the Grapes.
    class Grapes(Item):

        # This marks the Item as equippable.
        equippable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Show the grapes_screen screen.
            return renpy.show_screen("grapes_screen")

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Hide the grapes_screen screen.
            return renpy.hide_screen("grapes_screen")

    # Grapes defined.
    grapes = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )
    

# Screen that we'll show by Using the Item.
screen grapes_screen():

    # Inner frame of the Balls.
    frame:

        background None
        xysize (1250, 1250)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move counter-clockwise,
        # as well as a transform for smooth appear and disappear
        at frame_CC, frame_alpha

        # All the different Balls, spinning clockwise themselves.
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.125) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 0.0) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.125) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.0, 0.5) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (1.0, 0.5) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.875) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 1.0) at grapes_C
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.875) at grapes_C

    # Outer frame of the Balls.
    frame:

        background None
        xysize (2000, 2000)
        align (0.5, 0.5)
        padding (10, 10)
        
        # Makes the frame move clockwise,
        # as well as a transform for smooth appear and disappear
        at frame_C, frame_alpha

        # All the different Balls, spinning counter-clockwise themselves.
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.125) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 0.0) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.125) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.0, 0.5) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (1.0, 0.5) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.125, 0.875) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.5, 1.0) at grapes_CC
        add "lezInventory/example_items/images/11_Grapes_Green.png" align (0.875, 0.875) at grapes_CC

# Transform for smooth appear and disappear
transform frame_alpha():

    on show:
        alpha 0.0
        linear 0.5 alpha 1.0

    on hide:
        alpha 1.0
        easeout 1.0 alpha 0.0 yoffset 300

# Clockwise spin on a frame
transform frame_C():

    rotate 0.0
    linear 15.0 rotate 360.0
    linear 15.0 rotate 0.0
    repeat

# Counter-clockwise spin on a frame
transform frame_CC():

    rotate 0.0
    linear 15.0 rotate -360.0
    linear 15.0 rotate 0.0
    repeat

# Clockwise spin on a grape
transform grapes_C():

    rotate 0.0
    linear 3.0 rotate 360.0
    linear 3.0 rotate 0.0
    repeat

# Counter-clockwise spin on a grape
transform grapes_CC():

    rotate 0.0
    linear 3.0 rotate -360.0
    linear 3.0 rotate 0.0
    repeat
```
# Lemon
![15_Lemon](https://user-images.githubusercontent.com/56970124/190861161-09dc54d5-284e-485b-a919-5349323e4efb.png)

Lemon is a complex equippable item, one of the three with overwritten **__init__** method, like Pear or Cranberries.

When equipped, it clears the entire inventory except for itself in the equip slot. When unequipped, it returns the inventory to its original state.

```py
init -800 python:

    # Inventory is an OrderedDict, we need it to recreate it.
    from collections import OrderedDict

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
            self.inventory = OrderedDict()

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            # Remembers the current Inventory state...
            self.inventory = Inventory.inventory

            # ...before clearing it...
            Inventory.inventory = OrderedDict()

            # ...and keeping only the lemon.
            Inventory.inventory[self] = 1

        # What happens when the Item is Unequipped
        def unequipped(self, Inventory):

            # Loads up the original Inventory state back into the Inventory.
            Inventory.inventory = self.inventory

    # Lemon defined.
    lemon = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" )
```
# Cranberries
![03_Cranberry](https://user-images.githubusercontent.com/56970124/191125583-c69fbc07-a35f-4c84-b993-933206984c1d.png)

Cranberries in the only example fruit item that is both equippable and usable. It is one of the few with overwritten **__init__** method, like Pear or Lemon.

When equipped, it displays a simple message. Does nothing when unequipped. When used, displays a simple screen showing how many times this item has been equipped.

Unlike Peach, Cranberries has its counter set up in the **__init__** method, meaning the counter is not shared between different defined Cranberries items.

```py
init -800 python:

    # Class of the Dragon Fruit.
    class Cranberries(Item):

        # This marks the Item as equippable.
        equippable = True

        # This marks the Item as usable.
        usable = True

        # Do not remove this item on use.
        consumed_on_use = False

        # What happens upon the definition.
        # THIS CAN BE OMMITED, in case *you* don't need something special in the __init__.
        # In this case we need to set up the variable that counts times equipped.
        def __init__(self, *args, **kwargs):

            # Calls the parent class, Item, with everything that it needs.
            super(Cranberries, self).__init__( *args, **kwargs )

            self.counter = 0

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is Equipped
        def equipped(self, Inventory):

            self.counter += 1

            # Bring up a Notify with a custom text.
            return renpy.notify("You eat one berry as you pick the cranberries up.")

        # What happens when the Item is used.
        def used(self, Inventory):

            # Show a screen.
            return renpy.show_screen("cranberries_screen")

# Cranberries defined.
default cranberries = Cranberries( "Cranberries" , "A handful of red berries." , "lezInventory/example_items/images/03_Cranberry.png" )

# Screen that we'll show by Using the Item.
# Basically the same as Dragon Fruit's screen.
screen cranberries_screen():

    # Small frame in the bottom right corner
    frame:

        align (1.0, 1.0)
        padding (10, 10)
        offset (-50, -50)

        # Short trivia text, as well as a button to close this screen.
        vbox:
            text "You've had [cranberries.counter] cranberry berries so far!"
            textbutton "(Hide this)" action Hide("cranberries_screen") xalign 0.5
```
# Guava
![13_Guava](https://user-images.githubusercontent.com/56970124/190861304-ac106701-b674-4238-9ab2-44c038403441.png)

Guava is a complex usable item.

When used, it jumps to a random place in the inventory.

```py
init -800 python:

    # randint lets us choose a random number.
    from random import randint
    # Inventory is an OrderedDict, we need it to recreate it.
    from collections import OrderedDict

    # Class of the Guava.
    class Guava(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # Keep this Item in Inventory even after using it.
        consumed_on_use = False

        # What happens when the Item is used.
        def used(self, Inventory):

            # We cannot change the order of OrderedDict, which is what the Inventory is.
            # So, we'll create a list, copy stuff over there, deal with the Guava functionality, then update the OrderedDict.
            l = list(Inventory.inventory.keys())

            # Find out where the Guava currently is.
            old_index = l.index(self)

            # 5 Tries to generate a different index than where it currently is.
            # Only 8 tries to not affect performance, in case we'd get REALLY unlucky.
            for x in range(8):

                # Generated Index
                new_index = randint( 0 , len(Inventory.inventory.keys()) - 1 )

                # If it's the same index as the original one, try the roll again.
                # If not, use it.
                if new_index != old_index:
                    break        

                # Keep the index if 8 rolls weren't enough.

            # Get rid of original Guava.
            l.pop(old_index)

            # Insert Guava at the generated index..
            l.insert(new_index, self)

            # Prepare a new OrderedDict for the Inventory.
            d = OrderedDict()

            # Insert everything into the prepared OrderedDict.
            # keys are taken from the list which has had order of items changed,
            # values are taken from the original Inventory.
            for key in l:
                d[key] = Inventory.inventory[key]

            # Update Inventory to the new OrderedDict.
            Inventory.inventory = d

            # Unselect the Item, since selection depends on index:
            # If the order changed, a different item would be in place and kept selected.
            Inventory.unselect()

# Guava defined.
default guava = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )
```
# Apricot
![21_Apricot](https://user-images.githubusercontent.com/56970124/190861366-83bb8d4a-59cc-4019-8c09-ede25383a505.png)

Apricot is a usable item.

When used, it calls a label where there is a custom **menu** prepared. In the menu, all the example fruit items are listed. The used Apricot transforms into the fruit selected, keeping it's place in the inventory.

```py
init -800 python:    

    # Class of the Apricot.
    class Apricot(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Enter the apricot_label label defined above.
            # The function might look scary, but to us, it's like a regular call.
            # We pass it this Item, so that the label can figure out which Item to replace in the Inventory.
            return renpy.call_in_new_context("apricot_label", self_item = self)

# Apricot defined.
default apricot = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )


# Label that we'll enter by Using the Item.
label apricot_label(self_item):

    # All of the Menu options define a new Item that will be added.

    menu(screen = "apricot_menu"):
        "Apricot has the ability to transform into any fruit.\nIt will keep it's place in the inventory."

        "Durian.":
            $ r = Durian( "Durian" , "World's smelliest fruit, supposedly." , "lezInventory/example_items/images/08_Durian.png" )

        "Grapes.":
            $ r = Grapes( "Grapes" , "So many balls..." , "lezInventory/example_items/images/11_Grapes_Green.png" )

        "Lemon.":
            $ r = Lemon( "Lemon" , "Not good in combination with other fruits." , "lezInventory/example_items/images/15_Lemon.png" ) 

        "Apple.":
            $ r = Item( "Apple" , "The King of all the fruits." , "lezInventory/example_items/images/16_Apple.png" )

        "Cherries.":
            $ r = Item( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png" )

        "Orange.":
            $ r = Item( "Orange" , "This Inventory's creator is addicted to orange juice." , "lezInventory/example_items/images/17_Orange.png" )

        # "Cranberries.":

        #     $ r = Item( "Cranberries" , "Ever heard of \"Hermelín\"?" , "lezInventory/example_items/images/03_Cranberry.png" )

        "Kiwi.":
            $ r = Item( "Kiwi" , "Great as a tea with strawberries." , "lezInventory/example_items/images/14_Kiwi.png" )

        "Strawberry.":
            $ r = Item( "Strawberry" , "Great as a tea with kiwis." , "lezInventory/example_items/images/22_Strawberry.png" )

        "Dragon fruit.":
            $ r = dragonF( "Dragon Fruit" , "White as snow on the inside." , "lezInventory/example_items/images/07_Dragonfruit.png" )

        "Guava.":
            $ r = Guava( "Guava" , "Kinda random, to be honest." , "lezInventory/example_items/images/13_Guava.png" )

        "Apricot.":
            $ r = Apricot( "Apricot" , "Orange. Sweet. Delicious." , "lezInventory/example_items/images/21_Apricot.png" )

        "Watermelon.":
            $ r = WMelon( "Watermelon" , "So big, almost seems endless. And slippery." , "lezInventory/example_items/images/23_Watermelon.png" )

        "Passion fruit.":
            $ r = passionF( "Passion Fruit" , "About as tropical as you can get." , "lezInventory/example_items/images/20_Passionfruit.png" )

        "Grapefruit.":
            $ r = Grapefruit( "Grapefruit" , "It's so bitter. How can people eat this?" , "lezInventory/example_items/images/12_Grapefruit.png" )

        "Peach...?":
            $ r = Peach( "Peachpricot" , "An intriguing combination\nof peach and apricot.", image = "lezInventory/example_items/images/0X_Peachpricot.png" )

        "Fig.":
            $ r = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png" )

        "Plum.":
            $ r = Plum( "Plum" , "Evergrowing in power, dark like a deep abyss." , "lezInventory/example_items/images/06_Plum.png", stackable = True, stack_size = 9999 )


    # Note: Similar functionality to Guava.
    python:

        # We cannot change the order of OrderedDict, which is what the Inventory is.
        # So, we'll create a list, copy stuff over there, deal with the Guava functionality, then update the OrderedDict.
        l = list(inventory.inventory.keys())

        # Prepare a new OrderedDict for the Inventory.
        d = OrderedDict()

        # Insert everything into the prepared OrderedDict.
        # keys are taken from the list which has had order of items changed,
        # values are taken from the original Inventory.
        for key in l:

            # Once we encounter the index where Apricot is, replace it with the selected item.
            if key == self_item:
                d[r] = 1

            # Otherwise just copy over the info from the original Inventory.
            else:
                d[key] = inventory.inventory[key]

        # Update Inventory to the new OrderedDict.
        inventory.inventory = d

        # Aside from the fact that we don't want the new item selected anyway,
        # finishing of Inventory.used() will throw an error, because of not being able to remove it.
        # Unselecting it prevents this.
        inventory.unselect()

    # Return back to the Inventory.
    return

# A custom choice screen that is used instead of the default one.
# The choices look nicer and are way smaller, since there's so many of them.
screen apricot_menu(items):

    # Still has the same style as default choice screen though
    style_prefix "choice"

    default odd_items = items[::2]
    default even_items = items[1::2]

    # Vbox for all the buttons.
    vbox:

        align (0.5, 0.2)
        spacing 20

        for i, entry in enumerate(even_items):

            hbox:

                spacing 20

                textbutton odd_items[i].caption action odd_items[i].action text_color "000" xsize 700
                textbutton entry.caption action entry.action text_color "000" xsize 700

        # If there was a solo item at the end
        if len(odd_items) > len(even_items):

            hbox:

                xalign 0.5
                
                textbutton odd_items[-1].caption action odd_items[-1].action text_color "000" xsize 700
```
# Watermelon
![23_Watermelon](https://user-images.githubusercontent.com/56970124/190861502-4ace355c-38c0-4220-823f-afe55a980a91.png)

Watermelon is a complex usable item.

When used, it shuffles the order of items in the inventory.

```py
init -800 python:

    # Shuffle randomly shuffles a list.
    from random import shuffle
    # Inventory is an OrderedDict, we need it to recreate it.

    # Class of the WMelon.
    class WMelon(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Create a list that we can shuffle, since we cannot
            # change order of items in OrderedDict.
            l = list(Inventory.inventory.keys())

            # Shuffle the list with the items.
            shuffle(l)

            # Prepare a new OrderedDict.
            d = OrderedDict()

            # Insert everything into the prepared OrderedDict.
            # keys are taken from the list which has had order of items changed,
            # values are taken from the original Inventory.
            for key in l:
                d[key] = Inventory.inventory[key]

            # Update Inventory to the new OrderedDict.
            Inventory.inventory = d

# Watermelon defined.
default wmelon = WMelon( "Watermelon" , "Bouncy enough to hit other items." , "lezInventory/example_items/images/23_Watermelon.png" )
```
# Peach
![19_Peach](https://user-images.githubusercontent.com/56970124/190861633-5c3ba9b2-b6cd-4948-8a6d-cc782d62b6d8.png)

Peach is a usable item.

Upon being used, it shows a message, stating how many Peaches have been used so far. 

This information is stored inside a **class variable**, meaning multiple Peach items with different names and descriptions can be defined and the counter is shared among them.

```py
init -800 python:

    # Class of the Peach.
    class Peach(Item):

        # This marks the Item as usable.
        usable = True

        # Signature function of Peach.
        # How many times an Item of the Peach class has been used.
        how_many_times_used = 0

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # Up the class variable counter.
            Peach.how_many_times_used += 1

            # Show the count.
            if Peach.how_many_times_used != 4:
                renpy.notify("*Munching sounds...*\nYou just ate a peach number {}!".format(Peach.how_many_times_used))

            # Special message in a label instead, on the 4th peach used.
            else:
                renpy.call_in_new_context("peach_label")


# Three different peaches defined.
default peach1 = Peach( "Shiny Peach" , "It tastes really sweet!" , image = "lezInventory/example_items/images/19_Peach.png" )
default peach2 = Peach( "Shimmering Peach" , "It smells of an update." , image = "lezInventory/example_items/images/19_Peach.png" )
default peach3 = Peach( "Glistening Peach" , "Both tastes sweet {i}and{/i}\nsmells of an update." , image = "lezInventory/example_items/images/19_Peach.png" )
```
# Fig
![09_Fig](https://user-images.githubusercontent.com/56970124/190861697-5025a83a-99b7-4295-b54b-ae773fb7efd4.png)

Fig is an equippable item.

Upon being equipped, it shows a custom screen with a message, indicating this item will be removed from the inventory upon being unequipped.

```py
init -800 python:

    # Class of the Dragon Fruit.
    class Fig(Item):

        # This marks the Item as equippable.
        equippable = True

        # Remove the Item once it's unequipped.
        consumed_on_unequip = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is equipped.
        def equipped(self, Inventory):

            # Show the screen.
            return renpy.show_screen("fig_screen")

        # What happens when the Item is unequipped.
        def unequipped(self, Inventory):

            # Message showing the removal.
            return renpy.notify("The flavour fades away...")

# Fig defined.
default fig = Fig( "Fig" , "Strange fruit from the Mediterranean." , "lezInventory/example_items/images/09_Fig.png" )


# Overlay to darken Inventory behind the frame.
define fig_overlay = At( Solid("000"), Transform(alpha = 0.5) )

# Screen shown when the Item is equipped.
screen fig_screen():

    # Add the overlay.
    add fig_overlay

    # Frame in the middle of the screen
    frame:

        align (0.5, 0.5)
        padding (10, 10)

        vbox:
            text "As you bite into the fig, a sweet taste fills your mouth."
            text "Savour the flavour while you can!"
    
    # So that player cannot interact with stuff below this screen.
    modal True

    # Hide the screen on click.
    key "dismiss" action Hide("fig_screen")
```