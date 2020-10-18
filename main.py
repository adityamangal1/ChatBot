'''
Made by - Aditya mangal
Purpose - Python mini project 
Date  - 18 october 2020
'''
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train('chatterbot.corpus.english')

print('\t\t\t A Chatbot')
print('You can quit by type q\n')
while True:
    query = input(">> ")
    if 'q' in query:
        exit()
    else:
        print(chatbot.get_response(query))
