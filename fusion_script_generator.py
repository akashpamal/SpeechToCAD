from .Source.Object_Heirarchy.all_objects_2d import Rectangle
# from Source.Object_Heirarchy.object_2d import Object2D

class FusionScriptGenerator():
    
    def __init__(self, filename):
        self.filename = filename
        self._closing_lines = None
        self.objects = []
        self.sketches = ['sketch']

        with open(self.filename, 'w') as target_file:
            with open('./Fusion Scripts/FusionScriptShell/FusionScriptShell.py') as source_file:
                source_lines = source_file.readlines()
                line_divider = [index for index, elem in enumerate(source_lines) if '"""' in elem][0]
                target_file.write(''.join(source_lines[ : line_divider]))
                self._closing_lines = ''.join(source_lines[line_divider : ])
    
    def add_object(self, object):
        with open(self.filename, 'w') as target_file:
            target_file.write(object.to_string_fusion())
    
    def close_generator(self):
        with open(self.filename, 'a') as target_file:
            target_file.write(self._closing_lines)
       
            

fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
fusion_script_generator.objects.append(Rectangle(width=5, height=5))
fusion_script_generator.close_generator()