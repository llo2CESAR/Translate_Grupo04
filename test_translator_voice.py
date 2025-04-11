from tkinter import *
import tkinter as tk
from tkinter import ttk, Button
from googletrans import Translator
from tkinter import messagebox
import pyttsx3
from PIL import Image, ImageTk



# Dicionário de idiomas com códigos corretos
LANGUAGES = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',
    'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be',
    'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr',
    'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
    'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi',
    'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
    'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi',
    'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig',
    'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
    'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km',
    'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo',
    'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml',
    'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
    'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
    'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
    'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
    'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
    'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk',
    'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
    'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
    'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk',
    'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
    'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
}

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

framel = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#FF6002')
framel.place(x=0, y=0)

Label(root, text="Language Translator", font=("Roboto", 20, "bold"), fg="white", bg='#FF6002').pack(pady=10)

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get().lower()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the text to translate!')
    else:
        try:
            translator = Translator()
            print(f"Traduzindo '{lang_1}' para '{cl}'") 
            output = translator.translate(lang_1, dest=cl)
            text_entry2.delete(1.0, 'end')
            text_entry2.insert('end', output.text)
            print(f"Resultado: {output.text}")  
        except Exception as e:
            messagebox.showerror("Erro de Tradução", str(e))

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

def audio():
    engine = pyttsx3.init()
    texto_traduzido = text_entry2.get("1.0", "end-1c")
    if not texto_traduzido:
        messagebox.showerror("Language Translator", "Enter the text to translate")
    else:
        engine.say(texto_traduzido)
        engine.runAndWait()

# Combobox para seleção automática (não usado, mas mantido)
a = tk.StringVar()
auto_select = ttk.Combobox(framel, width=27, textvariable=a, state='readonly', font=('verdana', 10, 'bold'))
auto_select['values'] = ('Auto select',)
auto_select.place(x=40, y=60)
auto_select.current(0)

# Combobox com idiomas (exibindo nomes)
l = tk.StringVar()
choose_language = ttk.Combobox(framel, width=27, textvariable=l, state='readonly', font=('verdana', 10, 'bold'))
choose_language['values'] = list(LANGUAGES.keys())
choose_language.place(x=305, y=60)
choose_language.current(0)

# Áreas de texto
text_entry1 = Text(framel, width=20, height=7, borderwidth=5, relief=SOLID, font=('verdana', 15))
text_entry1.place(x=40, y=100)

text_entry2 = Text(framel, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

# Botões
btn1 = Button(framel, command=translate, text="Translate", relief=FLAT, borderwidth=2,
              font=('verdana', 10, 'bold'), bg='#248aa2', cursor="hand2")
btn1.place(x=185, y=300)

btn2 = Button(framel, command=clear, text=" Clear  ", relief=FLAT, borderwidth=2,
              font=('verdana', 10, 'bold'), bg='#248aa2', anchor="center")
btn2.place(x=300, y=300)

# Imagem de áudio
pil_image = Image.open("audio2.png")
pil_image = pil_image.resize((20, 20))
tk_image = ImageTk.PhotoImage(pil_image)

# Botão com imagem de áudio
btn3 = Button(root, image=tk_image, relief=FLAT, borderwidth=0, highlightthickness=0, cursor="hand2",
              padx=0, pady=0, bd=0, bg='#FF6002', activebackground='#FF6002', command=audio)
btn3.image = tk_image
btn3.place(x=390, y=305)

translator = Translator()
result = translator.translate("porta", src="pt", dest="en")

print(result.text)

root.mainloop()
