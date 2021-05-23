python early:
    renpy.register_sl_statement("marker", children="many").add_property("color").add_property("xysize")

screen marker(color = "fff", xysize = (155, 155) ):

    fixed:
        xysize xysize
        align (0.5, 0.5)

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