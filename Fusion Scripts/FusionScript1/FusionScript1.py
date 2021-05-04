#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('Sending message')
    s.sendall(b"Hello, world")
    print('Finished sending message')
    data = s.recv(1024)

print("Received", repr(data))
exit()

import adsk.core, adsk.fusion, math, traceback
import sys
# It looks like calls to the Fusion API are handled on a separate thread or processor core since objects are created at the same time as console I/O activity
# for i in range(10000):
#     print(i)
# sys.path.append(".") # Adds higher directory to python modules path.
# from runner_gui import Application
# import os
# print(os.getcwd())

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
        design = app.activeProduct

        # Get the root component of the active design.
        rootComp = design.rootComponent

        #Up Direction
        upDir = adsk.core.Vector3D.create(0,0,1)

        # Create a new sketch on the xy plane.
        sketch = rootComp.sketches.add(rootComp.xYConstructionPlane)
        rec1 = sketch.sketchCurves.sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(0, 0, 0), adsk.core.Point3D.create(20, 20, 0))
        
        #Extrudes object
        extrude = rootComp.features.extrudeFeatures

        # DRAWING A CUBE
        cube = extrude.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(20), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        for face in cube.faces:
            if face.geometry.objectType == adsk.core.Plane.classType():
                faceEval = face.evaluator
                (retVal, normal) = faceEval.getNormalAtPoint(face.pointOnFace)

                if normal.angleTo(upDir) < 0.001:
                    sketch = rootComp.sketches.add(face)
                    break
        
        circles = sketch.sketchCurves.sketchCircles.addByCenterRadius(adsk.core.Point3D.create(10, 10, 0), 5)
        cylinder = extrude.addSimple(sketch.profiles[-1], adsk.core.ValueInput.createByReal(15), adsk.fusion.FeatureOperations.NewBodyFeatureOperation)


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
                