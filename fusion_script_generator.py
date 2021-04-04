from os import read
from all_objects_2d import Rectangle
from all_objects_3d import Cylinder, Cube, Sphere

class FusionScriptGenerator():
    
    def __init__(self, filename):
        self.filename = filename
        self._closing_lines = None
        self._saving_lines = """
        #folder = 'C:/Temp/STLExport/'
        #Construct the output filename.
        filename = 'creation' + '.stl'

        exportMgr = adsk.fusion.ExportManager.cast(design.exportManager)
        stlOptions = exportMgr.createSTLExportOptions(rootComp)
        stlOptions.meshRefinement = adsk.fusion.MeshRefinementSettings.MeshRefinementMedium
        stlOptions.filename = filename
        exportMgr.execute(stlOptions)
                """
        self.objects = []
        self.sketches = ['sketch']

        with open(self.filename, 'w') as target_file:
            with open('./SpeechToCAD/Fusion Scripts/FusionScriptShell/FusionScriptShell.py') as source_file:
                source_lines = source_file.readlines()
                line_divider = [index for index, elem in enumerate(source_lines) if '"""' in elem][0]
                target_file.write(''.join(source_lines[ : line_divider]))
                self._closing_lines = ''.join(source_lines[line_divider : ])
    
    def add_object(self, object):
        with open(self.filename, 'a') as target_file:
            target_file.write('        ' + object.to_string_fusion() + '\n')
    
    def close_generator(self):
        with open(self.filename, 'a') as target_file:
            target_file.write(self._closing_lines)
            
    def add_save(self):
        with open(self.filename, 'a') as target_file:
            target_file.write(self._saving_lines)

if __name__ == '__name__':
    print('starting run of generator')
    print('running the script generator')
    fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    fusion_script_generator.add_object(Sphere(radius=2))
    fusion_script_generator.add_object(Cylinder(radius=1, height=20))
    fusion_script_generator.add_object(Cube(side_length=10))
    # fusion_script_generator.add_object(Rectangle(width=10, height=20))
    fusion_script_generator.close_generator()
    fusion_script_generator.add_save()
    print('finished saving file')

print('hello there')