import speech_recognition as sr
import pyttsx3
import openai

engine = pyttsx3.init()

openai.api_key = "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"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(f"Speaking: {text}")

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Comando reconhecido: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Não entendi o comando")
        return ""
    except sr.RequestError:
        speak("Falha ao conectar ao serviço de reconhecimento de voz")
        return ""

def ask_gpt(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Supondo que este é o modelo atualizado
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": question}]
        )
        answer = response.choices[0].message['content']
        speak(answer)
    except Exception as e:
        print(f"Erro ao acessar o GPT-3.5: {e}")
        speak("Houve um problema ao acessar o GPT-3.5.")


active = False
while True:
    command = listen_command()
    if "ok sexta-feira" in command:
        active = True
        speak("Sim, mestre.")
    elif active:
        if "pergunta" in command:
            speak("Qual é a sua pergunta?")
            question = listen_command()
            if question:
                ask_gpt(question)
        active = False
    else:
        if command:
            speak("Por favor, ative o sistema com 'Ok sexta-feira'")


# Codigo para execucao do GPT4.0

# import speech_recognition as sr
# import pyttsx3
# import openai
#
#
# engine = pyttsx3.init()
#
#
# openai.api_key = "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"
#
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#     print(f"Speaking: {text}")
#
# def listen_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Aguardando comando...")
#         audio = recognizer.listen(source)
#     try:
#         command = recognizer.recognize_google(audio, language='pt-BR')
#         print(f"Comando reconhecido: {command}")
#         return command.lower()
#     except sr.UnknownValueError:
#         speak("Não entendi o comando")
#         return ""
#     except sr.RequestError:
#         speak("Falha ao conectar ao serviço de reconhecimento de voz")
#         return ""
#
# def ask_gpt(question):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[{"role": "system", "content": "You are a helpful assistant."},
#                       {"role": "user", "content": question}]
#         )
#         answer = response.choices[0].message['content']
#         speak(answer)
#     except Exception as e:
#         print(f"Erro ao acessar o GPT-4: {e}")
#         speak("Houve um problema ao acessar o GPT-4.")
#
# # Loop principal
# active = False
# while True:
#     command = listen_command()
#     if "ok sexta-feira" in command:
#         active = True
#         speak("Sim, mestre. O que posso fazer?")
#     elif active:
#         if "fazer uma pergunta" in command:
#             speak("Qual é a sua pergunta?")
#             question = listen_command()
#             if question:
#                 ask_gpt(question)
#         active = False  # Desativa após executar um comando
#     else:
#         if command:
#             speak("Por favor, ative o sistema com 'Ok sexta-feira'")
