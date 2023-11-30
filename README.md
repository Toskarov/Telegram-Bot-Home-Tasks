# Telegram-Bot-Home-Tasks

> I created this bot for my roommates because we needed a plan to manage household chores. The bot uses an array where we store various tasks. Its purpose is to randomize these tasks every 7 days, ensuring that we never repeat the same task within that timeframe.

For run this bot you need your telebot token, you can get it at **BotFather** _(it's a telegram bot to create your new bot)_ , just say 
```` telegram
/newbot

````
follow the steps and **copy the HTTP API** *(it's your telebot token)*

On the other hand to get your **Chat ID** you need to execute
````Python 
Chat_ID.py
````
And type anything in your bot, you will see your Chat ID in your python console

This program only gets the time when you use it. 
So one of more ways is to run it when you turn on your pc.

**To do it on windows:**
- Make a shorcut for *Telegram_bot.py*

*press:*
````Powershell
Win+R
````
*And type*
````Powershell
shell:startup
````
*Copy the shorcut into the directory*, the program will start  when you log in to your account

**To do it on Linux:**

- Use crontab and add the script path
````bash
crontab -e
````
Add the path to the script and don't forget to do
````shell
@reboot /script/path
````

