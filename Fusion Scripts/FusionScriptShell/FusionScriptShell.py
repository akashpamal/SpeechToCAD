import adsk.core, adsk.fusion, math, traceback

def run(context):
    ui = None
    try: 
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)

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