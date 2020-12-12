import wikipedia
import datetime
import webbrowser
from chatBot import *
from google_trans_new import google_translator

language = "eng-US"
chatBot = None
translator = google_translator()


def get_bot():
    return Bot(chatBot)


def set_bot(name):
    global chatBot
    chatBot = Bot(name)
    return name


def set_language(lang):
    global language
    language = lang
    wikipedia.set_lang(lang)


def get_date():
    # Textual month, day and year
    date = datetime.date.today().strftime("%B %d, %Y")
    return f"Today is: {date}"


def get_person(info):
    result = f"Could not find information about {info}"
    try:
        result = wikipedia.summary(title=info, sentences=2)

    except:
        pass

    return result


def wiki_search(info):
    result = f"Could not find information about {info}"
    try:
        result = wikipedia.summary(title=info, sentences=2)

    except:
        pass

    return result


def browser_search(info):
    if info == '':
        webbrowser.open("https://www.google.com")
        return
    info = info.replace(" ", "+")
    webbrowser.open(f"https://www.google.com/search?q={info}")
    pass


def google_search(info):
    pass


def get_response(info, ara=False):
    answer = chatBot.get_response(statement=info)
    if ara:
        answer = translator.translate(f"{answer.text}", lang_src="eng", lang_tgt="ar")
    return answer
