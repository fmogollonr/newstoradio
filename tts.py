from google_speech import Speech

class tts:
    def __init__(self):
        self.lang ="es"

    def say(self,text):
        speech=Speech(text,self.lang)
        speech.play()
