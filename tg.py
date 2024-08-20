import telebot

bot = telebot.TeleBot("6821040399:AAEHRjALNFNWXBWhBhQwRZASS2YAmZ75UQ8", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum, yaxshimisiz? Bu start bo'limi.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Bu yerdan siz yordam olishingiz mumkin.")

@bot.message_handler(commands=['bellashuv'])
def send_bellashuv(message):
    bot.reply_to(message, "Bu bellashuv bo'limi. Bellashuvga tayyor bo'ling!")

@bot.message_handler(commands=['lugat'])
def send_lugat(message):
    bot.reply_to(message, "Bu lug'at bo'limi. Siz bu yerda yangi so'zlarni o'rganishingiz mumkin.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
