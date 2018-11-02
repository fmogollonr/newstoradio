import pyttsx3;

class tts:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', "spanish")
        self.engine.setProperty('rate',150)

    def say(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
