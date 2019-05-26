from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import User
import config

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(config.SECRET_KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    user = User
    username = user.name
    text = 'Привет {} Вызван {} /start'.format(username, bot.username)
    print(text)
    
    logging.debug (vars(user))
    logging.debug(bot)
    logging.debug("This is a debug message")
    logging.info(text)
    logging.info("Informational message")
    logging.error("An error has happened!")
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()