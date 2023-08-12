import speech_recognition as sr
import pyttsx3

import os

from dotenv import load_dotenv

load_dotenv()

key = os.getenv("")

import openai

openai.api_key = key


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

r = sr.Recognizer()

def record_text():
    while(1):
        try:

            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                print("Listening")

                audio2 = r.listen(source2)


