Styles allow for easy Inventory Screen customization. They're all located on the top of the **lezInv_screen.rpy** file.
This page shows all of them, as well their default properties. Some of the properties refer to variables from **lezInv_settings.rpy**.
# Main Frame Styles
Style of the main inventory **frame**.
```py
style inventory_main_frame:
    xysize lezInv_settings.main_frame_size
    align (0.5, 0.4)
```
# Slots Styles
Style of the **grid** holding all the inventory slots.
```py
style inventory_slots_grid:
    xpos 100
    yalign 0.5
    yoffset -35
    xspacing 50
    yspacing 15
```
Style of the **frame** representing an inventory slot, WHEN IT IS OCCUPIED BY AN ITEM.
```py
style inventory_slot:
    idle_background lezInv_settings.slot_full_idle
    hover_background lezInv_settings.slot_full_hover
    selected_idle_background lezInv_settings.slot_full_selected
    selected_hover_background lezInv_settings.slot_full_selected_hover
    xysize lezInv_settings.slot_size
```
Style of the **frame** representing an inventory slot, WHEN EMPTY.
```py
style inventory_slot_empty:
    idle_background lezInv_settings.slot_empty_idle
    hover_background lezInv_settings.slot_empty_hover
    xysize lezInv_settings.slot_size
```
Style of the **text** giving count of stackable Items.
```py
style inventory_slot_text:
    align (1.0, 1.0)
    offset (-10, -5)
    bold True
    size 48
    color "000"
    outlines [ (absolute(4), "ffcc11", absolute(0), absolute(0)) ]
```
Style of the **hbox** holding indicators for usable/equippable items.
```py
style inventory_slot_indicator_hbox:
    xalign 1.0
    offset (-10, 10)
```
# Side Menu Styles
Style of the **frame** holding everything in the side menu.
```py
style inventory_side_menu_frame:
    # background Solid("000") # Great for testing, shows the Frame.
    background None
    xysize(400, 660)
    align (1.0, 0.5)
    xoffset -50
```
Style of the **vbox** holding the "Equipped Item" label and the inventory equip slot.
```py
style inventory_side_menu_vbox_equipped:
    xalign 0.5
    spacing 5
    ypos 30
```
Style of the **vbox** holding the "Equipped Item" label and the inventory equip slot.
```py
style inventory_side_menu_vbox_equipped:
    xalign 0.5
    spacing 5
    ypos 30
```
Style of the "Equipped Item" **text**.
Commented out by default, as the default screen doesn't use it.
```py
style inventory_side_menu_vbox_equipped_text:
    example 123
```
Style of the **frame** representing the inventory equip slot.
```py
style inventory_side_menu_vbox_equipped_slot:
    background lezInv_settings.slot_equipped_image
    xysize (200, 200)
    xalign 0.5
```
Style of the **vbox** holding the Item's name and description.
```py
style inventory_side_menu_vbox_info:
    xsize 400 # Same size as the inventory_side_menu_frame.
    xalign 0.5
    spacing 5
    ypos 330
```
Style of the Item's name **text**.
```py
style inventory_side_menu_vbox_info_name:
    xalign 0.5
    underline True
```
Style of the Item's description **text**.
```py
style inventory_side_menu_vbox_info_description:    
    xalign 0.5
    size 26
```
# Side Menu Buttons Styles
Style of the **vbox** holding the **hbox** Equip/Unequip **buttons**, use **button** and throw away **button**.
```py
style inventory_side_menu_vbox_interaction:   
    xsize 400 # Same size as the inventory_side_menu_frame.
    xalign 0.5
    ypos 460
    spacing 8
```
Style of the **hbox** holding the Equip and Unequip **buttons**.
```py
style inventory_side_menu_vbox_interaction:   
    xsize 400 # Same size as the inventory_side_menu_frame.
    xalign 0.5
    ypos 460
    spacing 8
```
Style of the Unequip **textbutton**.
```py
style inventory_side_menu_vbox_interaction_unequip_textbutton:
    xsize 140
```
Style of the **text** of the Unequip **textbutton**.
```py
style inventory_side_menu_vbox_interaction_unequip_textbutton_text:
    xalign 0.5
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
Style of the Equip **textbutton**.
```py
style inventory_side_menu_vbox_interaction_equip_textbutton:
    xsize 140
```
Style of the **text** of the Equip **textbutton**.
```py
style inventory_side_menu_vbox_interaction_equip_textbutton_text:
    xalign 0.5
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
Style of the Use **textbutton**.
Commented out by default, as the default screen doesn't use it.
```py
style inventory_side_menu_vbox_interaction_use_textbutton:
    example 123
```
Style of the **text** of the Use **textbutton**.
```py
style inventory_side_menu_vbox_interaction_use_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
Style of the Throw Away **textbutton**.
```py
style inventory_side_menu_vbox_interaction_throwaway_textbutton:
    xalign 0.5
```
Style of the **text** of the Throw Away **textbutton**.
```py
style inventory_side_menu_vbox_interaction_throwaway_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
Style of the Return **textbutton**.
```py
style inventory_side_menu_return_textbutton:
    align (0.5, 1.0)
    yoffset -10
```
Style of the **text** of the Return **textbutton**.
```py
style inventory_side_menu_return_textbutton_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
# Page Controls Styles
Style of the **hbox** holding the page controls.
```py
style inventory_pages_hbox:
    xanchor 0.5
    xpos 415
    ypos 630
    spacing 180
```
Style of the left arrow **textbutton**.
The default inventory screen needs no properties for this, but needs it defined. 
```py
style inventory_pages_hbox_left:
    background None    
```
Style of the **text** of the left arrow **textbutton**.
```py
style inventory_pages_hbox_left_text:
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
    size 42
```
Style of the right arrow **textbutton**.
The default inventory screen needs no properties for this, but needs it defined. 
```py
style inventory_pages_hbox_right:
    background None
```
Style of the **text** of the right arrow **textbutton**.
```py
style inventory_pages_hbox_right_text:
    size 42
    insensitive_color "aaaaaa7f"
    idle_color "aaa"
    hover_color "c60"
```
Style of the **text** representing the page count.
```py
style inventory_pages_hbox_text:
    ypos 7
```
