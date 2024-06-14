import random
import os
import datetime
import telebot

# Telebot credentials
TOKEN = 'YOUR TOKEN'
bot = telebot.TeleBot(TOKEN)


# housework chores:

def chores():
    housework = ["Vacuuming & Mopping", "Cleaning the kitchen", "Cleaning the bathroom", "free day"]
    Alondra = []
    Kim = []
    Raul = []
    Gonzalo = []

    # Add the random item to a list 
    while housework:
        task = housework.pop(random.randint(0, len(housework)) - 1) 
        if len(Alondra) < 1:
            Alondra.append(task)
        elif len(Kim) < 1:
            Kim.append(task)
        elif len(Gonzalo) < 1:
            Gonzalo.append(task)
        else:
            Raul.append(task)

    return f"*Tasks for the week:*\n*Alondra:* {', '.join(Alondra)}\n*Kim:* {', '.join(Kim)}\n*Raúl:* {', '.join(Raul)}\n*Gonzalo:* {', '.join(Gonzalo)}"


### Sentences for made better the chores.
def frasesMarxistas():
    frases_marxistas = [
        "La religión es el opio del pueblo. - Karl Marx",
        "Proletarios del mundo, uníos. - Karl Marx y Friedrich Engels, en el Manifiesto del Partido Comunista",
        "La historia de todas las sociedades hasta nuestros días es la historia de la lucha de clases. - Karl Marx y Friedrich Engels, en el Manifiesto del Partido Comunista",
        "Los filósofos no han hecho más que interpretar de diversos modos el mundo, pero de lo que se trata es de transformarlo. - Karl Marx, en su tesis XI sobre Feuerbach",
        "La revolución no es una cena de gala. - Mao Zedong",
        "¡Pueblo, levántate y mira las estrellas! ¡Mira hacia abajo y observa tus cadenas! - Rosa Luxemburgo",
        "La emancipación de la clase trabajadora debe ser obra de los propios trabajadores. - Karl Liebknecht",
        "Los teóricos sólo han interpretado el mundo de diversas maneras; pero de lo que se trata es de transformarlo. - Karl Marx, en la Introducción a la Crítica de la Filosofía del Derecho de Hegel",
        "La burguesía no puede existir sin revolucionar constantemente los instrumentos de producción. - Karl Marx y Friedrich Engels, en el Manifiesto del Partido Comunista",
        "La paz no puede ser separada de la lucha de clases. - Vladimir Lenin"
    ]

    frase = f"\n{random.choice(frases_marxistas)}"
    return frase


# Save the last -or the first- execution date

def save_last_execution():
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime('%d-%m-%Y')
    with open('last_execution.txt', 'w') as file:
        file.write(current_date_str)


# Obtain the last execution date

def obtain_last_execution():
    if os.path.exists(
            r'THE PATH YOU WANT TO HAVE THE LAST EXECUTION LOG:
        with open('last_execution.txt', 'r') as file:
            current_date_str = file.read()
            return datetime.datetime.strptime(current_date_str, '%d-%m-%Y')
    else:
        return None


# Count days and apply the logically
def count_days():
    saved_date = obtain_last_execution()
    current_date = datetime.datetime.now()
    # If the weekday is > 4 (friday) then do..
    if saved_date is not None:
        past_days = current_date - saved_date
        
        # I made it because y want the execute the script in Fri,Sat or Sun.
        if past_days > datetime.timedelta(days=4) and current_date.weekday() >= 4:
            save_last_execution()
            chat_id = 'YOUR CHAT ID'
            message = f"{chores()}\n{frasesMarxistas()}"
            return bot.send_message(chat_id, message, parse_mode='Markdown')
        else:
            return f"it hasn't been 7 days, it's just been {past_days}"
    else:
        return "No found dates"


count_days()

# If you want to view the last execution
print(count_days())
