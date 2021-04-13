from all_objects_2d import *
from all_objects_3d import *
from object_2d import Object2D
from object_3d import PrimitiveObject3D, ExtrudedObject3D
from fusion_script_generator import FusionScriptGenerator
import speech_recognition as sr
import pyaudio
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
        starting_index = [index for index, elem in enumerate(all_words) if elem in self.options][0]

        object_in_progress = self.options[all_words[starting_index]]()
        possible_properties = object_in_progress.get_prop_list()
        loaded = False
        property = None
        value = None
        for word in all_words[starting_index : ]:
            if word in possible_properties:
                property = word
                if loaded:
                    object_in_progress.set_prop(property, value)
                    loaded = False
                    property = None
                    value = None
                else:
                    loaded = True
            try:
                value = int(word)
                if loaded:
                    object_in_progress.set_prop(property, value)
                    loaded = False
                    property = None
                    value = None
                else:
                    loaded = True
            except ValueError:
                pass
            
            if word in self.options:
                created_objects.append(object_in_progress)
                object_in_progress = self.options[word]()
                possible_properties = object_in_progress.get_prop_list()
                loaded = False
                property = None
                value = None
        created_objects.append(object_in_progress)
        return created_objects[1 : ]

    def _pre_process_text(self, raw_text):
        # pre_processed_text = word_tokenize(raw_text)
        # TODO add lemmatization
        # pre_processed_text = word_tokenize(raw_text)
        pre_processed_text = raw_text.split()
        pre_processed_text = [elem.lower() for elem in pre_processed_text]
        return pre_processed_text

    def continuous_listen(self): # TODO make this method asyncrhonous
        init_rec = sr.Recognizer()
        while True:
            print("Let's speak!!")
            with sr.Microphone() as source:
                audio_data = init_rec.record(source, duration=5)
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                print(text)

if __name__ == '__main__':
    text_parser = TextParser()
    text_parser.continuous_listen()

    created_object_list = text_parser.text_to_objects('Make a cube with 20 cm side length')
    [print(str(elem)) for elem in created_object_list]

    fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    
    for elem in created_object_list:
        fusion_script_generator.add_object(elem)
    
    fusion_script_generator.close_generator()