import telebot

from telebot import types

bot = telebot.TeleBot('6018900334:AAFTNKyueds7RPssUEDV_EfBK1p7SWIfub0')

fio = None
phone_number = None
series_number = None
date_of_birth = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Записаться к врачу')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Отмена записи или вызова')
    btn3 = types.KeyboardButton('Вызов врача на дом')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, 'Приветствую! Со мной Вы сможете:'+'\n'+'📌Записаться на прием к врачу'+'\n'+'📌Оформить вызов врача на дом'+'\n'+'📌Отменить запись или вызов', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    inline_markup = types.InlineKeyboardMarkup(row_width=1)
    inline_button1 = types.InlineKeyboardButton(text="Перейти на страницу", url="https://gu.spb.ru/188453/eservice/")
    inline_markup.row(inline_button1)
    if message.text == 'Записаться к врачу':
     bot.send_message(message.chat.id, '⌨️ На Портале госуслуг Санкт-Петербурга вы можете записаться на прием к врачу в электронном виде. Услуга доступна даже тем, кто не зарегистрирован в ЕСИА (в Единой системе идентификации и аутентификации). В этом случае все данные для записи нужно будет просто внести вручную.', reply_markup=inline_markup)
     bot.send_message(message.chat.id, '🔑 За пользователей, у которых есть логин и пароль от госуслуг, это сделает система. Она автоматически заполнит все нужные поля. В личном кабинете вы также можете указать номер полиса ОМС, чтобы не вводить его заново, когда понадобится записаться к врачу в следующий раз.')
     bot.send_message(message.chat.id, 'Если ваши планы изменились или вы больше не нуждаетесь в данной услуге, то в незамедлительном случае отмените запись, вернувшись в начальное меню и выбрав кнопку "Отмена записи или вызова"')
    elif message.text == 'Отмена записи или вызова':
     bot.send_message(message.chat.id,'✏️ Если у вас изменились обстоятельства, вы можете отменить электронную запись. Для этого на странице услуги по записи или вызову нажмите кнопку «Подать заявление» и выберите «Отмена записи».', reply_markup=inline_markup)
    elif message.text == 'Вызов врача на дом':
     bot.send_message(message.chat.id, '✏️ Пожалуйста, укажите вашу фамилию, имя и отчество')
     bot.register_next_step_handler(message, on_fio)

def on_fio(message):
    global fio
    fio = message.text.strip()
    bot.send_message(message.chat.id, '✏️ Пожалуйста, укажите Ваш номер телефона:')
    bot.register_next_step_handler(message, on_phone_number)

def on_phone_number(message):
    global phone_number
    phone_number = message.text.strip()
    bot.send_message(message.chat.id, '✏️ Укажите серию и номер полиса:')
    bot.register_next_step_handler(message, on_series_number)

def on_series_number(message):
    global series_number
    series_number = message.text.strip()
    bot.send_message(message.chat.id, '✏️ Укажите дату Вашего рождения в формате ДД.ММ.ГГГГ:')
    bot.register_next_step_handler(message, on_date_of_british)

def on_date_of_british(message):
    global date_of_birth
    date_of_birth = message.text.strip()
    bot.send_message(message.chat.id, '✅ Ваша заявка на стадии обработки! Ожидайте смс на ваш телефон.')

    bot.send_message(message.chat.id, 'Если ваши планы изменились или вы больше не нуждаетесь в данной услуге, то в незамедлительном случае отмените запись, вернувшись в начальное меню и выбрав кнопку "Отмена записи или вызова"')

bot.polling(none_stop=True)