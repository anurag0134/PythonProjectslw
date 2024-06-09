import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import subprocess
import smtplib
import pywhatkit
import boto3
import cv2
from PIL import Image, ImageOps
import numpy as np
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def Ec2():
    ec2 = boto3.resource('ec2',region_name="ap-south-1", aws_access_key_id="FAKIA4XXKBRY4AFX67T3",aws_secret_access_key="NwFEeRnS61zlKG0d+AA1r94h97KWYS3vkl+WdstJ+")
    instance = ec2.create_instances(
    ImageId='ami-0f58b397bc5c1f2e8',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    )

def sendWhatsApp():
    pywhatkit.sendwhatmsg_to_group_instantly("HMnmDlqL7uZUPHmFl3V5rD ", "Hey All!")

def sendEmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tonystark83033@gmail.com", "lhmyxcvfjtxaceqr")
    message = "Message_you_need_to_send"
    subject="test python mail server"
    body = "I love python"
    message = ":{}/n/n{}".format(subject,body)

    s.sendmail("sender_email_id", "", message)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() # Without this command, speech will not be audible to us.

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you?")

def Openvlc():
    media_path = "C:\Program Files\Windows Media Player\wmplayer.exe"
    subprocess.run(media_path)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return None
    return query

sendWhatsApp()