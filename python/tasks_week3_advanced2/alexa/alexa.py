import speech_recognition as sr
import webbrowser
from gtts import gTTS
import vlc
import os
import pyaudio
from playsound import playsound
from datetime import datetime

r = sr.Recognizer()

def my_voice():
    with sr.Microphone() as source:
        print("Talk")
        r.adjust_for_ambient_noise(source,duration=1)
        audio_text = r.listen(source)
        return audio_text
    
def reco_speech(audio):
        try:
           #text=r.recognize_google(audio,language='ar-EG')
           text=r.recognize_google(audio,language='en-US')
        # using google speech recognition
           print(f"Text: "+text)
           return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand your command.")
            return ""
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return ""
def respoonse(resp) :
     
     text1=gTTS(text=resp,lang='ar',slow=False)
     text1.save("audio.mp4")
     #p=vlc.MediaPlayer("audio.mp4")
     #p.play()
    # os.remove(text1)
     playsound("audio.mp4")


time_list=['time','TIME','وقت',' الوقت']
goole_list=['google','GOOGLE','جوجل']
youtube_list=['youtube','YOUTUBE','يوت يوب']
facebook_list=['facebook','FACEBOOK','فيس بوك']
name_list=['name','NAME',' اسم',' الاسم']

while True:
    x=my_voice()
    y=reco_speech(x).lower().strip()
    if y in time_list:
      time_now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      respoonse(time_now)
    elif y in goole_list:
        webbrowser.open("https://www.google.com")
        response_web = "Opening Google."
        respoonse(response_web)
    elif y in youtube_list:
        webbrowser.open("https://www.youtube.com")
        response_web = "Opening youtube."
        respoonse(response_web)  
    elif y in facebook_list:
        webbrowser.open("https://www.facebook.com")
        response_web = "Opening facebook."
        respoonse(response_web)
    elif y in name_list:
        response_web = "صباح الخير ياسحس "
        respoonse(response_web)
    else:
            response = "مش فاهمك يا صحبى"
            respoonse(response)
            
      