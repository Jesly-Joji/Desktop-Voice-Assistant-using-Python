# IMPORT STATEMENTS
import pyttsx3 
import speech_recognition as sr
import wikipedia
import eel
from pywhatkit import sendwhatmsg_instantly as kit


# IN-BUILT MODULE
from datetime import datetime   
import os
import subprocess as sp
import webbrowser


eel.init("web")

# INITIALIZATION
engine = pyttsx3.init("sapi5")    # sapi5 API of microsoft  
# engine is of type  <class 'pyttsx3.engine.Engine'>

# CHANGE VOICE DAVID to ZIRA
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

# SPEAK
def speak(text):
   print(text)
   engine.say(text)
   engine.runAndWait()


#WISH
def wish():
   hour=datetime.now().hour
 
   if (hour>=0 and hour<12):
      speak("Good Morning Jesly")
     
   
   elif(hour>=12 and hour<18):
      speak("Good Afternoon Jesly")
     
   else:
      speak("Good Evening Jesly")

   speak("I am Zira, Your Personal Virtual  Assistant")
   speak("How may I help you")


# TAKE COMMAND FROM USER

def takeCommand():
    r=sr.Recognizer()   
    with sr.Microphone() as source:
       print("Listening....")
       speak("Listening")
 
       r.pause_threshold=1
       audio=r.listen(source,0,5)
   
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')   # Speech recognition API of google
        print(f"User: {query}\n")
       
    
    except Exception as e:
        print(e)
        speak("Please say that again")
        query="none"

    return query 

# OFFLINE activities

path={'notepad':"C:\\Windows\\System32\\notepad.exe", 
      'calculator':"C:\\Windows\\System32\\calc.exe",
     }


def open_file():
   os.startfile(path['notepad'])
   os.startfile(path['calculator'])

def open_cmd():
   os.system('start cmd')

def camera():
   sp.run('start microsoft.windows.camera:', shell=True)

from hugchat import hugchat
def chatbot(query):
   input=query.lower()
   chatbot=hugchat.ChatBot(cookie_path="cookies.json")
   id=chatbot.new_conversation()
   chatbot.change_conversation(id)
   response=chatbot.chat(input)
   speak(response)
   print(response)


# MAIN EXECUTION
def Main():
 while True:
    query=takeCommand().lower()
   
 
    print(query)
    if 'exit'in query or 'stop'in query:    # TERMINATION STATEMENT
       speak("Thank you")
       speak("Have a good day Jesly")
       exit()
       

    elif 'how are you' in query:
       speak("I am fine. Thank You")
   
    elif 'time' in query:
      time=datetime.now().strftime("%H:%M:%S")
      speak(time)
   
    elif 'wikipedia' in query:
       speak("Searching in wikipedia......")
       results=wikipedia.summary(query,sentences=1)
       speak("According to wikipedia ")
       speak(results)
   
   
   
    elif 'open youtube' in query:
       speak("opening youtube")
       webbrowser.open("youtube.com")
    
    elif 'open google' in query:
       speak("opening google")
       webbrowser.open("google.com")

    elif 'open wikipedia' in query:
       speak("opening wikipedia")
       webbrowser.open("wikipedia.com")


       # WHATSAPP
   
    elif 'whatsapp' in query:
        
        contacts={"mummy":"+1234567890","papa":"+1234567890"}
        
        speak("Who do you want to send message to ?")
        person=takeCommand().lower()
        
        
        speak("Please tell me the message")
        message=takeCommand().lower()
        
        hr=datetime.now().hour
        min=datetime.now().minute

        speak("Sending message")
        speak("Opening Whatsapp")
        
        kit(contacts[person],message)
      
#MUSIC
        
    elif 'music' in query:
       speak("Playing Music")
       musicPath='C:\\Users\\jesly\\OneDrive\\Documents\\Zira Virtual Voice Assistant\\web\\songs\\Song1.mpeg'
       os.startfile(musicPath)

   #OFFLINE TASKS 
    elif 'camera' in query:
       speak("Opening the camera")
       camera()
       
    elif 'terminal' in query:
       speak("Opening the terminal")
       open_cmd()

    elif 'open calculator' in query:
       os.startfile(path['calculator'])

       
    
   #Shut Down
    elif 'shut down' in query:
       os.system("shutdown /s /t /1")

   #Hugging Face to generate content 
    elif 'ai' in query:
       speak("I am genearting Results please wait")
       chatbot(query)
       



 
@eel.expose  # Expose the function to be callable from JavaScript
def Wish():
 return wish()  # Call the Main function


@eel.expose  # Expose the function to be callable from JavaScript
def startMain():
   return Main()  # Call the Main function


eel.start("index.html")
        

   
