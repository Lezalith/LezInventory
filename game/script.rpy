init -1 python:
    def copyMyDisc():

        import pygame.scrap
       
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, "Lezalith (LezCave.com)#2853".encode("utf-8"))

        renpy.notify("Lez's Discord coppied to clipboard!")

screen main_menu():

    add gui.main_menu_background

    frame:
        align (0.5, 0.5)
        xysize (1600, 800)
        ypadding 75

        vbox:
            xalign 0.5
            spacing 125

            text "Inventory Framework by Lezalith" xalign 0.5 underline True

            vbox:
                spacing 2
                text "Welcome to my Inventory!"
                text "I hope this framework will be of use to many creators."
                text "You can always let me know where you've used it by writing me on Discord, I will always be happy to hear from you :)"
                textbutton "Lezalith (LezCave.com)#2853" xalign 0.5 action Function(copyMyDisc)
                text ""
                text "Now, would you like to enter the Inventory from a screen, or from a label?"

            hbox:
                spacing 250
                xalign 0.5

                textbutton "Enter from a screen.":
                    action Start("fromScreen")


                textbutton "Enter from a label.":
                    action Start("fromLabel")


screen startScreen():

    frame:
        align (0.5, 0.5)
        padding (100, 100)

        vbox:

            text "Click the following button to enter the Inventory."
            text "I sincerely hope you'll enjoy!" xalign 0.5
            text ""
            textbutton "Woosh!" action Show("inventoryScreen") xalign 0.5

label fromScreen:

    # From example_items.rpy, adds pre-defined Items.
    $ addExampleItems()

    call screen startScreen

    return


label fromLabel:

    # From example_items.rpy, adds pre-defined Items.
    $ addExampleItems()

    "Lezalith" "This is a line of dialogue to show you we are inside a label.\nFeel free to play around with the Inventory, you'll end up back in this label when you click Return!"

    call screen inventoryScreen

    "Lezalith" "Welcome back to the label! I hope you've enjoyed :)"

    return
