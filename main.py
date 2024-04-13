import datetime
import webbrowser
import os
import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.spVoice")

def say(text):
    os.system(f"say{text}")
def say(said):
    speaker.Speak(said)



def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as exe:
            return "error occurred"

    say("hello,i am jarvis")

    while 1:
        print("listening...")
        query = takecommand()
        sites=[["youtube","https://youtube.com"],["w3school","https://www.w3schools.com"],["github","https://github.com"],["gmail", "https://mail.google.com"]]
        for site in sites:
            if f"open{site[0]}".lower() in query.lower():
                say(f"opening {site[0]}")
                webbrowser.open(site[0])
                say(query)
        if "open music" in query :
            musicpath = "filename"
            os.startfile(musicpath)

        if "the time " in query :
            time = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {time}")

        elif "using the AI " in query:
            ai(prompt=query)

        elif "jarvis quit" in query:
            exit()
        else:
            print("chating....")

