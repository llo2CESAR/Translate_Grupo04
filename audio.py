import speech_recognition as sr

def reconhecer_fala(mensagem):
    print(mensagem)
    reconhecedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando para o ruído ambiente... Por favor, aguarde.")
        reconhecedor.adjust_for_ambient_noise(source, duration=2)

        print("Gravando... Fale agora (você tem 15 segundos):")
        audio = reconhecedor.record(source, duration=15)  # grava por 15 segundos fixos

    try:
        frase = reconhecedor.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
        return frase
    except sr.UnknownValueError:
        print("Não entendi o que você quis dizer.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao se conectar ao serviço de reconhecimento de fala: {e}")
        return None

reconhecer_fala("Iniciando reconhecimento de voz...")
