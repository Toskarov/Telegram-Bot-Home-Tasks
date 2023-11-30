import random
import os
import datetime
import telebot

# Telebot credentials
TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)


# housework chores:

def chores():
    housework = ["Vacuuming", "Mopping", "Cleaning the kitchen", "Cleaning the bathroom", "Empty", "Empty"]
    media = len(housework) // 3
    Alondra = []
    Kim = []
    Raul = []

    while housework:
        task = housework.pop(random.randint(0, len(housework)) - 1)  # take te random element from housework
        # Add the random item to a list that has not yet reached the media (average)
        if len(Alondra) < media:
            Alondra.append(task)
        elif len(Kim) < media:
            Kim.append(task)
        else:
            Raul.append(task)

    return f"*Tasks for the week:*\n*Alondra:* {', '.join(Alondra)}\n*Kim:* {', '.join(Kim)}\n*Raúl:* {', '.join(Raul)}"


# Save the last -or the first- execution date

def save_last_execution():
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime('%d-%m-%Y')
    with open('last_execution.txt', 'w') as file:
        file.write(current_date_str)


# Obtain the last execution date

def obtain_last_execution():
    if os.path.exists(
            r'PATH_TO_READ\last_execution.txt'):
        with open('last_execution.txt', 'r') as file:
            current_date_str = file.read()
            return datetime.datetime.strptime(current_date_str, '%d-%m-%Y')
    else:
        return None


# count days and execute something if >=7

def count_days():
    saved_date = obtain_last_execution()
    current_date = datetime.datetime.now()

    if saved_date is not None:
        past_days = current_date - saved_date
        if past_days > datetime.timedelta(days=7):
            save_last_execution()
            chat_id = 'CHAT_ID'
            message = chores()

            return bot.send_message(chat_id, message, parse_mode='Markdown')
        else:
            return f"it hasn't been 7 days, it's just been {past_days}"
    else:
        return "No found dates"


print(count_days())
