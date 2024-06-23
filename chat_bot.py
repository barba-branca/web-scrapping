# importando a bibliotecha chatterbot

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


# dando um nome para o chatbot

bot = ChatBot('yoha')

# criando DB
bot = ChatBot(
    'yoha',
    storage_adapter='chatterbot.storage.SQLDtorageAdapter',
    database_uri='sqlite//database.sqlite3'
)

# especificando adaptadores logicos

bot = ChatBot(
    'yoha',
    storange_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:database.sqlite3'
)

# Obtendo uma resposta do seu bot de bate-papo

while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input)
        
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
    
# Treinando bot de bate-papo

trainer = ListTrainer(bot)

trainer.train([])