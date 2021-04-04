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

        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(5, 5, 0))
        # DRAWING A CUBE
        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(5), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        """
        Do not delete this section – it's used for parsing
        """
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))