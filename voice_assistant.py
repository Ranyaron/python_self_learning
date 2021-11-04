from gtts import gTTS
from random import randint
from playsound import playsound
import speech_recognition as sr


def listen():
    # return input("Go: ")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду: ")
        audio = r.listen(source)

    try:
        speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: ", speech)
        return speech
    except sr.UnknownValueError:
        return "Error!"
    except sr.RequestError:
        return "Error!"


def say(text):
    voice = gTTS(text, lang="ru")
    unique_file_name = "audio_" + str(randint(0, 1000000)) + ".mp3"
    voice.save(unique_file_name)
    playsound(unique_file_name)
    print("Ассистент:", text)


def handle_message(message):
    message = message.lower()
    if "привет" in message:
        say("йоу")
    elif "пока" in message:
        finish()
    else:
        say("Я такой команды не знаю")


def finish():
    say("пока")
    exit()


if __name__ == "__main__":
    print("test")

    while True:
        command = listen()
        handle_message(command)
