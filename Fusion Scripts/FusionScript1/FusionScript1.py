import adsk.core, adsk.fusion, math, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        # doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.

        
        # DRAWING A SPHERE
        # Draw a circle.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        circle = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)
        
        # Draw a line to use as the axis of revolution.
        axisLine = sketch.sketchCurves.sketchLines.addByTwoPoints(adsk.core.Point3D.create(-1 * 2, 0, 0), adsk.core.Point3D.create(2, 0, 0))

        # Get the profile defined by half of the circle.
        prof = sketch.profiles.item(0)

        # Create an revolution input to be able to define the input needed for a revolution
        # while specifying the profile and that a new component is to be created
        revolves = rootComp.features.revolveFeatures
        revInput = revolves.createInput(prof, axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)

        angle = adsk.core.ValueInput.createByReal(2*math.pi)
        revInput.setAngleExtent(False, angle)

        # Create the extrusion.
        ext = revolves.add(revInput)
        
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        circles = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 1)
        # DRAWING A CYLINDER
        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(20), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(10, 10, 0))
        # DRAWING A CUBE
        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(10), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        """
        # Draw a circle.
        circles = sketch.sketchCurves.sketchCircles
        circle = circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2) #radius in cm
        
        # sketch.sketchCurves.sketchRectangle


        # Draw a line to use as the axis of revolution.
        lines = sketch.sketchCurves.sketchLines
        axisLine = lines.addByTwoPoints(adsk.core.Point3D.create(-3, 0, 0), adsk.core.Point3D.create(3, 0, 0))

        # Get the profile defined by half of the circle.
        prof = sketch.profiles.item(0)

        # Create an revolution input to be able to define the input needed for a revolution
        # while specifying the profile and that a new component is to be created
        revolves = rootComp.features.revolveFeatures
        revInput = revolves.createInput(prof, axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)

        # Define that the extent is an angle of 2*pi to get a sphere
        angle = adsk.core.ValueInput.createByReal(2*math.pi)
        revInput.setAngleExtent(False, angle)

        # Create the extrusion.
        ext = revolves.add(revInput)
        """
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))