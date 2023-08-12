
'''import speech_recognition as sr
import pyttsx3

import os

from dotenv import load_dotenv

load_dotenv()


'''
import speech_recognition as sr
import pyttsx3
import openai
from dotenv import load_dotenv

load_dotenv()

# Load your OpenAI API key from your environment variables
openai.api_key = ("")


def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def record_text():
    r = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                return text
        except sr.RequestError as e:
            print(f"Could Not Request Results: {e}")
        except sr.UnknownValueError:
            print("Unknown Error Occurred")


def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].message['content']
    return message


def main():
    messages = [{"role": "user", "content": "Please act like Jarvis from Iron man."}]

    while True:
        text = record_text()
        messages.append({"role": "user", "content": text})

        response = send_to_chatGPT(messages)
        SpeakText(response)

        print(response)


if __name__ == "__main__":
    main()
