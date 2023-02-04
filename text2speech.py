#Make sure gtts is installed
#Command to install gtts: python -m pip install gtts

import gtts
from gtts import gTTS

def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

text = "This is an example to convert text to speech"
filename = "hello.mp3"

text_to_speech(text, filename)
