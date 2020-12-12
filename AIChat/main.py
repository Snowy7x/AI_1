import speech_recognition as sr
import pyttsx3
from responses import *
from GUI import *

voiceId = 3
listenLang = 'en-US'
ara = False
r = sr.Recognizer()

# setting up the chatty bot
name = set_bot("Snowy")
chatBot = get_bot()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 10)
# default english
engine.setProperty('voice', voices[voiceId].id)

app = APP(" - Snowy-AI", "#3C3C3C", "600x300", False)


def say(message):
    print("speaking....")
    app.add_bot_line(message)
    print(message)
    engine.say('{}'.format(message))
    engine.runAndWait()


def listen():
    print("listening...")
    talk = "Could not get that. sorry!"
    try:
        with sr.Microphone() as source:  # use the default microphone as the audio source
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=60,
                             timeout=5)  # listen for the first phrase and extract it into audio data
        talk = r.recognize_google(audio, language=listenLang)  # recognize speech using Google Speech Recognition
        print("Raw->:" + talk)
        if ara:
            lang = translator.detect(talk)
            print(f"Language: {lang}")
            talk = translator.translate(talk, lang_tgt="en", lang_src="ar")
            print(f"eng: {talk}")
    except sr.UnknownValueError:  # speech is unintelligible
        if ara is False:
            say("Sorry!!, Couldn't understand you, Please try again!.")
        else:
            say("المعذرة، لم استطع فهم ذلك.")
        talk = listen()
    print("generating answer...")
    app.add_user_line(talk)
    return talk


def launch():

    global ara
    print("Launched!")
    while True:
        say("Hi Islam,")
        say("Do you want to use Arabic?")
        answer = listen().lower()

        if "yes" in answer or "ok" in answer or "yup" in answer or "y" in answer or "i want to" in answer or "i would like" in answer:
            print("changing the language....")
            ara = True
            listenLang = "ar-QA"
            set_language(listenLang)
            voiceId = 2
            engine.setProperty('voice', voices[voiceId].id)
            print("done")
            break
        elif "no" in answer or "nope" in answer or "nah" in answer or "n" in answer or "i do not" in answer:
            break

    welcome = "Welcome back Islam!"
    if ara:
        welcome = "مَرْحباً بِعودتكَ اِسلامْ"
    say(welcome)

    WAKE_STRS = ["hi snowy", "hay snowy", "hey snowy", "are you there", "snowy"]
    PERSON_STRS = ["who"]

    while True:
        # _input = str(input()).lower()
        _input = listen()
        print(f"YOU: {_input}")

        answer = 'I did not get you, ty another question!'
        unknown = 'I did not get you, ty another question!'
        fail = f"Could not find information about {_input}"
        for phrase in WAKE_STRS:
            if _input.count(phrase) > 0:
                say("I am here!")
                _input = listen()
                if _input is None:
                    continue

                if "close" in _input or "quit" in _input or "bye" in _input or "goodbye" in _input:
                    # Goodbye
                    respond = get_response(info="Goodbye", ara=ara)
                    if ara:
                        respond = translator.translate(f"{respond}", lang_tgt="ar")
                    print(f"{name}: {respond}")
                    get_bot().save()
                    break

                if "من هو" in _input or "who" in _input and answer == unknown:
                    answer = get_person(_input)

                if "تاريخ اليوم" in _input or "date" in _input and answer == unknown:
                    answer = get_date()

                if "what" in _input and answer == unknown:
                    answer = wiki_search(_input)
                    if answer == fail:
                        answer = wiki_search(_input.replace("what ", "").replace("is ", ""))

                if "open" in _input and answer == unknown:
                    if "browser" in _input:
                        answer = "Opening..."
                        if "search" in _input:
                            words = _input.split()
                            # clearing search quary:
                            for i in range(len(words)):
                                if words[0] == "search":
                                    if words[1] == "for":
                                        words.pop(1)
                                    words.pop(0)
                                    break
                                else:
                                    words.pop(0)
                            # opening the browser and searching
                            browser_search(' '.join(words[0] for i in words))
                        else:
                            browser_search('')

                if "search" in _input and answer == unknown:
                    if "browser" in _input:
                        answer = "Opening..."
                        words = _input.split()
                        # clearing search quary:
                        while "browser" in words or "search" in words:
                            words.pop(0)
                        if words[0] == "for":
                            words.pop(0)
                        # opening the browser and searching
                        browser_search(' '.join(words[0] for i in words))
                    else:
                        answer = wiki_search(_input.replace("search ", ''))

                if answer == unknown:
                    print("You: " + _input)
                    respond = get_response(info=_input, ara=ara)
                    if ara:
                        respond = translator.translate(f"{respond}", lang_tgt="ar")
                    print(f"{name}: {respond}")
                    say(respond)
                    continue
                print(f"{str(name).upper()}: {str(answer)}")
                say(answer)

    # chatBot.trainer.export_for_training('./bot_data.json')
    get_bot().save()

app.set_launch(launch)
app.window.mainloop()