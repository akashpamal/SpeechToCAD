class ExtrudedObject3D:
    """
    Abstract class that represents all 3d objects. These can be simple objects like Cubes and Spheres, or can be more complex objects that use a sketch and a length to extrude.
    """

    def __init__(self, sketch_profile='sketch.profiles[-1]', extrude_distance=None):
        self.object_type = 'Extruded Sketch'
        self.properties = {'sketch_profile' : sketch_profile, 'extrude_distance' : extrude_distance}

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
        return_str = f"        extrudeDistance = adsk.core.ValueInput.createByReal({self.properties['extrude_distance']})\n        extrude = rootComp.features.extrudeFeatures.addSimple({self.sketch_profile}, extrudeDistance, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)"
        return return_str
    
    def set_prop(self, property_name, value):
        self.properties[property_name] = value
    
class PrimitiveObject3D:
    """
    Abstract class that represents all 3d objects. These can be simple objects like Cubes and Spheres, or can be more complex objects that use a sketch and a length to extrude.
    """

    def __init__(self, sketch_profile='sketch.profiles[-1]', extrude_distance=None):
        self.object_type = 'Extruded Sketch'
        self.properties = {}

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
        return_str = f"This method needs to be implemented in {self.object_type}"
        return return_str
    
    def set_prop(self, property_name, value):
        if property_name not in self.properties:
            raise Exception(f'{property_name} is not a property of {self.object_2d_name}')
        self.properties[property_name] = value
    
    def get_prop(self, property_name):
        if property_name not in self.properties:
            raise Exception(f'{property_name} is not a property of {self.object_2d_name}')
        return self.properties[property_name]