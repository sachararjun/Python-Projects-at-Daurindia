import pyttsx3                 #pip install pyttsx3
import datetime
import wikipedia               #pip install wikipedia
import webbrowser              #pip install webbrowser
import os
import speech_recognition as sr        #pip install SpeechRecognition
import smtplib                         #pip install smtplib
import random                        #pip install random
from akhbaar import akhbaar        #module made by me named as akhbaar.py
import psutil                     #pip install psutil
import pyjokes                     # pip install pyjokes
import requests, json              #inbuilt
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)                            #Speed of the voice 

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#greet or wishes from assistant#
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    elif hour>=18 and hour<21:
        speak("Good Evening Sir!")

    else:
        speak("Its been night Sir!")

    speak("I am ginnie, your assistant, how may I help you.")

#take command from user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        # speak(query)

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

#sends email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'YourPassword`')                 #Fill your own Email Id and Password
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#check current time
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

#check current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)
    

#check current day
def day():
    now = datetime.datetime.now()
    day = now.strftime("%A")
    speak(f"Today is {day}")
    print(day)

#take screenshots
def screenshot(img_name):
    img = pyautogui.screenshot()
    img.save(
        "C:\\Users\\hp\\Pictures\\Screenshots\\"+ img_name +".png"
    )

#say non funny jokes
def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

#check current weather
def weather():
    api_key = "YOUR-API_KEY"                              #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    speak("tell me which city")
    city_name = takecommand()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        print(r)
        speak(r)
    else:
        speak(" City Not Found ")

#assistant's personal info and its features
def personal():
    speak(
        "My name is Ginnie, version 1.o. I am your voice assistant."
    )
    features = ''' i can help to do lot many things like..
    i can tell you the current time, date and day,
    i can tell you the current weather,
    i can create notes for you and can also read that list,
    i can take screenshots,
    i can send email to your boss or family or your friend,
    i can tell you non funny jokes,
    i can open google, youtube, vs code and github,
    i can search the thing on wikipedia,
    i can read latest news for you and,
    i can shut down, restart or logout your system,
    tell me what can i do for you??'''
    print(features)
    speak(features)

#Main 
if __name__ == "__main__":
    greet()
    # if 1:                              #if the user wants to run the program only once
    while True:                          #if the user wants to continue until the user say exit
        query = takecommand().lower()


        #searches anything from wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        #open youtube
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        #open google
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        #open github
        elif 'open github' in query:
            webbrowser.open("https://github.com")

        #open coursera
        elif 'open coursera' in query:
            webbrowser.open("https://www.coursera.org/")

        #open vscode
        elif 'open code' in query:
            pathCode = 'C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(pathCode)

        #speaks news        
        elif 'news' in query:
            akhbaar()

        #plays music
        elif 'play music' in query:
            music_dir = 'C:\\Users\\hp\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            ran = random.random() * 100
            os.startfile(os.path.join(music_dir, songs[int(ran)]))        

        #time
        elif 'time' in query:
            time()

        #date
        elif 'date' in query:
            date()
            

        #day
        elif 'day' in query:
            day()

        #email
        elif 'email' in query:
            try:
                speak("to whom sir,")
                name = takecommand()
                name = name.lower()
                emails={                                 #dictionary which contains names and the corresponding email id
                    name: email_id
                }
                #print(emails[name])
                if name not in emails:
                    speak('Name is not in the list') 
                speak("What should I say?")
                content = takecommand()
                to = emails[name]    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email!")

        #create notes
        elif "notes" in query:
            speak("What to be note?")
            data = takecommand()
            speak("You said" + data)
            with open("notes.txt", "a") as note_file:
                note_file.write('\n')
                x=datetime.datetime.now()
                note_file.write(f"On {x.day}-{x.month}-{x.year} You said: {data}")
            
        
        #reading notes list
        elif ("what to do" in query or "remember" in query):
            with open("notes.txt") as note_file:
                speak("Notes are: " + note_file.read())


        #personal info
        elif ("yourself" or "you" or "features" or "help")in query:
            personal()
        

        #screenshot
        elif "screenshot" in query:
            speak("save as")
            img_name = takecommand()
            screenshot(img_name)
            speak("Done!")
            print("Done")

        #jokes
        elif "joke" in query:
            jokes()
            

        #weather
        elif ("weather" or "temperature") in query:
            weather()

        #sysytem logout/ shut down etc
        elif "logout" in query:
            os.system("shutdown -1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shut down" in query:
            os.system("shutdown /r /t 1")

        #exit
        elif ('bye' or 'stop') in query:
            speak("I am turning off, Good Bye Sir, Have a good day.")
            quit()
