from object_2d import Object2D

class Rectangle(Object2D):
    def __init__(self, width=None, height=None):
        super().__init__()
        self.object_2d_name = 'Rectangle'
        self.properties = {'width' : width, 'height' : height}
    
    def to_string_fusion(self):
        return_string = f"rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create({self.properties['width']}, {self.properties['height']}, 0))"
        return return_string

class Circle(Object2D):
    def __init__(self, width=None, height=None):
        super().__init__()
        self.object_2d_name = 'Rectangle'
        self.properties = {'width' : width, 'height' : height}
    
    def to_string_fusion(self, sketch_surface='sketch'): # remove this default eventually
        return_string = f"rec1 = {sketch_surface}.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create({self.properties['width']}, {self.properties['height']}, 0))"
        return return_string