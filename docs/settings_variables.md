Here is the overview of all preference variables, and their default values.
# Inventory Screen Variables
This represents the grid of inventory slots. 
Both require **ints** (whole numbers).
```py
define lezInv_settings.width = 3
define lezInv_settings.height = 3
```
Width and height (in pixels) of the main Inventory Screen frame. 
**Tuple** of two **ints**.
```py
define lezInv_settings.main_frame_size = (1280, 720)
```
Background of the main frame. 
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.main_frame_image = "gui/frame.png"
```
Width and height (in pixels) of the Inventory Slots.
**Tuple** of two **ints**.
```py
define lezInv_settings.slot_size = (180, 180)
```
Multiple variables giving the background image of inventory slots in different states WHEN OCCUPIED BY AN ITEM.
These follow the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.slot_full_idle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_hover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_selected = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)
define lezInv_settings.slot_full_selected_hover = Frame("lezInventory/gui/slot_selected.png", 6, 6, 6, 6)
```
Multiple variables giving the background image of inventory slots in different states WHEN EMPTY.
These follow the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.slot_empty_idle = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
define lezInv_settings.slot_empty_hover = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
```
Background of the equip inventory slot.
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.slot_equipped_image = Frame("lezInventory/gui/slot.png", 6, 6, 6, 6)
```
Image on top of the slot with the currently equipped Item.
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.equipped_highlight_image = "lezInventory/gui/equipped_highlight_image.png"
```
Image on top of the equipped inventory slot.
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.equipped_highlight_slot_image = "lezInventory/gui/equipped_highlight_imageSlot.png"
```
If **True**, an image is added into the inventory slot whenever it's occupied by an item that's equippable.
```py
define lezInv_settings.show_equippable_indicator = True
```
Image potentially shown in inventory slot of items if **show_equippable_indicator** is **True**.
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.equippable_indicator = Text("E", bold = True, size = 28, color = "000", outlines = [ (absolute(1), "ffcc11", absolute(0), absolute(0)) ])
```
If **True**, an image is added into the inventory slot whenever it's occupied by an item that's usable.
```py
define lezInv_settings.show_usable_indicator = True
```
Image potentially shown in inventory slot of items if **show_usable_indicator** is **True**.
This follows the usual Ren'py image rules - **Displayable** or a **string**.
```py
define lezInv_settings.usable_indicator = Text("U", bold = True, size = 28, color = "000", outlines = [ (absolute(1), "ffcc11", absolute(0), absolute(0)) ])
```
Variables controlling what labels and buttons are shown on the Inventory Screen.
All **True** by default, they can be set to **False** to quickly hide different elements.
```py
define lezInv_settings.show_equipped_label = True
define lezInv_settings.show_equipped_slot = True
define lezInv_settings.show_description = True
define lezInv_settings.show_equip_button = True
define lezInv_settings.show_use_button = True
define lezInv_settings.show_throw_away_button = True
```

# Item Variables
Whether usable Items are removed from the inventory upon being used. This can always be overwritten in individual Items.
Can be **True** or **False**.
```py
define lezInv_settings.consumed_on_use = True
```
Whether equippable Items are removed from the inventory upon being unequipped. This can always be overwritten in individual Items.
Can be **True** or **False**.
```py
define lezInv_settings.consumed_on_unequip = False
```
Whether Items are stackable by default.
Can be **True** or **False**.
```py
define lezInv_settings.stackable = False
```
What is the default stack_size of Items that have **stackable** set to **True**.
Requires an **int** (whole number).
```py
define lezInv_settings.stack_size = 1
```