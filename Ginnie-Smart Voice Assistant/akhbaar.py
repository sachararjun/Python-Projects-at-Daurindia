# Akhbaar padhke sunaao used as module
import requests
import json
import speech_recognition as sr

#speak
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

#take command from user
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        return query

#reads news
def akhbaar():
    speak("News for today.. Lets begin")
    url = "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=YOUR_API_KEY"           #API key for news
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        print("Either <CONTINUE> or <STOP>.")
        query = takecommand()
        if 'continue' in query:
            continue
        else:
            break
        speak("Moving on to the next news..Listen Carefully")
        

    speak("Thanks for listening...")

#Main
if __name__ == '__main__':
    akhbaar()
