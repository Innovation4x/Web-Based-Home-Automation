
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import paho.mqtt.client as paho



broker="10.5.15.103"
port=1883
def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass


client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)    


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        print('speak say anything')
        # r.pause_threshold = 0.5
        audio = r.listen(source)    
        print("done listening")    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    while True:
    # if 1:
        query = takeCommand().lower()
        print(query)
        if 'turn on' in query:
            ret= client1.publish("led", "on")

        elif 'turn off' in query:
            ret= client1.publish("led", "off")
