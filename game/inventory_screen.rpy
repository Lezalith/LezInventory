
style inventory_frame:

    xysize (1280, 720)
    align (0.5, 0.5)

style inventory_grid:

    xpos 100
    yalign 0.5
    yoffset -35
    xspacing 50
    yspacing 15

style inventory_button:

    background Frame("gui/frame.png", 6, 6, 6, 6)
    xysize (180, 180)

style inventory_pages_text:

    size 42

style inventory_pages_button_text:

    size 42

screen inventoryScreen():

    modal True

    add Solid("c0c0c0")

    frame:

        style_prefix "inventory"

        grid Inventory.grid["width"] Inventory.grid["heigth"]:

            for index, item in enumerate( Inventory.getPageItems() ):

                button:


                    # If this slot is equipped
                    if Inventory.isEquipped(index):

                        # Custom screen statement
                        marker:
                            color "fc1"
                            xysize (165, 165)

                    # If this slot is selected
                    if Inventory.isSelected(index):

                        # Custom screen statement
                        marker:
                            color "f00"
                            xysize (150, 150)

                    action Function( Inventory.selectToggle , index )
                    
                    add item.image:
                        align (0.5, 0.5)

            for x in range( Inventory.getEmptyCells() ):

                button:

                    action Function( Inventory.unselect )

        frame:

            style_prefix None

            background None
            xysize(400, 660)
            align (1.0, 0.5)
            xoffset -30

            vbox:

                align (0.5, 0.06)
                spacing 5

                text "Equipped Item:"

                frame:

                    background Frame("gui/frame.png", 6, 6, 6, 6)
                    xysize (200, 200)
                    xalign 0.5

                    # 
                    if Inventory.getEquippedItem():
                        add Inventory.getEquippedItem().image:
                            align (0.5, 0.5)

                    # If something is equipped
                    if Inventory.getEquippedItem():
                        fixed:
                            xysize (175, 175)
                            align (0.5, 0.5)

                            add Solid("fc1"):
                                size (15, 15)
                                align(0.0, 0.0)
                            add Solid("fc1"):
                                size (15, 15)
                                align(1.0, 0.0)
                            add Solid("fc1"):
                                size (15, 15)
                                align(1.0, 1.0)
                            add Solid("fc1"):
                                size (15, 15)
                                align(0.0, 1.0)  

            vbox:

                align (0.5, 0.56)
                spacing 5
                xsize 500

                text ( Inventory.getSelectedItem().name if Inventory.getSelectedItem() else "Nothing selected." ):
                    xalign 0.5
                    underline True
                text ( Inventory.getSelectedItem().description if Inventory.getSelectedItem() else "Nothing selected." ):
                    xalign 0.5
                    size 24

            vbox:

                align (0.5, 0.83)
                xsize 400
                spacing 8

                hbox:
                    xalign 0.5
                    spacing 50

                    # Equipped Selected
                    if Inventory.canUnequip():

                        textbutton "Unequip":

                            action Function(Inventory.unequip)

                    else:

                        # No item selected
                        textbutton "Equip": 

                            sensitive Inventory.canEquip()
                            action Function(Inventory.equip)

                    textbutton "Use": 
                        
                        sensitive Inventory.canUse()
                        action Function(Inventory.use)


                textbutton "Throw Away":
                    sensitive Inventory.getSelectedItem()
                    xalign 0.5
                    action Function(Inventory.remove)

            textbutton "Return":

                align (0.5, 1.0)
                action Return()

        hbox:

            style_prefix "inventory_pages"

            xanchor 0.5
            xpos 415
            yalign 0.965

            spacing 180

            textbutton "<":
                action Function( Inventory.changePage, "down" )

            text "{} / {}".format( *Inventory.getPagesRepr() ):
                ypos 7

            textbutton ">":
                action Function( Inventory.changePage, "up" )
