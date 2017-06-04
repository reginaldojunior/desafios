import os
from telegram.ext import Updater, CommandHandler

"""
    Command is calling if /start
"""


def start(bot, update):
    update.message.reply_text('Start using /NadaPraFazer')

"""
    Command is calling if /NadaPraFazer
"""


def nadaprafazer(bot, update):
    message = update.message.text
    message = message.split(' ')
    reddits = message[1].split(';')

    for reddit in reddits:
        update.message.reply_text('Crawling data from...' + reddit)
        command = "scrapy runspider reddit.py -a " + \
                  "subreddit=r/" + str(reddit) + \
                  " -a chat_id=" + str(update.message.chat.id) + \
                  " &> /dev/null &"
        os.system(command)

updater = Updater('390538628:AAFEBJzvhs2OZky4UCPUt4vLH21RbVjU2dg')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('NadaPraFazer', nadaprafazer))

updater.start_polling()
updater.idle()
