from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer = None


def get_trainer():
    return trainer


def set_trainer(_trainer):
    global trainer
    trainer = _trainer


def setup_bot(name):
    chatbot = ChatBot(name=name)
    _trainer = ChatterBotCorpusTrainer(chatbot)
    set_trainer(_trainer)
    #_trainer.train("chatterbot.corpus.english")
    return chatbot


class Bot:

    def __init__(self, name):
        # setting up the bot
        self.name = name
        self.bot = setup_bot(name)
        self.trainer = get_trainer()

    def get_response(self, statement, ara=False):
        return self.bot.get_response(statement=statement)

    def save(self):
        self.trainer.export_for_training('./bot_data.json')
