from translate import Translator
import pyttsx3
import tkinter as tk
from tkinter import messagebox


def traduzir_e_falar():
    try:
      
        idioma_1 = idioma_origem.get()
        idioma_2 = idioma_destino.get()
        
     
        if idioma_1 == idioma_2:
            messagebox.showerror("Erro", "Os idiomas de origem e destino não podem ser iguais.")
            return
        
       
        tradutor = Translator(from_lang=idiomas[idioma_1], to_lang=idiomas[idioma_2])

       
        frase = tradutor.translate(entry_frase.get())

      
        robo.say(frase)
        robo.runAndWait()

       
        label_resultado.config(text=frase)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


robo = pyttsx3.init()
voices = robo.getProperty('voices')
robo.setProperty('voice', voices[1].id)  


idiomas = ['pt-br', 'en-us', 'de']
idiomas_nome = ['Português', 'Inglês', 'Alemão']


janela = tk.Tk()
janela.title("Tradutor com Leitura")


label_origem = tk.Label(janela, text="Idioma de Origem:")
label_origem.grid(row=0, column=0, padx=10, pady=10)

idioma_origem = tk.IntVar()
idioma_origem.set(0) 
menu_origem = tk.OptionMenu(janela, idioma_origem, 0, 1, 2)
menu_origem.grid(row=0, column=1)

label_destino = tk.Label(janela, text="Idioma de Destino:")
label_destino.grid(row=1, column=0, padx=10, pady=10)

idioma_destino = tk.IntVar()
idioma_destino.set(1)  
menu_destino = tk.OptionMenu(janela, idioma_destino, 0, 1, 2)
menu_destino.grid(row=1, column=1)

label_frase = tk.Label(janela, text="Digite a frase a ser traduzida:")
label_frase.grid(row=2, column=0, padx=10, pady=10)

entry_frase = tk.Entry(janela, width=40)
entry_frase.grid(row=2, column=1)


botao_traduzir = tk.Button(janela, text="Traduzir e Falar", command=traduzir_e_falar)
botao_traduzir.grid(row=3, column=0, columnspan=2, pady=20)


label_resultado = tk.Label(janela, text="", wraplength=400)
label_resultado.grid(row=4, column=0, columnspan=2)


janela.mainloop()
