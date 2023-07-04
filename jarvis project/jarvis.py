import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib



engine = pyttsx3.init('sapi5')
vocies = engine.getProperty('voices')

engine.setProperty('voices', vocies[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def  takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query


def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")

    elif hour>12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("I am Jarvis sir . please tell me how can i help you")

#to send email
def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yuvrajsingh96909@gmail.com',"01y01s000000")
    server.sendmail('yuvrajsingh96909@gamil','',"i love you")
    server.close()


if __name__ == "__main__":
    



    wish()



    while True:

     if 1:


        query= takecommand().lower()

        if "notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)

        elif "fusion 360" in query:
            apath= "C:\\Users\\mohan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Autodesk\\Autodesk Fusion 360.lnk"
            os.startfile(apath)
        
        elif "Visual Studio" in query:
            apath= "C:\\Users\\mohan\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(apath)
        
        elif "this PC" in query:
            apath= "C:\\Users\\mohan\\OneDrive\\Desktop"
            os.startfile(apath)
        
        elif "command prompt" in query:
            os.system("start cmd")

        elif "camera" in query:
            cap= cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.inshow('aebcan' , img)
                k = cv2.waitKey(50)
                if k==27:

                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "music" in query :
            music_dir="C:\\Users\\Yuvraj\\Music"
            songs= os.listdir(music_dir)
            rd= random.choice(songs)

            for songs in songs:
               
                os.startfile(os.path.join(music_dir,songs))



        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        

        elif "instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "google" in query:
            speak("sir,what should i search on google ")
            cm= takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            kit.sendwhatmsg("+919209077622","this is testing protocol",10,24 )

        elif "play song on youtube" in query:
            kit.playonyt("BALLER")

        # elif "email to avi " in query:
        #     try:
        #         speak("what should i say?")
        #         content = takecommand().lower()
        #         to="yuvrajsingh96909@gmail.com"

