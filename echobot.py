import telebot

bot = telebot.TeleBot('1622666315:AAEuQC1xYLhvwBVQh9lSdzKeCwLVlrpAflM')


# Бот отвечает зеркально.
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.send_message(message.chat.id, message.text)

# Заставляет бота работать бесконечно.
bot.polling(none_stop=True)
