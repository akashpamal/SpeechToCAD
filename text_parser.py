from all_objects_2d import *
from all_objects_3d import *
from object_2d import Object2D
from object_3d import PrimitiveObject3D, ExtrudedObject3D
from fusion_script_generator import FusionScriptGenerator
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords


class TextParser():
    def __init__(self) -> None:
        self.options = {
            Cube : ('cube', 'box'),
            Sphere : ('sphere', 'ball'),
            Cylinder : ('cylinder', 'barrel'),
        }

        temp_new_dict = {}
        for key, value_tuple in self.options.items():
            for value in value_tuple:
                temp_new_dict[value] = key
        # self.all_stopwords = set(stopwords.words('english'))

        self.options = temp_new_dict
    
    def text_to_objects(self, raw_text): # returns a list of objects that were specificed by this text. Some objects may have missing arguments
        all_words = self._pre_process_text(raw_text)
        created_objects = []
        object_in_progress = None
        for word in all_words:
            try:
                if object_in_progress is not None:
                    object_in_progress.set_next_prop(int(word))
            except ValueError:
                pass
            if word in self.options:
                created_objects.append(object_in_progress)
                object_in_progress = self.options[word]()
        created_objects.append(object_in_progress)
        return [elem for elem in created_objects]

    def _pre_process_text(self, raw_text):
        # pre_processed_text = word_tokenize(raw_text)
        # TODO add lemmatization
        # pre_processed_text = word_tokenize(raw_text)
        pre_processed_text = raw_text.split()
        pre_processed_text = [elem.lower() for elem in pre_processed_text]
        return pre_processed_text


if __name__ == '__main__':
    text_parser = TextParser()
    created_object_list = text_parser.text_to_objects('Make a sphere with 2 cm diameter and a cube with a side length of 3')
    created_object_list = created_object_list[1 : ] # remove the None that's at the front of the list
    [print(str(elem)) for elem in created_object_list]

    fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    
    for elem in created_object_list:
        fusion_script_generator.add_object(elem)
    
    fusion_script_generator.close_generator()