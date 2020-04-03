import pyttsx3          #library which use to listen from mic what user is saying and also use to speak
import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import Trainner as tr
from tkinter import *
from PIL import Image,ImageTk
import cv2
import Movement as m
import Hand as h
import Input as in1
import Emails as em
#from tkinter import ttk
from pygame import mixer
from tkinter import messagebox



engine = pyttsx3.init('sapi5')  #The Speech Application Programming Interface or SAPI is an API developed by Microsoft to allow the use of speech recognition and speech synthesis within Windows applications

voices = engine.getProperty('voices')
print(engine)
engine.setProperty('voice', voices[0].id)  #here we are seting voice

root = Tk()
root.title("System X")
root.geometry("1380x740")

'''root1 = Toplevel()
root1.title('Universal Search Bar')
root1.iconbitmap('C:\\Users\\User\\PycharmProjects\\SystemX\\mic.ico')
style = ttk.Style()
style.theme_use('winnative')

photo1 = PhotoImage(file='C:\\Users\\User\\PycharmProjects\\SystemX\\microphone.png').subsample(15, 15)

label1 = ttk.Label(root1, text='Query:')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(root1, width=40)
entry1.grid(row=0, column=1, columnspan=4)'''


def greetings():
    xd = tr.TakeId()

    if xd==0:
        exit()
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        speak(f"Good morning")
    elif hr >=12 and hr <18:
        speak(f"Good Afternoon")
    else:
        speak(f"Good evening")
    speak("SystemX is activated")
    speak("How can I help you ?")


def command():
    mixer.init()
    messagebox.showinfo("Command","Press button and give command")
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.energy_threshold = 400


    with sr.Microphone() as source:
        print("I'm Listening")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            print("Recognizing..")
            q = str(r.recognize_google(audio, language='en-in'))
            print(f"User Said:: {q}\n")

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')
            return "None"

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')
            return "None"
    return q


'''def Search():
    greetings()
    MyButton1 = ttk.Button(root1, text='Search', width=10, command=command)
    MyButton1.grid(row=0, column=6)

    MyButton6 = Button(root1, image=photo1, command=command, bd=0, activebackground='#c1bfbf', overrelief='groove',relief='sunken')
    MyButton6.grid(row=0, column=5)
    print(MyButton6)

    entry1.focus()
    root1.wm_attributes('-topmost', 1)

    root1.mainloop()
    return q'''


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def hand():
    x = h.HandCommand()
    if x==1:
        speak("Who are you?")
    elif x==2:
        speak("Can you get me some water?")
    elif x==3:
        speak("Hello I am DarkArt")
    elif x==4:
        speak("I lived in Nashik")
    elif x==5:
        speak("Can you call on this number")


def main():

    root.destroy()
    greetings()
    while True:
        qu = command().lower()
        print(qu)

        if 'wikipedia' in qu:
            speak('Searching..')
            qu = qu.replace('wikipedia', "")
            result = wikipedia.summary(qu, sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)

        elif 'x open youtube' in qu:
            #webbrowser.get("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe").open_new("https://www.youtube.com/")
            speak('opening youtube')
            webbrowser.open("http://youtube.com/")

        elif 'x open fb' in qu:
            speak('opening facebook')
            webbrowser.open("http://facebook.com/")

        elif 'x open google hello' in qu:
            speak('opening google')
            webbrowser.open("http://google.com/hello")

        elif 'x play music' in qu:
            speak('playing music.')

            music = 'E:\\music'             #Directory where songs are stored
            songs = os.listdir(music)       #listing or taking length of songs in that directory
            #len1 = len(songs)
            #c = random.randint(0, len1)     #generating random no.
            os.startfile(os.path.join(music, songs[1]))     #Starting time

        elif 'x play video' in qu:
            speak('playing video.')
            vid_dir = 'E:\\video'
            vid = os.listdir(vid_dir)
            len2 = len(vid)
            x = random.randint(0, len2)
            os.startfile(os.path.join(vid_dir, vid[1]))


        elif 'x tell me time' in qu:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, time is {strTime}")

        elif 'terminate x' in qu:
            speak('shutting down system X.')
            exit()

        elif 'x open steam' in qu:
            speak('opening..')
            p = 'F:\\Steam\\Steam.exe'
            os.startfile(p)

        elif 'x open c3' in qu:
            speak('opening Crysis 3. shut down system x otherwise fps will drop.')
            p = 'E:\\game\\Crysis 3\\Bin32\\Crysis3.exe'
            os.startfile(p)

        elif 'x open notepad' in qu:
            speak('opening notepad')
            p = 'C:\\WINDOWS\\system32\\notepad.exe'
            os.startfile(p)

        elif 'x open spotify' in qu:
            speak('opening spotify')
            p = 'C:\\Users\\User\\AppData\\Roaming\\Spotify\\Spotify.exe'
            os.startfile(p)

        elif 'start' in qu:
            speak('Starting Stealth Mode. Taking initial frame')
            cv2.waitKey(1000)
            m.Move()

        elif 'x hand mode' in qu:
            speak("Initiating Hand Mode.")
            cv2.waitKey(100)
            hand()

        elif 'x new user' in qu:
            speak("Enter ID:.")
            cv2.waitKey(100)
            in1.InputX()

        elif 'x mail' in qu:
            speak("Stand by mode activated")
            em.read_email_from_gmail()
            '''while(1):
                t = threading.Timer(5.0, em.read_email_from_gmail())
                t.start()
                t.cancel()'''
            break




def Login():
    canvas = Canvas(root, width=1380, height=740)
    canvas.pack()

    im = Image.open("BG.jpg")
    photo = ImageTk.PhotoImage(im)
    bg = canvas.create_image(0, 0, anchor=NW, image=photo)


    user_label = Label(root, text="Username", font="Centaur 40 bold")
    us_label_window = canvas.create_window(690, 300, window=user_label)


    user_image = Image.open("user.png")
    photo2 = ImageTk.PhotoImage(user_image)
    user_icon = Button(root, image=photo2)
    user_icon_window = canvas.create_window(690, 220, window=user_icon)

    password = Label(root, text="Password:", font="Times 15")
    password_window = canvas.create_window(590, 360, window=password)
    passvalue = StringVar()
    passentry = Entry(root, textvariable = passvalue)
    passinput_window = canvas.create_window(710, 360, window=passentry)

    login = Button(root, text="Login", font="Times 15")
    login_window = canvas.create_window(650, 400, window=login)
    facelogin = Button(root, text="Face Login", font="Times 15", command=main)
    facelogin_window = canvas.create_window(750, 400, window=facelogin)

    forgot_label = Button(root, text="Forgot Password?", fg='red', font="Times 10")
    forgot_window = canvas.create_window(700, 440, window=forgot_label)


    shut_image = Image.open("shutdown.png")
    photo1 = ImageTk.PhotoImage(shut_image)
    shutdown = Button(root, image=photo1)
    shutdown_window = canvas.create_window(1300, 680, window=shutdown)

    root.mainloop()


Login()