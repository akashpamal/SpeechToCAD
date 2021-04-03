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
        
        coordinates = [
            0,0,0,
            1,0,0,
            1,1,0,
            0,1,0,
            0,0,0
        ]
        # Name the component
        component.name = "Cube"
        
        #Get reference to the sketchs and plane
        sketches = component.sketches
        xyPlane = component.xYConstructionPlane
        
        #Create a new sketch and get lines reference
        sketch = sketches.add(xyPlane)
        lines = sketch.sketchCurves.sketchLines
        i = 0
        while i < len(coordinates)-3:
            point1 = adsk.core.Point3D.create(coordinates[i], coordinates[i+1], coordinates[i+2])
            point2 = adsk.core.Point3D.create(coordinates[i+3], coordinates[i+4], coordinates[i+5])
            adsk.core.BoundingBox3D.create()
            #Create Line
            lines.addByTwoPoints(point1, point2)
            i += 3
        
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




"""
#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('Hello script')



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
"""