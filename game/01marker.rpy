python early:

    # Registers the marker screen as a custom screen language statement.
    renpy.register_sl_statement("marker", children="many").add_property("color").add_property("xysize")

# Screen that will function as the statement.
# 
# Creates a box of xysize = (width, heigth), and places
# a 15x15 square into each corner.
# Squares have the color of color.
screen marker(color = "fff", xysize = (155, 155) ):

    # Fixed area.
    # Frames have default BG and Padding.
    fixed:
        xysize xysize
        align (0.5, 0.5)

        # All 4 squares added, each in different corner.
        add Solid(color):
            size (15, 15)
            align(0.0, 0.0)
        add Solid(color):
            size (15, 15)
            align(1.0, 0.0)
        add Solid(color):
            size (15, 15)
            align(1.0, 1.0)
        add Solid(color):
            size (15, 15)
            align(0.0, 1.0)  