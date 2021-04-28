from all_objects_2d import *
from all_objects_3d import *
from object_2d import Object2D
from object_3d import PrimitiveObject3D, ExtrudedObject3D
from fusion_script_generator import FusionScriptGenerator
import speech_recognition as sr
import pyaudio
import deprecation
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

        # reverse the dictinonary so the key is the keyword and the value is the corresponding Object3d
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
        value = None # TODO add support for a case when the user says two properties that mean the same thing, then a single value. e.g. Side length of 5. side and length may both be properties, but this should be handled smoothly
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
        pre_processed_text = [elem.lower().replace('.', '') for elem in pre_processed_text]

        return pre_processed_text

    @deprecation.deprecated(details="This functionality has been moved to the SpeechParser class")
    def continuous_listen(self): # TODO make this method asyncrhonous
        init_rec = sr.Recognizer()
        all_objects = []
        while True:
            print("Let's speak!!")
            with sr.Microphone() as source:
                audio_data = init_rec.record(source, duration=7) # TODO instead of using a timeout here, listen for a pause in speech
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                print(text)
            added_objects = self.text_to_objects(text)
            all_objects.extend(added_objects)

            print('Added objects:')
            [print(str(elem)) for elem in added_objects]
            print()
            print('All objects:', all_objects)
            [print(str(elem)) for elem in all_objects]
            print('\n' * 3)

class SpeechParser():
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()
        # sr.Microphone.list_microphone_names()
    
    def listen_once(self, adjust_for_ambient_noise=True, return_detailed_response=False):
        with self.mic as source:
            if adjust_for_ambient_noise:
                print('Adjusting for ambient noise...')
                self.recognizer.adjust_for_ambient_noise(source)
            print('Say something!')
            audio =self. recognizer.listen(source)
            print('Finished listening')
        response = {"error" : None, "transcription" : None}

        try:
            print('Recognizing text...')
            transcription = self.recognizer.recognize_google(audio)
            print(transcription)
            response["transcription"] = transcription
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["error"] = "API Unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible. This may be due to an audio source that doesn't have any input
            response["error"] = "Unable to recognize speech"
        
        if return_detailed_response:
            return response
        else:
            return response["transcription"]
    
    def continuous_listen(self, callback_function, stop_condition=lambda : False): # TODO add a stop_condition function
        while not stop_condition():
            transcription = self.listen_once()
            if transcription is None:
                print("We didn't hear anything that time, try again")
            else:
                print('Calling callback function from continuous_listen in SpeechParser')
                created_objects = callback_function(transcription)
                print('Newly created objects:')
                [print(elem) for elem in created_objects]

def main1():
    text_parser = TextParser()
    text_parser.continuous_listen()

    created_object_list = text_parser.text_to_objects('Make a cube with 20 cm side length')
    [print(str(elem)) for elem in created_object_list]

    fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    
    for elem in created_object_list:
        fusion_script_generator.add_object(elem)
    
    fusion_script_generator.close_generator()

def main2_full_test():
    text_parser = TextParser()
    speech_parser = SpeechParser()
    speech_parser.continuous_listen(text_parser.text_to_objects)

def main2_text_parser_test():
    text_parser = TextParser()
    all_objects = text_parser.text_to_objects('Make me a cube with side length 5. Also generate a cylinder with diameter 10 and a height of 13. An additional sphere should have a radius of 5')
    [print(elem) for elem in all_objects]

def main2_with_script_generator_test():
    text_parser = TextParser()
    speech_parser = SpeechParser()
    fusion_script_generator = FusionScriptGenerator('./Fusion Scripts/FusionScript1/FusionScript1.py')
    # text = speech_parser.listen_once()
    text = "Make me a cube with side length 5. Also make me a cylinder with radius 2 and height 15. Finally, make me a sphere with a diameter of 10."
    object_list = text_parser.text_to_objects(text)
    [print(elem) for elem in object_list]
    [fusion_script_generator.add_object(elem) for elem in object_list]
    fusion_script_generator.close_generator()


if __name__ == '__main__':
    main2_with_script_generator_test()