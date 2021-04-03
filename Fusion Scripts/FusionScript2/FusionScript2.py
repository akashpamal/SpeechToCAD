#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try: 
        #creating plane and stuff
        app = adsk.core.Application.get()
        ui = app.userInterface

        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)


        #rectangle creation
        lines = sketch.sketchCurves.sketchLines
        rec1 = lines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(8, 2, 0))

        ui.messageBox('hi:\n{}'.format(traceback.format_exc()))
        ui.messageBox(sketch.profiles.format(traceback.format_exc()))
        # print(sketch.profiles)
        
        """
        #rectangle extrusion
        extrudeDistance = adsk.core.ValueInput.createByReal(8)
        #extrude = rootComp.features.extrudeFeatures.addSimple()
        """

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
