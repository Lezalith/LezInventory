python early:

    # Registers the marker screen as a custom screen language statement.
    renpy.register_sl_statement("marker", children="many").add_property("color").add_property("xysize").add_property("thickness")

# Screen that will function as the statement.
# 
# Creates a square border of xysize = (width, heigth).
# It has the color of color and thickness of thickness.
screen marker(color = "fff", xysize = (155, 155) , thickness = 6):

    # Fixed area.
    # Frames have default BG and Padding.
    fixed:
        xysize xysize
        align (0.5, 0.5)

        # Adds 4 rectangles that look line lines.
        add Solid(color): # Top left going right
            size (xysize[1], thickness)
            align(0.0, 0.0)
        add Solid(color): # Top left going down
            size (thickness, xysize[1])
            align(0.0, 0.0)
        add Solid(color): # Bottom right going up
            size (thickness, xysize[1])
            align(1.0, 1.0)
        add Solid(color): # Bottom right going left
            size (xysize[0], thickness)
            align(1.0, 1.0)  