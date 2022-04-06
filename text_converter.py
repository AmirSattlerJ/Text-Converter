from gtts import gTTS
import pyttsx3
from deep_translator import GoogleTranslator as gt
class text_converter:
    def __init__(self, text: str):
        self.text = text
    def translater_text(self, target_language: str = 'en', output_file: str = 'translate.txt'):
        self.target_language = target_language
        self.output_file = output_file
        self.tt = gt('auto', self.target_language).translate(self.text)
        try:
            print('Was Translated ! ! !')
            with open(self.output_file, 'w', encoding='utf-8') as t: 
                t.write(self.tt)
        except Exception as e:
            print(e)
            print(f'Python can Not write {self.target_language} in file {self.output_file}')
    def android_tts(self, lang: str = 'en', output_file: str = 'voice.mp3', slow: bool = False):
        self.lang = lang
        self.output_file = output_file
        self.slow = slow
        tts = gTTS(self.text, lang=self.lang, slow=self.slow)
        tts.save(self.output_file)
    def PC_tts(self, rate: str = '100', volume: str = '1.0', voice: str = 'male', output_file: str = 'tts_PC.mp3'):
        eng = pyttsx3.init()
        self.output_file = output_file
        self.rate = rate
        self.volume = volume
        self.voice = voice
        if self.voice.lower() == 'male' or 'man':
            self.voices = eng.getProperty('voices')[0].id
        elif self.voice.lower() == 'female' or 'woman':
            self.voices = eng.getProperty('voices')[1].id
        else: 
            print('Male or Female')
            exit()
        self.voices = eng.getProperty('voices')
        eng.setProperty('rate', self.rate)
        eng.setProperty('volume', self.volume)
        eng.setProperty('voice', self.voices)
        eng.say(self.text)
        eng.save_to_file(self.text, self.output_file)
        eng.runAndWait()
