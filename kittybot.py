from telegram.ext import CommandHandler, Updater, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup


BOT_TOKEN = '5302624518:AAFcQB_LQkM7FLKBBbDojsNH-e71U7rjcA0'

updater = Updater(token=BOT_TOKEN)

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я KittyBot!')

def wake_up(update, context):
    # В ответ на команду /start 
    # будет отправлено сообщение 'Спасибо, что включили меня'
    chat = update.effective_chat
    name = update.message.chat.first_name
    button = ReplyKeyboardMarkup([
                ['Который час?'], 
                ['Определи мой ip'],
                ['/random_digit'],
            ])
    context.bot.send_message(
                                chat_id=chat.id, 
                                text='Спасибо, что включили меня, {}!'.format(name),
                                reply_markup=button
                            )

# Регистрируется обработчик CommandHandler;
# он будет отфильтровывать только сообщения с содержимым '/start'
# и передавать их в функцию wake_up()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.start_polling()
updater.idle()  