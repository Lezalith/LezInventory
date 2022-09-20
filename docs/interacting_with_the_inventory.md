This page shows all the ways you can interact with the Inventory, from adding/removing Items to checking what is currently equipped. Don't forget that this is all Python code, requiring to be in a **python** or **init python** block, or preceeded by a **$** sign.
The default **Inventory** object is stored in the **inventory** variable, so all the methods are bound to it. This basically means that everything has the form of **inventory.<some_name>**.
# Basic Inventory Methods
Adds a defined Item object to the Inventory.
If keyword argument **count** is given, multiple copies of the Item can be added to the Inventory. In this case, the Item has to be **stackable**.
```py
inventory.add(item, count = 1)
```
Removes a defined Item object from the Inventory. **item** can be omitted, in which case the currently **selected** Item is removed, or nothing is if nothing is selected.
If keyword argument **count** is given, multiple copies of the Item can be removed from the Inventory. In this case, the Item has to be **stackable**. Removing more Items that are present simply removes the Item from the inventory. 
```py
inventory.remove(item = None, count = 1)
```
Discards an Item. Difference between **remove** and **discard** is that **discard** calls the item's **discarded** before removing the item, allowing custom functionality when the item is removed. **item** can be omitted, in which case the currently **selected** Item is discarded, or nothing is if nothing is selected.
Item being discarded HAS TO BE IN THE INVENTORY.

Generally, **discard** should be used by the player and **remove** should be used by you.
```py
inventory.discard(item = None, count = 1)
```
Resets the Inventory to the empty state. Takes no arguments.
```py
inventory.clear()
```
Selects an Item, if it's present in the inventory.
This will be mostly used by the Inventory Screen, as you can **use**/**equip** Items present in the inventory directly.
```py
inventory.select(item)
```
Unselect the currently selected Item, if there is one. Takes no arguments.
```py
inventory.unselect()
```
Uses an Item, calling it's **used** method. **item** can be omitted, in which case the currently **selected** Item is used, or nothing is if nothing is selected.
Item given DOES NOT HAVE TO BE IN THE INVENTORY, but if it is, it refers to the **consumed_on_use** variable to see whether it should be removed.
```py
inventory.use(item = None)
```
Equips an Item into the inventory equip slot, calling it's **equipped** method. **item** can be omitted, in which case the currently **selected** Item is used, or nothing is if nothing is selected.
Item given DOES NOT HAVE TO BE IN THE INVENTORY, but if it's not, it's added upon the equip.
```py
inventory.equip(item = None)
```
Unequips the currently equipped Item, calling it's **unequipped** method. Does nothing if nothing is equipped. Takes no arguments.
```py
inventory.unequip()
```
# Inventory Properties
Returns an **OrderedDict** in which the present Items are stored.
In the dictionary, **keys** are the Item objects, and **values** are how many of them are in the inventory.
```py
inventory.items
```
Returns the Item currently selected, or **None** if nothing is selected.
```py
inventory.selected
```
Returns the Item currently equipped, or **None** if nothing is equipped.
```py
inventory.equipped
```
# Advanced Inventory Methods
Checks whether at least one of given Item is present in the inventory. Returns **True** or **False**.
```py
inventory.is_in_inventory(item)
```
Checks whether the given Item is the one currently selected. Returns **True** or **False**.
```py
inventory.is_selected(item)
```
Checks whether the given Item is the one currently equipped. Returns **True** or **False**.
```py
inventory.is_equipped(item)
```

# Additional Checks, Page Control and Calculations
There are a couple more methods, but they're very specific, so I'm not including them here.
They can all be found in the **lezInv.inventory.rpy** file.