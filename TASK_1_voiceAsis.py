import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import os

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

greeting = "Hello there! How can I help you today?"

#text
def speak(text):
    engine.say(text)
    engine.runAndWait()

#Chrome
def open_chrome():
    speak("Opening Chrome")
    os.system('start chrome')

#time
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

#date
def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    speak(f"The current date is {current_date}")

#websearch
def search_web(query):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
    speak(f"Searching for {query} on the web.")


while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        print("Recognizing...")
        command = recognizer.recognize_google(audio)

        if "hello" in command.lower():
            speak(greeting)
        elif 'chrome' in command.lower():
            open_chrome()
        elif "time" in command.lower():
            get_time()
        elif "date" in command.lower():
            get_date()
        elif "search" in command.lower():
            query = command.split("search for")[-1]
            search_web(query)
        else:
            speak("I'm sorry, I don't understand that command.")

    except sr.UnknownValueError:
        speak("I couldn't understand your command. Please try again.")
    except sr.RequestError as e:
        speak("There was an error. Please try again later.")
        print(f"Could not request results from Google Speech Recognition service; {e}")