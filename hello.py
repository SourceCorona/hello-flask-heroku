from flask import Flask, request
import random, string, os
from gtts import gTTS


def random_string(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello_world():
    rand = random_string(9)
    text = request.args.get("text")
    lang = request.args.get("lang")
    myobj = gTTS(text=text, lang=lang, slow=False)
    if myobj.save(rand + ".mp3") != False:
        return ("saved as  " + rand + ".mp3")
    else:
        return ("error")


if __name__ == '__main__':
    app.run()
