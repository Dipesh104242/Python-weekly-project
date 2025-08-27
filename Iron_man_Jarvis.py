#this Programme is not complete properly. its need to improve so take care of you all step on this code 

# Modules import
import os 
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) + 12
    
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sir I am Laura. Please tell me how may I help you.")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon! Sir I am Laura. Please tell me how may I help you.")
        
    else:
        speak("Good Evening! Sir I am Laura. Please tell me how may I help you.")
        
def takeCommend():
    """
    It takes microphone input from the users and return string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while 1:
        query  = takeCommend().lower()

        #Logics for executing task for based on querys
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open gmail" in query:
            webbrowser.open("gmail.com")
        elif "open github" in query:
            webbrowser.open("github.com")
        elif 'open blog' in query:
            webbrowser.open("blogger.com")
        
        elif 'play music' in query:

            music_dir = r"C:\Users\pc\Music"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codepath = r"C:\Users\pc\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)

        # elif 'email to dipesh' in query:
        #     try:
        #         speak("What should i say")
        #         content = takeCommend()
        #         to = 'dipeshkayal890@gmail.com'
        #         sendEmail(to,content)
        #         speak("Email has been sent!") 
        #     except Exception as e:
        #         print(e)
        #         print("Sorry  am not able to sent this email")       
