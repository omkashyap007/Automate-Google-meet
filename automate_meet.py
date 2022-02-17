import os 
import pyttsx3 
import speech_recognition as sr
from playsound import playsound
import pyautogui as pg
import time

# setting the engine to speak .
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices" , voices[0].id)

# the points to be clicked . 
play_x , play_y = (700 , 365)
on_mic_x , on_mic_y =  (1907 , 725)

def speak(audio) : 
    engine.say(audio)
    engine.runAndWait()

def ListenCommand() : 
    r = sr.Recognizer()

    with sr.Microphone(1) as source: 
        print("! Listening ...")
        r.adjust_for_ambient_noise(source , duration = 0.5)
        r.pause_threshold =  0.5
        r.energy_threshold = 1200
        audio = r.listen(source)
    try: 
        print("Recognizing....")
        query = r.recognize_google(audio , language = "en-in"  ) 
        query = query.lower()
        print()
        print("The query was ->  {}\n".format(query))
            
    except Exception as e : 
        print(e)
        return "I did't get , please say that again !"
    return query



speeches = ['bolo han ya na', 'polo ha ya na', 'beta samajh mein aaya', 'samajh mein aaya', 'bolo na ', 'samajh mein aaya kya', 'bolo na', 'samajh mein aaya beta' ,'theek hai' ,'clear hai sabko' ,'show ho raha hai' ,'kuch doubt' ,'han ya na' ,'clear hua' ,'beta bolo han ya na' ,'clear hai' ,'samajh rahe ho' ,'clear a seiko' ,'clear mein sabko']

def checkAsking(query) :
    for i in speeches :
        if i in query : 
            return True 
    return False

def runSpeaking():
    print("Sir asked for understanding... ")
    pg.click(on_mic_x , on_mic_y)
    time.sleep(0.5)
    pg.click(play_x , play_y)
    time.sleep(2.5)
    pg.click(on_mic_x , on_mic_y)
    
def main() :    
    keep_listening = True
    while keep_listening :
        query = ListenCommand()
        if checkAsking(query) :
            runSpeaking()
        if query == "quit" : 
            keep_listening = False
 
if __name__ == "__main__" :
    main()
