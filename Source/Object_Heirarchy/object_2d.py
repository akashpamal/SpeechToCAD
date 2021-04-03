class Object2D:

    def __init__(self) -> None:
        self.object_2d_name = None
        self.surface = None
        self.properties = {}

    def draw_on_sketch(self, sketch): # surface is a plane or other surface where we can create a sketch
        print('The draw_on_sketch needs to be implemented in' + self.object_2d_name)
    
    def get_needed_properties(self):
        needed_properties = [elem for elem in self.properties if self.properties[elem] is None]
        if self.object_2d_name is None:
            raise Exception('This Object2D subclass needs a name')
        if self.surface is None:
            needed_properties.append('surface')
        return needed_properties # list of strings
    
    def to_string_display(self):
        """
        Returns a string that can be used to display the object in a human-readable format.
        """
        return_string = self.object_type + ', '.join([elem for elem in self.properties.items()])
        return return_string

    def to_string_fusion(self):
        """
        Returns a string that can be used to create the object using the Fusion API. Implemented in each subclass.
        """
        return 'The to_string_fusion method needs to be implemented in class:' + self.object_type
    