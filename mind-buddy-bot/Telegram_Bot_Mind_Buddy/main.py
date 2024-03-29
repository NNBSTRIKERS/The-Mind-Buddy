from asyncio import constants
from turtle import update
from urllib import response
import constants as keys

from telegram.ext import *
import Responses as R

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Type something random to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help, you should ask for it!')

def assess_command(update, context):
    update.message.reply_text("We are starting the assessment now! Type 'Yes' to proceed.")

def handle_message(update, context):
    text = str(update.message.text).lower()

    response= R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater= Updater(keys.API_KEY, use_context=True)

    dp= updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("assess", assess_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
