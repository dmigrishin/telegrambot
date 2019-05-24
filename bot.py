from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater("793650499:AAHmpenNWfX7_AKeYDDZZqCf6X83V_a6oKY", request_kwargs=PROXY)
     # токен для бота - как ключ от квартиры, лучше в публичных местах типа гитхаба не оставлять, а то кто угодно может его взять
     # обычно его выносят в отдельный файл, который добвляют в .gitignore и не "светят" наружу

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    # давай тут хоть приветствие по имени или нику добавим? если есть имя - его, если нет - ник, или наоборот
    text = 'Вызван /start'
    print(text) # если уж подключаешь логгирование - пользуйся им. советую использовать сразу 2 кровня info и debug
    # все "отладочные" принты выводить в debug, а важные - в info
    # для того чтобы запкстить в дебаге, в конфиге логов надо поставить уровень логирования дебаг
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

main()
