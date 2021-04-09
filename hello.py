from flask import Flask, request
import random, string,os
from gtts import gTTS

def glob(path):
    files = []
    for dentry in os.scandir(path):
        files.append(dentry.name)
    return (files)

def random_string(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

app = Flask(__name__)

@app.route("/")
def homepage():
    return "hello"

@app.route("/speech", methods=['GET'])
def hello_world():
    #os.mkdir("temp")
    rand = random_string(9)
    text = request.args.get("text")
    lang = request.args.get("lang")
    myobj = gTTS(text=text, lang=lang, slow=False)
    if myobj.save("temp/"+rand + ".mp3") != False:
        z = ("{}\n\n===========================\n<a href='{}'><h1>temp/{}.mp3 </h1></a> ".format(glob("temp"),rand+".mp3",rand))
        return z
        #return ("<h2>dhurgham.</h2>","\nsaved as  " + "temp/"+ rand + ".mp3")
    else:
        return ("error")


if __name__ == '__main__':
    app.run()
