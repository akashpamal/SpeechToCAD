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

        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        circles = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 2)
        # DRAWING A CYLINDER
        extrude = rootComp.features.extrudeFeatures.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(15), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        circles = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), 5.0)

        # DRAWING A SPHERE
        axisLine = sketch.sketchCurves.sketchLines.addByTwoPoints(adsk.core.Point3D.create(-1 * 5, 0, 0), adsk.core.Point3D.create(5, 0, 0))
        revolves = rootComp.features.revolveFeatures
        revInput = revolves.createInput(sketch.profiles[-1], axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
        revInput.setAngleExtent(False, adsk.core.ValueInput.createByReal(2 * math.pi))
        ext = revolves.add(revInput)
        
        """
        Do not delete this section – it's used for parsing
        """
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
        #folder = 'C:/Temp/STLExport/'
        #Construct the output filename.
        filename = 'creation' + '.stl'

        exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
        stlOptions = exportMgr.createSTLExportOptions(rootComp)
        stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        stlOptions.filename = filename
        exportMgr.execute(stlOptions)
                