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
        sketches = rootComp.sketches;
        xyPlane = rootComp.xYConstructionPlane;
        sketch = sketches.add(xyPlane)

        #rectangle creation
        lines = sketch.sketchCurves.sketchLines
        width = 8
        height = 2
        rec1 = lines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(width, height, z))

        #rectangle extrusion
        length = 
        

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
