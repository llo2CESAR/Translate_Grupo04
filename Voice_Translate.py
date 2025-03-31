# importar as bibliotecas

from translate import Translator 
import pyttsx3 



#iniciar o pyttsx3

robo = pyttsx3.init()

voices = robo.getProperty('voices')

robo.setProperty('voice',voices[1].id)



#criar a nossa lista de idiomas

idiomas = ['pt-br', 'en-us', 'de']



#criar um menu com os idiomas suportados

print('Lista de idiomas suportados: ')

print('-='* 30)

print('''1-Português 2-Inglês 3-Alemão''')

print('-=' * 30)



#Escolher o idioma a ser traduzido

idioma_1 = int(input('Digite o número correspondente ao idioma a ser traduzido: '))-1

print('-='*30)

while idioma_1 not in [1, 2, 3]:

    print('Digite um valor válido')

    print('-=' *30)

    idiona_1 = int(input('Digite o número correspondente ao idioma a ser traduzido: '))-1 #mesma frase do input

idioma_2 = int(input('Digite o número correspondente ao idioma a ser traduzido: '))-1

print('-='*30)



#criar o tradutor



tradutor = Translator(from_lang=idiomas[idioma_1],to_lang=idiomas[idioma_2])



#pegar a frase e traduzir ela

frase = tradutor.translate(input('Digite a frase a ser traduzida: '))



robo.say(frase)

print(frase)

robo.runAndWait()

robo.stop()