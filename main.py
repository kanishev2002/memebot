"""A telegram bot that sends a random meme to the user."""
from os import environ as env

import requests
import telebot

TOKEN = env.get('TOKEN')
print(f'Token is: {TOKEN}')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Send an introduction message"""
    bot.reply_to(message, "Welcome to memebot. To get a random meme, type /send_meme")


@bot.message_handler(commands=['send_meme'])
def send_meme(message):
    """Send a meme to the user."""
    response = requests.get('https://meme-api.herokuapp.com/gimme')
    if not response.ok:
        return
    link = response.json()['url']
    bot.reply_to(message, link)


bot.infinity_polling()
