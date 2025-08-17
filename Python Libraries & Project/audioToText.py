import speech_Recognition as sr

recognizer = sr.Recognizer()

audio_file = "audio.wav"

from pydub import audioSegment

audioSegment.from_mp3(audio_file).export(audio_file,format="wav")

with sr.AudioFile(audio_file) as source :
    audio_data = recognizer.record(source)


try:

    text = recognizer.recognize)google(audio_data)
    print("extracted Text :",text)

except sr.unknownValueError:
    print("couldnt understand the audio")

except sr.RequestError as e:
    print("API Error :",e)