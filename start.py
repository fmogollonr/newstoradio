import tts
from flask import Flask, jsonify, request

app = Flask(__name__) #create the Flask app

#speech=tts.tts()
#speech.say("hola ramon")


@app.route('/speak')
def speak():
    #speech=tts.tts()
    #speech.say("probando")
    if 'text' in request.args:
        speech=tts.tts()
        speech.say("Hola "+request.args['text'])
        return 'Say '+request.args['text']
    else:
  	    return 'Dont say anything'

@app.route('/query-example')
def query_example():
    return 'Todo...'

@app.route('/form-example')
def form_example():
    return 'Todo...'

@app.route('/json-example')
def json_example():
    return 'Todo...'

if __name__ == '__main__':
    app.run(debug=False, port=5000) #run app in debug mode on port 5000