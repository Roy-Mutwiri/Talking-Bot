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

                MyText = r.recognize_google(audio2)

                return MyText

        except sr.RequestError as e:
            print(f"Could Not Request Results:  {0}" .format(e))

        except sr.UnknownValueError:
            print("Unknown Error Occurred")


def send_to_chatGPT(messages, model = "gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(

        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5

    )

