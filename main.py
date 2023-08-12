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

