init -890 python:

    ###########################################
    ###########################################
    #
    # Item Class
    #
    ###########################################
    ###########################################

    class Item():

        "Base class for all the items."

        # Initialization. Arguments:
        #
        # name - String, name of the item.
        #
        # desc - Description of the item.
        #
        # image - Image of the Item. Can be a file,
        # a displayable, or the default None, which then
        # creates a Text Displayable from the name argument.

        def __init__(self, name, desc, image = None):

            print( str( locals() ) )

            # Name of the Item.
            self.name = name

            # Description of the Item.
            self.description = desc

            # Image of the Item.
            if image:
                self.image = image
            else:
                # Use Text Displayable if Image not given.
                self.image = Text(name)

            # My test version of .image.
            # Overwrites the stuff above.
            # # TODO: Remove this.
            # self.image = Transform( image, zoom = 2.0) 

            # This is the base class for Items, 
            # so there is no functionality for these.
            self.usable = False
            self.equippable = False

        ############################
        ## Checks
        ############################

        def isEquippable(self):

            return self.equippable

        def isUsable(self):

            return self.usable

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is used.
        def used(self):
            return None 

        # What happens when the Item is Equipped.
        def equipped(self):
            return None

    ###########################################
    ###########################################
    #
    # UsableItem Class
    #
    ###########################################
    ###########################################

    class UsableItem(Item):

        "Class for usable Items."

        def __init__(self, name, desc, image):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less
            # arguments that should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(UsableItem, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

            # That's the point of this class.
            self.usable = True

        ############################
        ## Checks
        ############################

        # Whether the Item is usable.
        def isUsable(self):

            return self.usable 

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is used.
        def used(self):
            return renpy.notify("An Item {} has been used!".format(self.name)) 

    ###########################################
    ###########################################
    #
    # EquippableItem Class
    #
    ###########################################
    ###########################################

    class EquippableItem(Item):

        "Class for usable Items."

        def __init__(self, name, desc, image):

            # Gets all the arguments.
            args = locals()

            # Manual check whether there are more/less
            # arguments that should be.
            numOfArguments = 4

            if len( args.keys() ) > numOfArguments:
                raise TypeError( "__init__() takes {} arguments ({} given)".format( numOfArguments , len( args.keys() ) ) )

            ##########################

            # Calls the parent class, Item, with everything that it needs.
            super(EquippableItem, self).__init__( name = args.get("name"), desc = args.get("desc"), image = args.get("image") )

            # That's the point of this class.
            self.equippable = True

        ############################
        ## Checks
        ############################

        # Whether the Item is equippable.
        def isEquippable(self):

            return self.equippable 

        ############################
        ## To Be Overwritten
        ## Should be overwritten by child class
        ############################
        
        # What happens when the Item is equipped.
        def equipped(self):
            return renpy.notify("An Item {} has been equipped!".format(self.name)) 