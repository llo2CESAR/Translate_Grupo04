from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6f')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#F7DC6F').pack(pady=10)

from deep_translator import GoogleTranslator
def translate():
    lang1 = text_entry1.get('1.0', 'end-1c')
    cl = choose_language.get()

    if lang1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = GoogleTranslator(source="auto", target=cl)
        output = translator.translate(lang1)
        text_entry2.insert('end', output)
def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a = tk.StringVar()

auto_select = ttk.Combobox(framel, width=27, textvariable=a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto select',
                        )
auto_select.place(x=15, y=60)
auto_select.current(0)

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

text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(framel, command=translate, text="Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg="white", cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(framel, command=clear, text="Clear", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2')
btn2.place(x=300, y=300)


root.mainloop()


