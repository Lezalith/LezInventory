# Cherries is a Usable item.
# When used, it adds a CDD on screen.

init -800 python:

    # Used for generating random tag name.
    from random import randrange

    # Class of the Durian.
    class Cherries(Item):

        # This marks the Item as usable.
        usable = True

        ## __init__ got ommited, as this Item doesn't take/need any extra arguments.

        # What happens when the Item is used.
        def used(self, Inventory):

            # A random string for the tag is generated, so that the cherry seed
            # can be shown on screen multiple times, rather than one being re-shown.
            #
            # The random string is a number of 5-8 digits.
            tag = str(randrange(10000, 99999999))

            # Show a new CherrySeed CDD on screen.
            return renpy.show( tag, layer = "screens", zorder = 20, what = CherrySeed() )

# Durian defined.
default cherries = Cherries( "Cherries" , "Spit the seeds at your foes!" , "lezInventory/example_items/images/01_Cherry_Red.png", stackable = True, stack_size = 9999 )

init -870 python:

    # Used for determining the random starting position of the seed.
    from random import randrange

    # Used to calculate an arc movement.
    from math import sin

    # Sets the starting ypos to random within the given range.
    def cherry_seed_starting_pos(trans, st, at):

        # Choose a random y, within the screen boundaries.
        # -128 compensates for image size.
        # +250 compensates for the arc image will be moving on (value is arc_height from cherry_seed_arc + 50, to allow partial overlap)
        trans.ypos = randrange(0, config.screen_height - 128 + 250) 
        
        # Finish this function.
        return None

    def cherry_seed_arc(trans, st, at):

        # Aprox. time of the seed crossing the right side of the screen.
        duration = 2.0

        # Both determine the arc's shape.
        arc_height = 200
        arc_shape = 0.7

        # Finish this function so that the transform doesn't keep on updating endlessly after getting offscreen.
        if st >= duration:
            return None

        # Update yoffset.
        # This is calculated from a formula which has the displayables's current display time inside (st).
        trans.yoffset = int(-arc_height * sin(st / arc_shape) )
        
        # Call this function again - continue the transform.
        return 0

# Transform that starts the image at random ypos on the left,
# before moving it to the right with a vertical arc.
init -860:
    transform cherry_seed_transform():

        # First set random ypos.
        function cherry_seed_starting_pos

        # At the same time, calculate yoffset for the arc movement.
        parallel:
            function cherry_seed_arc

        # At the same time, move the seed to the right side of the screen.
        parallel:
            linear 1.5 xpos 2000

# CherrySeed CDD.
init -850 python:

    class CherrySeed(renpy.Displayable):

        # What happens upon the definition.
        def __init__(self, **kwargs):

            # Pass additional properties on to the renpy.Displayable constructor.
            super(CherrySeed, self).__init__(**kwargs)

            # The child.
            i = renpy.displayable( "lezInventory/example_items/images/0X_CherrySeed.png" )

            # That child will be moving at this transform.
            self.child = At(i, cherry_seed_transform)

        # Runs when the screen is rendered.
        def render(self, width, height, st, at):

            # Create a render, basically a canvas onto which we can place things.
            render = renpy.Render(width, height)

            # Place the seed image.
            render.place(self.child)

            # Return the render to show it.
            return render