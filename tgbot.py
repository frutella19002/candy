import telebot
from cfg import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Введите: \n 1) валюту из которой хотите перевести. \n 2) в какую валюту хотите перевести. \n 3) кол-во валюты. \n (без запятых, через пробел, с маленькой буквы) \n P.S доступные валюты можно посмотреть через комманду /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много/мало параметров.')

        quote, base, amount = values

        total_base = CryptoConverter.get_price(quote, base, amount)


        quantity_total_base = total_base * float(amount)


    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n {e}')
    except Exception as e:
        bot.reply_to(message, f'не удалось обработать комманду \n {e}')
    else:
        text = f'цена: {amount} {quote} = {quantity_total_base} {base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)






