class Object2D:

    def __init__(self) -> None:
        self.object_2d_name = None
        self.sketch_plane = None
        self.properties = {'sketch_plane' : 'sketch'}
    
    def get_needed_properties(self):
        needed_properties = [elem for elem in self.properties if self.properties[elem] is None]
        if self.object_2d_name is None:
            raise Exception('This Object2D subclass needs a name')
        if self.sketch_plane is None:
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
    
    def set_prop(self, property_name, value):
        if property_name not in self.properties:
            raise Exception(f'{property_name} is not a property of {self.object_2d_name}')
        self.properties[property_name] = value
    
    def get_prop(self, property_name):
        if property_name not in self.properties:
            raise Exception(f'{property_name} is not a property of {self.object_2d_name}')
        return self.properties[property_name]