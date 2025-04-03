from tkinter import *
import tkinter as tk
from tkinter import ttk, Button
from tkinter import messagebox
import pyttsx3
from PIL import Image, ImageTk
from deep_translator import GoogleTranslator

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#FF6002')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Roboto", 20, "bold"), fg="white", bg='#FF6002').pack(pady=10)

def audio():
    engine = pyttsx3.init()
    texto_traduzido = text_entry2.get("1.0", "end-1c")
    if not texto_traduzido:  # Se texto_traduzido for vazio
        print("Nenhum texto para reproduzir")
    else:
     engine.say(texto_traduzido)
     engine.runAndWait()

a = tk.StringVar()

auto_select = ttk.Combobox(framel, width=27, textvariable=a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto select',
                        )
auto_select.place(x=20, y=60)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='randomly', font=('verdana', 10, 'bold' ))

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = GoogleTranslator(source="auto", target=cl)
        output = translator.translate(lang_1)
        text_entry2.insert('end', output)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')




auto_select = ttk.Combobox(framel, width=27, textvariable=a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto select',
                        )
#auto_select.place(x=20, y=60)
#auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='randomly', font=('verdana', 10, 'bold' ))

choose_language['values'] = (
                                'afrikaans',
                                'albanian',
                                'amharic',
                                'arabic',
                                'armenian',
                                'azerbaijani',
                                'basque',
                                'belarusian',
                                'bengali',
                                'bosnian',
                                'bulgarian',
                                'catalan',
                                'cebuano',
                                'chichewa',
                                'chinese (simplified)',
                                'chinese (traditional)',
                                'corsican',
                                'croatian',
                                'czech',
                                'danish',
                                'dutch',
                                'english',
                                'esperanto',
                                'estonian',
                                'filipino',
                                'finnish',
                                'french',
                                'frisian',
                                'galician',
                                'georgian',
                                'german',
                                'greek',
                                'gujarati',
                                'haitian creole',
                                'hausa',
                                'hawaiian',
                                'hebrew',
                                'hebrew',
                                'hindi',
                                'hmong',
                                'hungarian',
                                'icelandic',
                                'igbo',
                                'indonesian',
                                'irish',
                                'italian',
                                'japanese',
                                'javanese',
                                'kannada',
                                'kazakh',
                                'khmer',
                                'korean',
                                'kurdish (kurmanji)',
                                'kyrgyz',
                                'lao',
                                'latin',
                                'latvian',
                                'lithuanian',
                                'luxembourgish',
                                'macedonian',
                                'malagasy',
                                'malay',
                                'malayalam',
                                'maltese',
                                'maori',
                                'marathi',
                                'mongolian',
                                'myanmar (burmese)',
                                'nepali',
                                'norwegian',
                                'odia',
                                'pashto',
                                'persian',
                                'polish',
                                'portuguese',
                                'punjabi',
                                'romanian',
                                'russian',
                                'samoan',
                                'scots gaelic',
                                'serbian',
                                'sesotho',
                                'shona',
                                'sindhi',
                                'sinhala',
                                'slovak',
                                'slovenian',
                                'somali',
                                'spanish',
                                'sundanese',
                                'swahili',
                                'swedish',
                                'tajik',
                                'tamil',
                                'telugu',
                                'thai',
                                'turkish',
                                'ukrainian',
                                'urdu',
                                'uyghur',
                                'uzbek',
                                'vietnamese',
                                'welsh',
                                'xhosa',
                                'yiddish',
                                'yoruba',
                                'zulu',
                            )

choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=SOLID, font=('verdana', 15))
text_entry1.place(x=20, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=SOLID, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(framel, command=translate, text="Translate", relief=FLAT, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', cursor="hand2")
btn1.place(x=185, y=300)



btn2 = Button(framel, command=clear, text=" Clear  ", relief=FLAT, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', anchor="center")
btn2.place(x=300, y=300)

pil_image = Image.open("audio2.png")  
pil_image = pil_image.resize((20, 20))   
tk_image = ImageTk.PhotoImage(pil_image) 


btn3 = Button(root, image=tk_image, relief=FLAT, borderwidth=0, highlightthickness=0, cursor="hand2", padx=0, pady=0, bd=0, command=audio)
btn3.image = tk_image  
btn3.pack()
btn3.place(x=390, y=310)


root.mainloop()
