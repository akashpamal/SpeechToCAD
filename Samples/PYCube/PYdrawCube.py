#Author-
#Description-

import adsk.core, adsk.fusion, traceback

def main():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct
        design = product
        # Get reference to the root component
        rootComp = design.rootComponent
        
        # Create a new component
        occurrence = rootComp.occurrences.addNewComponent(adsk.core.Matrix3D.create())
        component = occurrence.component
        
        # Name the component
        component.name = "Cube"
        
        #Get reference to the sketchs and plane
        sketches = component.sketches
        xyPlane = component.xYConstructionPlane
        
        #Create a new sketch and get lines reference
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        
        #Create first two points
        x=0
        y=0
        z=0
        point1 = adsk.core.Point3D.create(x, y, z)
        x=1
        y=0
        z=0
        point2 = adsk.core.Point3D.create(x, y, z)
        
        #Create Line
        lines.addByTwoPoints(point1, point2)
        
        #Repeat to create 3 more lines (purposely verbose code)
        point1 = point2
        x=1
        y=1
        z=0
        point2 = adsk.core.Point3D.create(x, y, z)
        lines.addByTwoPoints(point1, point2)
        point1 = point2
        x=0
        y=1
        z=0
        point2 = adsk.core.Point3D.create(x, y, z)
        lines.addByTwoPoints(point1, point2)
        point1 = point2
        x=0
        y=0
        z=0
        point2 = adsk.core.Point3D.create(x, y, z)
        lines.addByTwoPoints(point1, point2)
    
        #Get reference to the first profile of the sketch
        profile = sketch.profiles.item(sketch.profiles.count-1)
        
        #Get extrude features reference
        extrudes = component.features.extrudeFeatures
        
        #Create input object for the extrude feature
        extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(1)
        extInput.setDistanceExtent(False, distance)
        
        #Create extrusion
        extrudes.add(extInput)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

main()
