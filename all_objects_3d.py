from object_3d import PrimitiveObject3D, ExtrudedObject3D
from all_objects_2d import Circle, Rectangle, Square

class Sphere(PrimitiveObject3D):
    
    def __init__(self, radius=None):
        super().__init__()
        self.object_type = 'sphere'
        self.object_properties.update({'radius' : radius})
        self.old_alternative_properties.update({'diameter'})
        self.alternative_properties.update({
            "diameter" : ('radius', lambda x : x/2)
        })

    def to_string_fusion(self):
        circle = Circle(radius = self.get_prop('radius'))
        part1 = circle.to_string_fusion()
        part2 = """
        # DRAWING A SPHERE
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
        self.object_properties.update({'radius' : radius, 'height' : height, 'sketch_plane' : 'rootComp.xYConstructionPlane'}) # TODO delete sketch_plane from this dictionary and use self.sketch_plane instead
        self.old_alternative_properties.update({'diameter'})
        self.alternative_properties.update({
            "diameter" : ('radius', lambda x : x/2)
        })

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
        self.object_properties.update({'side_length' : side_length})
        self.old_alternative_properties.update({'length'})
        self.alternative_properties.update({
            'length' : ('side_length', lambda x : x)
        })

    def to_string_fusion(self):
        square = Square(side_length=self.get_prop('side_length'))
        # square.set_prop('sketch_profile' : )
        part1 = square.to_string_fusion()
        # Extrude the circle by height "height"
        part2 = f"# DRAWING A CUBE\n        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal({self.get_prop('side_length')}), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)\n"
        return part1 +  "        " + part2