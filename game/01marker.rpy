python early:
    renpy.register_sl_statement("marker", children=0).add_positional("color")

screen marker(color):

    fixed:
        xysize (155, 155)
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