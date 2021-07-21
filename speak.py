from gtts import gTTS
from playsound import playsound
import os

os.system("clear")
while True:
	text_s = input(">> ")
	if(text_s == "q"): break
	tts = gTTS(text=text_s, lang="tr")
	name = "audio.mp3"
	tts.save(name)
	playsound(name)
	url = "sudo rm "+name
	os.system(url)

