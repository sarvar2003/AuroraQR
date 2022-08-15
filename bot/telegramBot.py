from telegram import *
from telegram.ext import *
from requests import *

import qrcode


# Available commands
Start = "Start"
Help = "Help"
About = "About"
GenerateQR = "GenerateQR"
Link = "Link"
Data = "Data"

def startCommand(update: Update, context: CallbackContext):
    # Buttons that will appear when start command is called
    buttons = [[KeyboardButton(Start), KeyboardButton(Help), KeyboardButton(About)],[KeyboardButton(GenerateQR)]]

    username = update.message.chat.username

    welcome_message = f"""
Welcome to Aurora QR Bot, @{username}!

Aurora QR Bot - bot that generates a QR code with different types of customizations

Customizations:

- Color of QR Code
- Logo on the QR Code 

"""


    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, reply_markup = ReplyKeyboardMarkup(buttons))



def helpCommand(update: Update, context: CallbackContext):

    # Buttons that appear when help command is called
    buttons = [[KeyboardButton(GenerateQR)],[KeyboardButton(Start), KeyboardButton(About)]]

    help_msg = """
Using the bot is pretty simple
""" 
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg, reply_markup=ReplyKeyboardMarkup(buttons))




def aboutCommand(update: Update, context: CallbackContext):

    about_text = """
Aurora QR Bot - bot that generates a QR code with different types of customizations. You can use this bot for link redirections, barcodes and etc. You can also insert your own logo or any image in the QR code. And many more features are coming soon.

Credits:
Javokhirbek Khaydaraliev:
Email:   khaydaraliev99@gmail.com
LinkedIn:  https://www.linkedin.com/in/javokhirbek-kh
GitHub:  https://github.com/javokhirbek1999
Instagram:   https://www.instagram.com/dev_jeff20/

Sarvarbek Juraev:
Email:   sarvarbekjuraev159@gmail.com
LinkedIn     https://www.linkedin.com/in/sarvarbek-juraev-bb5888237/
GitHub:      https://github.com/sarvar2003
Instagram:    https://www.instagram.com/sarvar_striker/


Report an issue  https://github.com/javokhirbek1999/AuroraQR/issues 

    """

    context.bot.send_message(chat_id=update.effective_chat.id, text=about_text)


def generateQR(update: Update, context: CallbackContext):

    """
    QR code generator Selection
    """

    # Buttons that appear when help command is called
    buttons = [[KeyboardButton(Link), KeyboardButton(Data)], [KeyboardButton(Start)]]

    linkOrData = "What data are you going to encode ?"

    context.bot.send_message(chat_id=update.effective_chat.id, text=linkOrData, reply_markup=ReplyKeyboardMarkup(buttons))


def generateQRData(update: Update, context: CallbackContext):

    """
    QR code generator for Data
    """
    pass



def generateQRLink(update: Update, context: CallbackContext):

    """
    QR code generator for Links
    """
    pass



def messageHandler(update: Update, context: CallbackContext):

    """
    Dynamic message handler
    """

    if Start in update.message.text:
        startCommand(update, context)
    elif Help in update.message.text:
        helpCommand(update, context)
    elif About in update.message.text:
        aboutCommand(update, context)
    elif GenerateQR in update.message.text:
        generateQR(update, context)
    elif Data in update.message.text:
        generateQRData(update, context)
    elif Link in update.message.text:
        generateQRLink(update, context)


def main():
    updater = Updater(token="5508338510:AAHUc4tIS9edzMR_XD8gKP0rrzxKmA4LorU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", startCommand))
    dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

    updater.start_polling()