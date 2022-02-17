import pyttsx3 
# not import to import pyttsx3 if you are not making any A.I or need any computer voice. You will use your recorded voice here

import speech_recognition as sr
# for speech recognition
import pyautogui as pg
# for automating the tasks . 
import time
# creating a lag in the code to make it work finer . not to be super quick. .

# setting the engine to speak .
engine = pyttsx3.init("sapi5")
# sapi5 for the windows . nsss for mac os and espeak for linux and other 
voices = engine.getProperty("voices")
engine.setProperty("voices" , voices[0].id)

# if you are using your own recorded voice , don't use this . just comment out the above block of code.
    

# the points to be clicked . 
play_x , play_y = (700 , 365) # the coordinate points of the play button of your recorded voice . 
on_mic_x , on_mic_y =  (1907 , 725) # the coordinate points of the mic on and off button of the google meet. 
# to get the coordinates of your play button and meet mic use this code to get it . 

"""
import pyautogui as pg
imoprt time

time.sleep(3)
print(pg.position())

"""
# after runnig this file , immediately bring your cursor to the point whose position you want to get . 

def speak(audio) : 
    engine.say(audio)
    engine.runAndWait()
    # for speaking the audio . engine sapi5 used for windows . 
    # again this is not required if you are using your recorded voice , 

def ListenCommand() : 
    # for listening the audio. 
    r = sr.Recognizer()

    with sr.Microphone() as source: 
        print("! Listening ...")
        r.adjust_for_ambient_noise(source , duration = 0.5)
        r.pause_threshold =  0.5 # the amount of pause second after which the sentence is considered complete . 
        r.energy_threshold = 1000 # if you have lot of background noise , or you need to scream to make it listen , just increase this. 
        # for very calm and good enironment , use 300 and then according to you , increase it was wanted .
        audio = r.listen(source)
    try: 
        print("Recognizing....")
        query = r.recognize_google(audio , language = "en-in"  )
        # google speech recognition . language set to india .
        query = query.lower()
        print()
        print("The query was ->  {}\n".format(query))
        # the query . 
            
    except Exception as e : 
        print(e)
        return "I did't get , please say that again !"
    return query


# the special speeches to be considered to make your recorded file run 
# the speeches which need to be recognised to say yes sir . 
speeches = ['bolo han ya na', 'polo ha ya na', 'beta samajh mein aaya', 'samajh mein aaya', 'bolo na ', 'samajh mein aaya kya', 'bolo na', 'samajh mein aaya beta' ,'theek hai' ,'clear hai sabko' ,'show ho raha hai' ,'kuch doubt' ,'han ya na' ,'clear hua' ,'beta bolo han ya na' ,'clear hai' ,'samajh rahe ho' ,'clear a seiko' ,'clear mein sabko']


# this function takes a query , the speech which was said , it then checks whether the query has the speech which need to be considered and to be responded. 
def checkAsking(query) :
    for i in speeches :
        if i in query : 
            return True 
    return False
# if the query is found it returns True else False .  


# if the query is found then this function runs the commands to make the voice work . 
def runSpeaking():
    print("Sir asked for understanding... ")
    # this is the ultimate program , which will will run your files and run the recorded file. 
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
    
