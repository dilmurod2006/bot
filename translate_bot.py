"""
crete translate and wikipedia bot
two buttons! the first button is translate and the second button is wikipedia
"""
from telebot import TeleBot
from telebot import types
from deep_translator import GoogleTranslator
token = "5988492660:AAFMWzbtYP4z8zbB4DHAlQErwSbFA6g-T_c"
bot = TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.chat.id, 'Hello!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('uz-en')
        item2 = types.KeyboardButton('en-uz')
        markup.add(item1,item2)
        bot.send_message(message.chat.id, 'Choose one of the buttons', reply_markup=markup)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def translate_wikipedia(message):
    if message.text == 'en-uz':
        bot.send_message(message.chat.id, 'Ingiliz tilida tarjima qilinadiga matn yuboring')
        bot.register_next_step_handler(message, translate_en_uz)
    if message.text == 'uz-en':
        bot.send_message(message.chat.id, "matn yuboring")
        bot.register_next_step_handler(message, translate_uz_en)
@bot.message_handler(content_types=['text'])
def translate_en_uz(message):
    text = GoogleTranslator(source='en', target='uz').translate(message.text)
    bot.send_message(message.chat.id, text)
def translate_uz_en(message):
    text = GoogleTranslator(source='uz', target='en').translate(message.text)
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
