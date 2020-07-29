import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is Jarvis Adik")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

# time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

# date()

def wishme():
    speak("Welcome back Advait Sir")
    # speak("The current time is")
    time()
    # speak("The current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<=18:
        speak("Good afternoon sir!")
    elif hour >=18 and hour<=24:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")

    speak("Jarvis at your service Please tell me how can I help you?")

# wishme()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

# takeCommand()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcd@gmail.com','123')
    server.sendmail('abcd@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)   
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content - takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in chrome' in query:
            speak('What should i search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
  
        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shoutdown' in query:
            os.system("shutdown /s /t l")

        elif 'restart' in query:
            os.system("shutdown /r /t l")

        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'offline' in query:
            quit()    
        


