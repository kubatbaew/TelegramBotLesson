from telebot import TeleBot, types
from config import BOT_TOKEN


bot = TeleBot(token=BOT_TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    
    button = types.InlineKeyboardButton(text="Нажми меня", callback_data="button_click")
    markup.add(button)
    
    bot.send_message(
        message.chat.id,
        "Привет!",
        reply_markup=markup
    )
    
    
@bot.callback_query_handler(func=lambda call: True)
def button_click(call: types.CallbackQuery):
    if call.data == "button_click":
        bot.send_message(call.message.chat.id, "Вы нажали на кнопку!")


@bot.message_handler(commands=["help"])
def command_help(message: types.Message):
    bot.send_message(
        message.chat.id,
        "<strong>/start</strong> - <em>Старт Бота</em>\n<strong>/help</strong> - <em>Показать команды</em>",
        parse_mode="html",
    )



@bot.message_handler()
def photo(message: types.Message):
    if str(message.text).lower() == "фото":
        with open("images/photo.jpg", 'rb') as photo:
            bot.send_photo(
                message.chat.id,
                photo
            )
    elif message.text == "Команды":
        command_help(message)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
        button = types.InlineKeyboardButton(text="Команды")
        markup.add(button)
        
        bot.send_message(
        message.chat.id,
        "Что вы хотите сделать?",
        reply_markup=markup
    )


    
if __name__ == "__main__":
    print("Что юы остановить: Ctlr+C")
    bot.polling(allowed_updates=True)
