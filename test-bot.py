import telebot

bot = telebot.TeleBot('5864036658:AAHbA-zu9RXLNvxaHt-FfzBShx_Ievy2ubA')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')
   

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, "Hello too you", parse_mode='html')
    elif message.text == "My id":
        bot.send_message(message.chat.id, f"Твой id: {message.from_user.id}", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю", parse_mode='html')


@bot.message_handler()
def first(photo):
    if message.photo == 'photo':
       bot.send_photo('window.png', 'rb') 
    else:
        bot.send_message(message.chat_id, 'no photo', parse_mode='html')
file = open('window.png' , 'rb')
file.read()
file.seek(0)
file.read()



@bot.message_handler(content_types=['text'])
def response(message):
    get_message_bot = message.text.strip().lower()

bot.polling(none_stop=True)