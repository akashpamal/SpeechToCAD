from object_3d import PrimitiveObject3D, ExtrudedObject3D
from all_objects_2d import Circle, Rectangle, Square

class Sphere(PrimitiveObject3D):
    
    def __init__(self, radius=None):
        super().__init__()
        self.object_type = 'sphere'
        self.properties.update({'radius' : radius})

    def set_prop(self, property_name, value):
        return super().set_prop(property_name, value)

    def to_string_fusion(self):
        circle = Circle(radius = self.get_prop('radius'))
        part1 = circle.to_string_fusion()
        part2 = """
        axisLine = sketch.sketchCurves.sketchLines.addByTwoPoints(adsk.core.Point3D.create(-1 * %d, 0, 0), adsk.core.Point3D.create(%d, 0, 0))
        revolves = rootComp.features.revolveFeatures
        revInput = revolves.createInput(sketch.profiles[-1], axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
        revInput.setAngleExtent(False, adsk.core.ValueInput.createByReal(2 * math.pi))
        ext = revolves.add(revInput)
        """ % (self.get_prop('radius'), self.get_prop('radius'))
        
        return part1 + part2
    
class Cylinder(PrimitiveObject3D):
    
    def __init__(self, radius=None, height=None):
        super().__init__()
        self.object_type = 'cylinder'
        self.properties.update({'radius' : radius, 'height' : height})

    def to_string_fusion(self):
        # Make a new circle with radius "radius"
        circle = Circle(radius = self.get_prop('radius'))
        part1 = circle.to_string_fusion()
        # Extrude the circle by height "height"
        part2 = f"# DRAWING A CYLINDER\n        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal({self.get_prop('height')}), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)\n"
        return part1 +  "        " + part2    

class Cube(PrimitiveObject3D):
    
    def __init__(self, side_length=None):
        super().__init__()
        self.object_type = 'cube'
        self.properties.update({'side_length' : side_length})

    def to_string_fusion(self):
        square = Square(side_length=self.get_prop('side_length'))
        part1 = square.to_string_fusion()
        # Extrude the circle by height "height"
        part2 = f"# DRAWING A CUBE\n        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal({self.get_prop('side_length')}), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)\n"
        return part1 +  "        " + part2