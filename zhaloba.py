import telebot
import math
from telebot import types
from telebot.types import KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

TOKEN = '1067853332:AAFKDeTl-e4ywm3oS4z4bfC3Yrlp05_bmzE'
admin_id = 780183482

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands = ['start'])
def cmd_start(message):
    keyboard = types.InlineKeyboardMarkup()
    start_qweth = types.InlineKeyboardButton(text='Частые вопросы 💻',callback_data='qweth')
    start_howbuy = types.InlineKeyboardButton(text='Как заказать 🛠', callback_data='howbuy')
    start_reviews = types.InlineKeyboardButton(text='Отзывы 📨', callback_data='reviews')
    start_tariff = types.InlineKeyboardButton(text='Тариф 💸', callback_data='tariff')
    start_teaching = types.InlineKeyboardButton(text='Обучение 📚', callback_data='teaching')
    start_howmuch = types.InlineKeyboardButton(text='Стоимость заказа 🧮', callback_data='howmuch')
    start_order = types.InlineKeyboardButton(text='Сделать заказ 📦', callback_data='order')


    keyboard.add(start_qweth, start_howbuy)
    keyboard.add(start_reviews, start_tariff)
    keyboard.add(start_teaching, start_howmuch)
    keyboard.add(start_order)
    bot.send_photo(chat_id = message.from_user.id, photo = 'https://imbt.ga/vz1OIqegdB', reply_markup=keyboard)
    bot.send_message(message.chat.id, '"GORILLA VBIV║ASOS║AMAZON║FARFETCH"\n• РАБОТАЕМ БОЛЕЕ ГОДА\n• ИМЕЕМ ОГРОМНУЮ БАЗУ КЛИЕНТОВ\n• ПОДДЕРЖКА 24/7', reply_markup=keyboard)


#ИЗНАЧАЛЬНОЕ МЕНЮ
start_qweth = types.InlineKeyboardButton(text='Частые вопросы 💻',callback_data='qweth')
qweth = InlineKeyboardMarkup().add(start_qweth)
start_howbuy = types.InlineKeyboardButton(text='  Как заказать 🛠', callback_data='howbuy')
howbuy = InlineKeyboardMarkup().add(start_howbuy)
start_reviews = types.InlineKeyboardButton(text='Отзывы 📨', callback_data='reviews')
reviews = InlineKeyboardMarkup().add(start_reviews)
start_tariff = types.InlineKeyboardButton(text='Тариф 💸', callback_data='tariff')
tariff = InlineKeyboardMarkup().add(start_tariff)
start_teaching = types.InlineKeyboardButton(text='Обучение 📚', callback_data='teaching')
teaching = InlineKeyboardMarkup().add(start_teaching)
start_howmuch = types.InlineKeyboardButton(text='Стоимость заказа 🧮', callback_data='howmuch')
howmuch = InlineKeyboardMarkup().add(start_howmuch)
start_order = types.InlineKeyboardButton(text='Сделать заказ 📦', callback_data='order')
order = InlineKeyboardMarkup().add(start_order)

#ВОЗВРАТ

keyret = types.InlineKeyboardMarkup()
keyret.add(start_qweth, start_howbuy)
keyret.add(start_reviews, start_tariff)
keyret.add(start_teaching, start_howmuch)
keyret.add(start_order)
#bot.send_photo(chat_id = message.from_user.id, photo = 'https://imbt.ga/vz1OIqegdB', reply_markup=keyret)


def backmenu(message):
    KeyboardBack = types.InlineKeyboardMarkup()
    BackMenu = types.InlineKeyboardButton(text='В меню', callback_data='BM')

BackMenu = types.InlineKeyboardButton(text='В меню', callback_data='BM')
BM = InlineKeyboardMarkup().add(BackMenu)
KeyBack = types.InlineKeyboardMarkup()
KeyBack.add(BackMenu)



#МЕНЮ Ч-Е В-Ы
def chastvoprkye(message):
    chastvopr = types.InlineKeyboardMarkup()
    chastvopr01 = types.InlineKeyboardButton(text='Покупки 💳', callback_data = 'chv01')
    chastvopr02 = types.InlineKeyboardButton(text='Блокировка устройств 📱', callback_data = 'chv02')
    chastvopr03 = types.InlineKeyboardButton(text='Доставка 📦', callback_data = 'chv03')
    chastvopr04 = types.InlineKeyboardButton(text='Оплата 💸', callback_data = 'chv04')
    chastvopr05 = types.InlineKeyboardButton(text='Оригинальность товара 📃', callback_data = 'chv05')
    chastvopr06= types.InlineKeyboardButton(text='Гарантия на получения товара ⁉️', callback_data = 'chv06')

    chv01 = InlineKeyboardMarkup().add(chastvopr01)
    chv02 = InlineKeyboardMarkup().add(chastvopr02)
    chv03 = InlineKeyboardMarkup().add(chastvopr03)
    chv04 = InlineKeyboardMarkup().add(chastvopr04)
    chv05 = InlineKeyboardMarkup().add(chastvopr05)
    chv06 = InlineKeyboardMarkup().add(chastvopr06)

chastvopr = types.InlineKeyboardMarkup()
chastvopr01 = types.InlineKeyboardButton(text='Покупки 💳', callback_data = 'chv01')
chastvopr02 = types.InlineKeyboardButton(text='Блокировка устройств 📱', callback_data = 'chv02')
chastvopr03 = types.InlineKeyboardButton(text='Доставка 📦', callback_data = 'chv03')
chastvopr04 = types.InlineKeyboardButton(text='Оплата 💸', callback_data = 'chv04')
chastvopr05 = types.InlineKeyboardButton(text='Оригинальность товара 📃', callback_data = 'chv05')
chastvopr06= types.InlineKeyboardButton(text='Гарантия на получения товара ⁉️', callback_data = 'chv06')

chv01 = InlineKeyboardMarkup().add(chastvopr01)
chv02 = InlineKeyboardMarkup().add(chastvopr02)
chv03 = InlineKeyboardMarkup().add(chastvopr03)
chv04 = InlineKeyboardMarkup().add(chastvopr04)
chv05 = InlineKeyboardMarkup().add(chastvopr05)
chv06 = InlineKeyboardMarkup().add(chastvopr06)

chastvopr.add(chastvopr01)
chastvopr.add(chastvopr02)
chastvopr.add(chastvopr03)
chastvopr.add(chastvopr04)
chastvopr.add(chastvopr05)
chastvopr.add(chastvopr06)
chastvopr.add(BackMenu)



#МЕНЮ ОБУЧЕНИЯ
teachingkey= types.InlineKeyboardMarkup()
start_teaching = types.InlineKeyboardButton(text='НАЧАТЬ ОБУЧЕНИЕ', url = 'https://t.me/GORILLA_VBIV')
teaching2 = types.InlineKeyboardButton(text='ОБУЧЕНИЕ КАРДИНГУ', url = 'https://tgraph.io/Obuchenie-Karding-Ebay-06-14')
teaching3 = types.InlineKeyboardButton(text='ОБУЧЕНИЕ ЦИФРОВОМУ КАРДИНГУ', url = 'https://tgraph.io/Obuchenie-Cifrovomu-Kardingu-06-14')
teachingkey.add(start_teaching)
teachingkey.add(teaching2)
teachingkey.add(teaching3)
teachingkey.add(BackMenu)



#МЕНЮ СДЕЛАТЬ ЗАКАЗ
def takesellkey(message):
    takesell = types.InlineKeyboardMarkup()
    takesell01 = types.InlineKeyboardButton(text='Заказ с сайта', callback_data = 'ts1')
    ts1 = InlineKeyboardMarkup().add(takesell01)

    takesell02 = types.InlineKeyboardButton(text='Заказ товара в наличии', callback_data = 'ts2')
    ts2 = InlineKeyboardMarkup().add(takesell02)

takesell = types.InlineKeyboardMarkup()

takesell01 = types.InlineKeyboardButton(text='Заказ с сайта', callback_data = 'ts1')
ts1 = InlineKeyboardMarkup().add(takesell01)

takesell02 = types.InlineKeyboardButton(text='Заказ товара в наличии', callback_data = 'ts2')
ts2 = InlineKeyboardMarkup().add(takesell02)

takesell.add(takesell01)
takesell.add(takesell02)
takesell.add(BackMenu)



#ССЫЛКИ
chastolink = '<a href="https://tgraph.io/Tut-my-sobrali-samye-chasto-zadavaemye-voprosy-06-03">Частые вопросы💻</a>'
howbuylink = '<a href="https://telegra.ph/CHto-nuzhno-dlya-zakaza-06-03">Как заказать🛠</a>'



#ФУНКЦИИ КНОПОК
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.data == "qweth":
            bot.send_message(chat_id=call.from_user.id, text="""<a href="https://telegra.ph/Tut-my-sobrali-samye-chasto-zadavaemye-voprosy-06-03">Частые вопросы💻</a>\n\n\n<a href="https://tgraph.io/Tut-my-sobrali-samye-chasto-zadavaemye-voprosy-06-03">В случае, если не открывается</a>""",reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "BM":
            bot.send_photo(chat_id=call.from_user.id, photo='https://imbt.ga/vz1OIqegdB', reply_markup=keyret)

        elif call.data == "ts1":
            bot.send_message(chat_id=call.from_user.id, text='<b>Для заказа пришлите боту</b>\n\nФИО, город, улица , индекс , Область , номер телефона, способ оплаты.  <b>На латинице!</b>\n\n\n<b>Пример:</b>\n\nTarasov Andrey Stepanovich\nMoscow\nTverskaya street, 13\n125009\nMoscow Region\n74955059322\nКарта Bitcoin QIWI\n\n\nИ внести мин сумму в размере 300руб для того что бы мы убедились в вашей платежеспособности.', reply_markup=takesell, parse_mode='HTML')
        elif call.data == "ts2":
            bot.send_message(chat_id=call.from_user.id, text='<b>Для заказа товара в наличии от дропа пришлите боту</b>\n\n\nТовар в наличии \nФИО, город, улица , индекс , Область , номер телефона, способ оплаты.  <b>На латинице!</b>\nПример:\nТовар: 11 Pro Space Gray 256GB\n\nTarasov Andrey Stepanovich\nMoscow\nTverskaya street, 13\n125009\nMoscow Region\n74955059322\nКарта Bitcoin QIWI\n\n\nИ внести 50% от сумма товара остальная оплата после отправки и получении трек номера.\nДоставка осуществляется: СДЭК, DHL, НП', reply_markup=takesell, parse_mode='HTML')

        elif call.data == "howbuy":
            bot.send_message(chat_id=call.from_user.id, text='''<a href="https://telegra.ph/CHto-nuzhno-dlya-zakaza-06-03">Как заказать🛠</a>\n\n\n<a href="https://tgraph.io/CHto-nuzhno-dlya-zakaza-06-03">В случае, если не открывается</a>''',reply_markup=KeyBack, parse_mode='HTML')

        elif call.data == "reviews":
            bot.send_message(chat_id=call.from_user.id, text="""Отзывы тех, кто пользовался услугами GORILLA VBIV\n\n<a href="https://t.me/joinchat/AAAAAEensaosa3gUSdQWDg">Отзывы🛠</a>\n\nКанал:<a href="https://t.me/joinchat/AAAAAESUWKdBc_aHDTDGBw">GORILLA VBIV</a>\nСвязь:<a href="https://t.me/GORILLA_VBIV">GORILLA_VBIV</a>""", reply_markup=KeyBack, parse_mode='HTML')

        elif call.data == "tariff":
            bot.send_message(chat_id=call.from_user.id, text="<a>https://imbt.ga/2sicF42UNY</a>\nМинимум — Максимум\n<b>100$ — 5000$</b>\n\n\nКомиссия за заказ 50% с любой суммой заказа от\n<b>100$ — 5000$</b>""", reply_markup =KeyBack, parse_mode='HTML')
            bot.send_photo(chat_id=call.from_user.id, photo='https://imbt.ga/2sicF42UNY',reply_markup=KeyBack)

        elif call.data == "teaching":
            bot.send_message(chat_id=call.from_user.id, text="pop", parse_mode='HTML')
            bot.send_photo(chat_id=call.from_user.id, photo='https://imbt.ga/lTTnpmPPGo', reply_markup=teachingkey)

        elif call.data =="howmuch":
            bot.send_message(chat_id=call.from_user.id, text="введите цену Вашего товара(в долларах):  ", parse_mode='HTML')

        elif call.data == "order":
            bot.send_photo(chat_id=call.from_user.id, photo='https://imbt.ga/mH3jPJXUjd', reply_markup=takesell)

        elif call.data == "chv01":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Мы не покупаем технику за свои деньги. Дело в том, что существует такое понятие, как Вещевой Кардинг, или просто Вещевуха.\n\nВещевой кардинг появился, когда обналичивание грязных денег стало представлять определенную сложность, поскольку зачастую для этого требуется физическое лицо обладателя карты. Поэтому «умельцы» приобретают товар удаленно в Интернет-магазинах Европы, США, или Великобритании. В отдельных случаях доходило до того, что фирменный товар можно было купить по цене в половину ниже отпускной цены производителя.\n\nВесь товар изначально заказывается на дропов, первичный заказ делается именно на них. Дропы все ручные, расположены почти по всему европейскому союзу. Далее уже тети Зины дяди Васи этих дропов делают пересыл на СНГ, откуда ваш товар доставляется курьерской службой! Так что можете не переживать о том что к вам придут и постучат в дверь.", reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "chv02":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="По поводу блокировки устройств и подобной белиберды - вместе с заказанным устройством на руки вы получаете все идущие к нему комплектующие, всю документацию с серийными, имей номерами. Чтобы вам было понятно, мои умники и умницы, имея все номера устройства, не один озлобленный америкашка, итальяшка, инопланетяшка, даже порвав свою жопу на тысячи частей, не сможет заблокировать устройство. На примере всеми любимых яблок (apple) - дабы заблокировать устройство удаленно, оно должно быть авторизовано в Айклауд, ну а аппараты все запакованные, даже не активированные. Следственно о каком Айклауде может идти речь?",reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "chv03":
            bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.message_id, text="• Товар проходит через дропа и попадает на территорию СНГ за 20 - 30 дней.\n• Минимальный заказ 200$\n• За дополнительную плату можно ускорить доставку.\n• Доствка через CDEK, DHL. Все зависит от страны покупателя.\n• Товар проходит таможенный контроль 100%. Проверено неоднократно на примере России, Украины, Республике Беларусь и ряде других стран СНГ. По Европе и США также без проблем. Никаких доп. затрат. Существует масса способов обхода таможженых пошлин (мы используем поддельные докладные).\n• Доставка курьером. При доставке курьер звонит заранее. По желанию можете сами забрать товар в отделении.\n• Необходимая информация для оформления заказа: имя и фамилия, адрес доставки с индексом, номер телефона, email.\n• После оформления всегда выдаём трек номер посылки.\n\nНаложенный платеж:\n\n\nРод деятельности к сожалению таков, что приходится делать отправки с левых данных, по причине этого мы не работаем с наложенным платежом, личными встречами, мечеными деньгами и прочим. Сесть не хочет никто и это все прекрасно понимают." ,reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "chv04":
            bot.edit_message_text(chat_id = call.message.chat.id,message_id=call.message.message_id, text="Оплата производится на картку VISA Mastercard Bitcoin или Qiwi.\nОплата картой даёт вам возможность отменить платеж в течение недели, просто позвонив в банк. Таким образом, в случае обмана, вы сможете вернуть себе деньги и сделать нам немало проблем. Это даёт вам возможность находиться в полной безопасности и гарантирует возврат средств в случае возникновения каких-либо проблем.", reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "chv05":
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="Весь предлагаемый нами ассортимент товара полностью оригинал, все строго новое, никаких рефов, лоченых устройств и т.п.", reply_markup=chastvopr, parse_mode='HTML')

        elif call.data == "chv06":
            bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id, text="К сожалению, в телеграмме развелось очень много нечисти и кидал, остаётся только принять этот факт. При работе со своими клиентами, в отличии от всех, «подобных» каналов, мы даём очень хорошую гарантию тем, что оплату за товар принимаем переводом на карту. Во многих банках транзакцию можно оспорить в течении недели после перевода, в остальных же - отследить средства и создать кучу неприятностей, в случае каких-либо проблем с нашей стороны, у клиента это займёт не более двух часов. Помимо этого, работа так называемых «скам» проектов продолжается не более месяца, далее их либо находят по причине частых жалоб в органы, либо они попросту сдуваются и перестают работать. У нас же, вы видите канал со всеми датами и кучей отзывов - опять же которых, думаю сами понимаете что просто так взять нигде нельзя.", reply_markup=chastvopr, parse_mode='HTML')
    except Exception as error:
        print("Info: {}".format (error))


@bot.message_handler(func = lambda message: True)
def handle_text(message):
    try:
        if message.chat.id == int(admin_id):
            bot.send_message(message.reply_to_message.forward_from.id,message.text)
        else:
            bot.forward_message(admin_id, message.chat.id, message.message_id)

    except Exception as error:
        print("Info: {}".format (error))

    try:
        numsell = int(message.text)/2
        if int(message.text) < 5000 or int(message.text) > 100:
            bot.send_message(chat_id = message.from_user.id, text ='К оплате: ' + str(numsell),reply_markup=KeyBack)
    except Exception as error:
        print("Info: {}".format (error))






bot.infinity_polling(True)