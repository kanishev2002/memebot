from os import environ as env

import telebot

TOKEN = env.get('TOKEN')
print(f'Token is: {TOKEN}')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler()
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()