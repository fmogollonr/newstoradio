import pyttsx3;
engine = pyttsx3.init();
engine.setProperty('voice', "spanish");
engine.say("Hola, buenos dias");
engine.runAndWait() ;
