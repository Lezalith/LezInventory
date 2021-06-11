init -1 python:
    def copyText(text, notice):

        import pygame.scrap
       
        pygame.scrap.put(pygame.scrap.SCRAP_TEXT, text.encode("utf-8"))

        renpy.notify(notice)

# TODO: Lemon equipped when the only one on page
# Entering from screen doesnt refill items

screen main_menu():

    tag main

    add gui.main_menu_background

    frame:
        align (0.5, 0.5)
        xysize (1600, 800)
        ypadding 75

        vbox:
            xalign 0.5
            spacing 50

            vbox:
                xalign 0.5
                spacing 4

                text "LezInventory" xalign 0.5 size 72
                add Solid("000") size (700, 3) xalign 0.5
                text "Inventory Framework by Lezalith" xalign 0.5 

            vbox:
                
                spacing 40

                vbox:
                    xalign 0.5
                    spacing 2
                    text "Welcome to LezInventory!"
                    text "An Inventory framework that I hope will be of use to many creators."

                hbox:
                    xalign 0.5
                    spacing 80

                    textbutton "What is LezInventory?" yalign 0.5 action Show("desc")

                    textbutton "How do I set it up?" yalign 0.5 action Show("info")

                text "You can try LezInventory by clicking one of the buttons below." xalign 0.5

                hbox:
                    spacing 250
                    xalign 0.5

                    textbutton "Enter from a screen.":
                        action Show("fromScreen")


                    textbutton "Enter from a label.":
                        action Start("fromLabel")

                vbox:
                    xalign 0.5
                    yalign 1.0
                    text "And here, you can click to copy my Discord, let me know how you've liked my work."
                    textbutton "Lezalith (LezCave.com)#2853" xalign 0.5 action Function(copyText, text = "Lezalith (LezCave.com)#2853", notice = "Lez's Discord copied to clipboard!"):
                        text_size 21


screen info():

    modal True

    add gui.main_menu_background

    frame:
        align (0.5, 0.5)
        xysize (1800, 800)
        ypadding 120

        vbox:
            xalign 0.5
            spacing 40

            text "Sorry, this is just a preview! The code will be out soon!"

            # vbox:
            #     spacing 5
            #     text "If you go through the files of this project, you will find a .zip file named \"LezInventoryCode.zip\"."
            #     text "Inside this zip are all the files you need to set up the Inventory."

            # vbox:
            #     spacing 5
            #     text "It contains the Inventory code and screen, as well as the examples on how to show it."
            #     text "It also contains the Items code, but doesn't include the fruit examples like this project does."

            # vbox:
            #     spacing 5
            #     text "It is basically the clean canvas for you to grab if you want to use this inventory yourselves."
            #     text "If you do, be sure to check out the \"inv_intro.rpy\" file first, that's where the journey begins!"
            #     text "All of the code is commented as much as it can be, feel free to customize anything you want."

            # text "Good luck!! :)"

        textbutton "Back to the menu!" align (0.5, 1.0) yoffset -10 action Hide("info")

style descStyle_text:
    size 28

screen desc():

    modal True

    add gui.main_menu_background

    frame:
        align (0.5, 0.5)
        xysize (1850, 800)
        ypadding 120

        vbox:

            style_prefix "descStyle"

            xalign 0.5
            spacing 50

            vbox:
                spacing 3
                text "LezInventory is a framework that I've put together in about three weeks."
                text "In case you don't know me, my name is Lezalith, Lez for short, and I've been coding in Ren'Py for about 7 years."

            vbox:
                spacing 3
                text "Framework is a code that you can take and use yourselves. In my case it means a working Inventory."
                text "LezInventory is easy to use, customize and modify. It is flexible and does all the basics."
                text "It supports regular items, as well as equippable and usable ones. For the equippables, it has one equip slot."
                text "What's more, items are very easy to create."

            vbox:
                spacing 3
                text "There are defined styles for every piece of graphics in the Inventory."
                text "Styles are used to customize default Ren'Py projects, too, making things easier for those who use them."

            vbox:
                spacing 3
                text "The point of this Inventory is to provide game creators with a modern Inventory."
                text "An Inventory that let's them move forward with their projects, even better, help them make the whole game better."
                text "It is up to you to decide whether I've succeeded."


        textbutton "Back to the menu!" align (0.5, 1.0) yoffset 70 action Hide("desc")


screen fromScreen():

    tag main
    modal True

    frame:
        align (0.5, 0.5)
        padding (100, 100)

        vbox:
            spacing 2

            text "Sorry, didn't want to drop you into the Inventory straight away."
            text "Click the button below to enter it." xalign 0.5
            text "I sincerely hope you'll enjoy!" xalign 0.5
            text ""
            textbutton "Woosh!" action Show("inventoryScreen", howToLeave = "both") xalign 0.5

label fromLabel:

    "Lezalith" "This is a line of dialogue to show you we are inside a label.\nFeel free to play around with the Inventory, you'll end up back in this label when you click Return!"

    call screen inventoryScreen

    "Lezalith" "Welcome back to the label! I hope you've enjoyed :)"

    return
