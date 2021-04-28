from object_2d import Object2D

class Rectangle(Object2D):
    def __init__(self, width=None, height=None):
        super().__init__()
        self.object_type = 'Rectangle'
        self.properties.update({'width' : width, 'height' : height})
    
    def to_string_fusion(self):
        return_string = super().to_string_fusion()
        return_string += f"        rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create({self.get_prop('width')}, {self.get_prop('height')}, 0))\n"
        return return_string
    
class Square(Object2D):
    def __init__(self, side_length=None):
        super().__init__()
        self.object_type = 'Square'
        self.properties.update({'side_length' : side_length})

    def to_string_fusion(self):
        return_string = super().to_string_fusion()
        return_string += f"        rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create({self.get_prop('side_length')}, {self.get_prop('side_length')}, 0))\n"
        return return_string
    
class Circle(Object2D):
    def __init__(self, radius=None):
        super().__init__()
        self.object_type = 'Circle'
        self.properties.update({'radius' : radius})
    
    def to_string_fusion(self):
        return_string = super().to_string_fusion()
        return_string += f"        circles = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), {self.get_prop('radius')})\n"
        return return_string