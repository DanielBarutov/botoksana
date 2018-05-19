# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)


	
@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, 'Nice \n\nWrite /help for help.')

@bot.message_handler(commands=["help"])
def start(message):
	bot.send_message(message.chat.id, 'lol')







@bot.message_handler(content_types=["text"])
def messages(message):
	if int(message.chat.id) == int(config.owner):
		try:
			chatId=message.text.split(': ')[0]
			text=message.text.split(': ')[1]
			bot.send_message(chatId, text)
		except:
			pass
	else:
		bot.send_message(config.owner, str(message.chat.id) + ': ' + message.text)
		bot.send_message(message.chat.id, '%s, Good 👍'%message.chat.username)

if __name__ == '__main__':
	bot.polling(none_stop=True)
