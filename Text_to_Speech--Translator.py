from tkinter import *
from tkinter import messagebox
import os
from gtts import gTTS
import speech_recognition
import playsound
from tkinter import ttk
from googletrans import Translator
################################################
# 
language = ["ru","de","en","no","fr","it",'af', 'ar', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo', 'es', 'et', 'fi', 'fr', 'gu', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jw', 'km', 'kn', 'ko', 'la', 'lv', 'mk', 'ml', 'mr', 'my', 'ne', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'si', 'sk', 'sq', 'sr', 'su', 'sv', 'sw', 'ta', 'te', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'zh-CN']
# 
trans = Translator()
# 
window = Tk()
#################################################
#
#
def main():
    gts = gTTS(text = text1.get('1.0',END),lang=box_value.get())
    if os.path.exists("/home/ulutan/Schreibtisch/Translator/conv.mp3"):
        os.remove("/home/ulutan/Schreibtisch/Translator/conv.mp3")
    filename = "/home/ulutan/Schreibtisch/Translator/conv.mp3"
    gts.save(filename)
    playsound.playsound(filename)
#
def trs():
    translated = trans.translate(text1.get('1.0',END),dest=box_value.get())
    text1.delete('1.0',END)
    text1.insert('1.0',translated.text)
#
#
##################################################
window.config(bg="gray20")
#
window.title("IHarryTranslator")
#
frame = Frame(window,bg="gray20")
#
label1 = Label(frame, text="by IHx0",bg="gray20",font="arial 12 bold")
#
label2 = Label(frame, text="Text to Speech", bg = "gray20",font="arial 12 bold")
#
text1 = Text(frame,height =4, width=50,bg="gray20")
#
box_value = StringVar()
cm = ttk.Combobox(frame,value=language,width=10,textvariable=box_value)
#
cm.pack(anchor=E)
label1.pack(anchor=W)
label2.pack(anchor=E)
text1.pack(anchor=W)
frame.pack(fill="both",expand=1)
################################################
uframe = Frame(window,bg="gray20")
#
button1 = Button(uframe,text="Cancel",bg="gray20",font="arial 10 bold")
#
button2 = Button(uframe, text="Convert", bg="gray20",font="arial 10 bold",command=main)
#
button3 = Button(uframe, text="Translate", bg="gray20",font="arial 10 bold",command=trs)
#
button1.pack(side=LEFT)
#
button2.pack(side=LEFT)
#
button3.pack(side=LEFT)
#
uframe.pack(anchor=E)
#
#
#
#End
#
window.mainloop()
