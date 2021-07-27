# importing required module

import webbrowser
import speech_recognition as spr
from pygame import mixer
from tkinter import *
from tkinter import ttk
from google_trans_new import google_translator
from gtts import gTTS
from tkinter import messagebox
import os

# Made a list of Supported language
# Used Only 9 languages out of 107
# To Present
langs = ["en", "hi", "bn", "ar", "gu", "it", "la", "ml", "mr"]
spt = Tk()

spt.resizable()

evar1 = StringVar()
evar2 = StringVar()
msgvar = StringVar()


txt1 = StringVar()
txt2 = StringVar()

# styling the frame which helps to
# make our background stylish

frame1 = Frame(spt, bg="lightPink", height="150")

# place the widget in gui window

frame1.pack(fill=X)

frame2 = Frame(spt, bg="lightgreen", height="750")

frame2.pack(fill=X)

# styling the label which show the text
# in our tkinter window

from_l = Label(frame1, text="From_Language", font="bold, 10", bg="lightpink")

from_l.place(x=80, y=10)

To_l = Label(frame1, text="To_Language", font="bold, 10", bg="lightpink")
To_l.place(x=80, y=70)

supp_msg = Message(frame2, textvariable=msgvar, font="bold, 10", bg="lightgreen")
supp_msg.place(x=0, y=190)

spo_wrd = Label(frame2, text="Spoked Sentence", font="bold, 10", bg="lightgreen")
spo_wrd.place(x=80, y=5)

trns_wrd = Label(frame2, text="Translated", font="bold, 10", bg="lightgreen")
trns_wrd.place(x=80, y=90)

msgvar.set(
    "Supported Languages:(Only Use The Short Forms As Input ) \n\n English = 'en' \n Hindi='hi' \n Bengali='bn' \n Arabic = 'ar' \n Gujarati = 'gu'  \n Italian = 'it' \n Latin = 'la' \n Malayalam = 'ml' \n Marathi = 'mr'")

c_from = ttk.Combobox(textvariable=txt1, values=langs)
c_from.set(value='en')
c_from.place(x=250, y=10)

c_to = ttk.Combobox(textvariable=txt2, values=langs)
c_to.set(value='hi')
c_to.place(x=250, y=70)

spo_ent = Entry(frame2, textvariable=evar2, width=25, bd=4, font=14)
spo_ent.place(x=250, y=10)

trans_ent = Entry(frame2, textvariable=evar1, width=25, bd=4, font=14)
trans_ent.place(x=250, y=80)

spo_ent.insert(0, "")


# define a function which can
# get text and convert into audio
def speak():


    spo_ent.delete(0, END)
    # Creating Recogniser() class object
    recog1 = spr.Recognizer()

    # Creating microphone instance
    mc = spr.Microphone()

    # Capture Voice
    with mc as source:
        init_msg = "Speak 'hello' to initiate the Translation !"
        messagebox.showinfo("Speech Simulation", init_msg)

        recog1.adjust_for_ambient_noise(source, duration=0.2)
        audio = recog1.listen(source)
        MyText = recog1.recognize_google(audio)
        MyText = MyText.lower()

    # Here initialising the recorder with
    # hello, whatever after that hello it
    # will recognise it.
    if 'hello' in MyText:
        with mc as source:
            sp = "Speak a stentence.."
            messagebox.showinfo("Hello Detected", sp)
            recog1.adjust_for_ambient_noise(source, duration=0.2)

            # Storing the speech into audio variable
            audio = recog1.listen(source)

            # Using recognize.google() method to
            # convert audio into text

            get_s = recog1.recognize_google(audio)



            messagebox.showinfo("Detected Speech", get_s)
            spo_ent.insert(0, get_s)


def translate():
    trans_ent.delete(0, END)

    translator = google_translator()

    # short form of english in which
    # you will speak
    from_lang = c_from.get()

    # In which we want to convert, short
    # form of hindi
    to_lang = c_to.get()

    get_sentence = evar2.get()

    text_to_translate = translator.translate(get_sentence, lang_src=from_lang, lang_tgt=to_lang)

    # trns_wrd.config(text=text_to_translate,)
    # trns_wrd.place( x=80, y=90)
    trans_ent.insert(0, text_to_translate)
    # Storing the translated text into text variable
    # To be used by gTTs()
    text = text_to_translate

    # Using Google-Text-to-Speech ie, gTTS() method
    # to speak the translated text into the
    # destination language which is stored in to_lang.
    # Also, we have given 3rd argument as False because
    # by default it speaks very slowly
    speak = gTTS(text=text, lang=to_lang, slow=False)

    # Using save() method to save the translated
    # speech in capture_voice.mp3
    speak.save("translated.mp3")


def play():
    # Using OS module to run the translated voice.
    os.system("start translated.mp3")


def search_eng():
    root = Tk()
    root.title('Speech Search Bar')

    label1 = ttk.Label(root, text='Query:')
    label1.grid(row=0, column=0)
    entry1 = ttk.Entry(root, width=40)
    entry1.grid(row=0, column=1, columnspan=4)

    btn2 = StringVar()

    def callback():
        if btn2.get() == 'google' and entry1.get() != '':
            webbrowser.open('http://google.com/search?q=' + entry1.get())

        elif btn2.get() == 'duck' and entry1.get() != '':
            webbrowser.open('http://flipkart.com/?q=' + entry1.get())

        elif btn2.get() == 'amz' and entry1.get() != '':
            webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry1.get())

        elif btn2.get() == 'ytb' and entry1.get() != '':
            webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())

        else:
            pass

    def get(event):
        if btn2.get() == 'google' and entry1.get() != '':
            webbrowser.open('http://google.com/search?q=' + entry1.get())

        elif btn2.get() == 'Flpk' and entry1.get() != '':
            webbrowser.open('http://Flipkart.com/?q=' + entry1.get())

        elif btn2.get() == 'amz' and entry1.get() != '':
            webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry1.get())

        elif btn2.get() == 'ytb' and entry1.get() != '':
            webbrowser.open('https://www.youtube.com/results?search_query=' + entry1.get())

        else:
            pass

    def buttonClick():

        mixer.init()
        mixer.music.load('chime1.mp3')
        mixer.music.play()

        r = spr.Recognizer()
        r.pause_threshold = 0.7
        r.energy_threshold = 400

        with spr.Microphone() as source:

            try:

                audio = r.listen(source, timeout=5)
                message = str(r.recognize_google(audio))

                mixer.music.load('chime2.mp3')
                mixer.music.play()

                entry1.delete(0, END)
                entry1.insert(0, message)

                if btn2.get() == 'google':
                    webbrowser.open('http://google.com/search?q=' + message)

                elif btn2.get() == 'Flpk':
                    webbrowser.open('http://flipkart.com/?q=' + message)

                elif btn2.get() == 'amz':
                    webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + message)

                elif btn2.get() == 'ytb':
                    webbrowser.open('https://www.youtube.com/results?search_query=' + message)

                else:
                    pass

            except spr.UnknownValueError:
                print('Google Speech Recognition could not understand audio')

            except spr.RequestError as e:
                print('Could not request results from Google Speech Recognition Service')

            else:
                pass

    entry1.bind('<Return>', get)

    MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
    MyButton1.grid(row=0, column=6)

    MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
    MyButton2.grid(row=1, column=1, sticky=W)

    MyButton3 = ttk.Radiobutton(root, text='Flpk', value='duck', variable=btn2)
    MyButton3.grid(row=1, column=2, sticky=W)

    MyButton4 = ttk.Radiobutton(root, text='Amz', value='amz', variable=btn2)
    MyButton4.grid(row=1, column=3)

    MyButton5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=btn2)
    MyButton5.grid(row=1, column=4, sticky=E)

    MyButton6 = Button(root, text="Speak", command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove',
                       relief='sunken')
    MyButton6.grid(row=0, column=5)

    entry1.focus()
    root.wm_attributes('-topmost', 1)
    btn2.set('google')

# cereate a button which holds
# our play function using command = play

sp_btn = Button(frame2, text="Speak", width="15", pady=10, font="bold, 10", command=speak, bg='yellow')

sp_btn.place(x=250, y=130)

trns_btn = Button(frame2, text="Translate", width="15", pady=10, font="bold, 10", command=translate, bg="yellow")

trns_btn.place(x=100, y=130)

ply_btn = Button(frame2, text="Play", width="15", pady=10, font="bold, 10", command=play, bg="yellow")

ply_btn.place(x=400, y=130)

ser_btn = Button(frame2, text="Search Engine", width="15", pady=10, font="bold, 10", command=search_eng, bg="yellow")
ser_btn.place(x=500, y=350)

# give a title

spt.title("Speech Translator")

# we can not change the size
# if you want you can change

spt.geometry("650x550+350+200")
# start the gui
spt.mainloop()

