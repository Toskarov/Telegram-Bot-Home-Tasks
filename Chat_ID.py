# *******************************
# obtain the chat ID
# *********************************

import telebot

TOKEN = 'YOUR_TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def print_chat_id(message):
    print(f"Chat ID: {message.chat.id}")


bot.polling()

#You need to type in the chat where the bot is to get the CHAT ID in the python console.
