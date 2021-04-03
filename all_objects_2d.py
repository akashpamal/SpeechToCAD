from Source.Object_Heirarchy.object_2d import Object2D


class Rectangle(Object2D):
    def __init__(self, width=None, height=None):
        super().__init__()
        self.object_2d_name = 'Rectangle'
        self.properties = {'width' : width, 'height' : height}
    
    def to_string_fusion(self):
        return_string = f"rec1 = lines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create({self.width}, {self.height}, 0))"
        return return_string
