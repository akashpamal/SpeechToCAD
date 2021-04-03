class Object3D:
    """
    Abstract class that represents all 3d objects. These can be simple objects like Cubes and Spheres, or can be more complex objects that use a sketch and a length to extrude.
    """

    def __init__(self):
        self.object_type = None
        self.properties = ['sketch', 'extrude_level']
        self.properties = {elem : None for elem in self.properties}

    def get_needed_properties(self):
        needed_properties = [elem for elem in self.properties if self.properties[elem] is None]
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
    