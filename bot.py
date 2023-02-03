"""
crete translate and wikipedia bot
two buttons! the first button is translate and the second button is wikipedia
"""
from telebot import TeleBot
from telebot import types
from wikipedia import wikipedia as wiki
from deep_translator import GoogleTranslator
import pyttsx3
token = "5988492660:AAFMWzbtYP4z8zbB4DHAlQErwSbFA6g-T_c"
bot = TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id==1485043917:
        bot.send_message(message.chat.id, 'Assalomu alaykum Admin!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #b1 = types.KeyboardButton('text to speech')
        b2 = types.KeyboardButton('Translate')
        b3 = types.KeyboardButton('Wikipedia')
        markup.add(b2, b3)
        bot.send_message(message.chat.id, 'Tugmalarni tanglang', reply_markup=markup)
    if message.chat.id==5420071824:
        bot.send_message(message.chat.id, 'Assalomu alaykum Admin!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #b1 = types.KeyboardButton('text to speech')
        b2 = types.KeyboardButton('Translate')
        b3 = types.KeyboardButton('Wikipedia')
        markup.add(b2, b3)
        bot.send_message(message.chat.id, 'Tugmalarni tanglang', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Hello!')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Translate')
        item2 = types.KeyboardButton('Wikipedia')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Choose one of the buttons', reply_markup=markup)

@bot.message_handler(content_types=['text', 'document', 'audio'])
def translate_wikipedia(message):
    if message.text == 'Translate':
        bot.send_message(message.chat.id, 'Ingiliz tilida tarjima qilinadiga matn yuboring')
        bot.register_next_step_handler(message, translate_text)
        """if message.text == 'Wikipedia':
            bot.send_message(message.chat.id, 'Qnday malumot kerak')
            bot.register_next_step_handler(message, wikipedia)
        if message.text == 'text to speech':
            bot.send_message(message.chat.id, 'mp3ga o\'girish uchun matn yuboring')
            bot.register_next_step_handler(message, text_to_speech)"""
    elif message.text == 'Wikipedia':
        bot.send_message(message.chat.id, 'Enter a text')
        bot.register_next_step_handler(message, wikipedia)
        """if message.text == 'Translate':
            bot.send_message(message.chat.id, 'Ingiliz tilida tarjima qilinadiga matn yuboring')
            bot.register_next_step_handler(message, translate_text)"""
    """elif message.text == 'text to speech':
        bot.send_message(message.chat.id, 'Enter a text')
        bot.register_next_step_handler(message, text_to_speech )
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ovoz = types.ReplyKeyboardMarkup("ovozni yubotish")
        markup.add(ovoz)
        bot.send_message(message.chat.id,reply_markup=markup)"""
    """elif message.text == 'ovozni yubotish':
        with open('test.ogg', 'rb') as audio:
            bot.send_audio(message.chat.id, audio)"""
        
        #bot.send_audio(message.chat.id, 'test.ogg')
@bot.message_handler(content_types=['text'])
def translate_text(message):
    text = GoogleTranslator(source='auto', target='en').translate(message.text)
    bot.send_message(message.chat.id, text)
@bot.message_handler(content_types=['text'])
def wikipedia(message):
    wiki.set_lang('uz')
    text = wiki.summary(message.text)
    bot.send_message(message.chat.id, text)

"""@bot.message_handler(content_types=['text'])
def text_to_speech(message):
    engine = pyttsx3.init()
    engine.save_to_file(message.text, 'test.ogg')
    engine.runAndWait()"""

bot.polling(none_stop=True)
