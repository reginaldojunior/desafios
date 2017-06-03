from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')
	
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Hello!\n"
    msg += "I'm {0} and I came here to help you.\n".format(me.first_name)
    msg += "What would you like to do?\n\n"
    msg += "/support - Opens a new support ticket\n"
    msg += "/settings - Settings of your account\n\n"

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/support')],
                          [telegram.KeyboardButton('/settings')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

updater = Updater('390538628:AAFEBJzvhs2OZky4UCPUt4vLH21RbVjU2dg')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()