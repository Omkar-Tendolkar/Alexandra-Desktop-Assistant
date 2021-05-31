import datetime
import os
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour <15:
        speak("Good Afternoon")
    elif hour >=15 and hour <19:
        speak("Good Evening")

    speak("Hello, My name is Alexandra, Speed 1 terahertz, memory 1 zeta byte, version 1.O")
    speak("How may i help you today?")
    print("How may i help you today?")
def takeCommand():
    '''
    Its take the user voices command and
    respond, do the work for given command as output
    speak("I am Alexandra, Sir how may i help you today?")
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Pardon Sir, but can you repeat again, please...?")
        speak("Pardon Sir, but can you repeat again, please...?")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtplib.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender-email@gmail.com', 'your-email-password') # Put sender's email address and password here (Note: Before sending make that gmail check for less-secure app is enable
    server.sendmail('sender-email@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishME()
    while True:
    # if 1:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open music' in query:
            music_dir = "C:\\Users\\Omkar Tendolkar\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'email to omkar' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "reciever-email@gmail.com" #Put reciever email here for sending
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Omkar Sir, I was failed to sent your email")
        elif 'you stop' in query:
            speak ("Thank you for using me sir")
            speak("Bye Bye")
            break


