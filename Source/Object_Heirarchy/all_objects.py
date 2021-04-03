# from Source.Object_Heirarchy import object_3d
# import object_3d
from Source.Object_Heirarchy.object_3d import Object3D


class Sphere(Object3D):
    
    def __init__(self):
        self.object_type = 'sphere'
        self.properties = ['radius']
        self.properties = {elem : None for elem in self.properties} # initialize the properties to None

    def to_string_fusion(self):
        pass