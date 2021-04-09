from flask import Flask,request
import random,string
from gtts import gTTS
app = Flask(__name__)
class speech:
    def __init__(self,text,lang):
        self.text = text
        self.lang = lang
    def say(text,lang):
        myobj = gTTS(text=text, lang=lang, slow=False)
        if myobj.save(rand + ".mp3") != False:
            return ("saved as  " + rand + ".mp3")
        else:
            return ("error")

@app.route("/", methods=['GET'])
text = request.args.get("text")
lang = request.args.get("lang")
def hello_world():
    return speech.say(text,lang)

if __name__ == '__main__':
    app.run()
