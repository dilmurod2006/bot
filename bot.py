import telebot

token = "6034195441:AAHLELU5vN6LPeFXWed07ODfoxmeJmmk9w4"

bot  = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"bot.service file ishladi ura")


bot.polling(none_stop=True)
