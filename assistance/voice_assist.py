import os
import speech_recognition as sr
from gtts import gTTS

r = sr.Recognizer()
micph = sr.Microphone()

with micph as source:
	print("You can now speak")
	r.adjust_for_ambient_noise(source, duration=0.5)
	# r.adjust_for_ambient_noise(source)
	audio = r.listen(source)
	# audio = r.record(source)

print("Translating your speech.....")
# print("You said: " + r.recognize_google(audio))

said = r.recognize_google(audio)

print("You said: ", said)

if said == 'mute':
	os.system("sysmute.vbs")
elif said == 'unmute':
	os.system("sysunmute.vbs")

# os.system("sysmute.vbs")