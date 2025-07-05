import speech_recognition as sr
import pyttsx3
import os
import subprocess
import cohere


COHERE_API_KEY = "lj9PsWN98AxUnq6JsqerZM6ffeq2owEdoQLnImyV"
co = cohere.Client(COHERE_API_KEY)

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("Smith:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.8
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def ask_cohere(prompt):
    try:
        response = co.generate(
            model='command-light',  # safer model, available in most accounts
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.generations[0].text.strip()
    except Exception as e:
        print("Cohere API Error:", e)
        return "Sorry, I had a problem contacting Cohere."

def run_smith():
    speak("Hey Jagmeet, I'm Smith, your assistant. How can I help you?")

    while True:
        command = listen()
        if not command:
            continue

        if "stop smith" in command or "goodbye" in command:
            speak("Goodbye! See you soon.")
            break

        # System commands
        elif "open vs code" in command:
            speak("Opening Visual Studio Code.")
            os.system("code")
        elif "open chrome" in command:
            speak("Opening Chrome.")
            subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif "open downloads" in command:
            speak("Opening Downloads folder.")
            os.startfile(os.path.expanduser("~/Downloads"))
        elif "open d drive" in command:
            speak("Opening D drive.")
            os.startfile("D:\\")

        else:
            speak("Let me think...")
            response = ask_cohere(command)
            speak(response)

if __name__ == "__main__":
    run_smith()
