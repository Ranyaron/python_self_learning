from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Test')
bot.set_trainer(ListTrainer)
# trainer = ListTrainer(ChatBot)

for _file in os.listdir('files'):
    chats = open('files/' + _file, 'r').readlines()
    bot.train(chats)

while True:
    request = input('You: ')
    response = bot.get_response(request)

    print('Bot: ', response)
