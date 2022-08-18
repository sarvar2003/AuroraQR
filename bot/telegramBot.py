import asyncio
from curses import COLOR_GREEN, COLOR_RED
from time import sleep
from telegram import *
from telegram.ext import *
from requests import *

import qrcode




class AuroraBot:
    def __init__(self) -> None:
        self.data = ""
        self.Start = "Start"
        self.Help = "Help"
        self.About = "About"
        self.GenerateQR = "GenerateQR"
        self.Data = None

    def startCommand(self, update: Update, context: CallbackContext):
        # Buttons that will appear when start command is called

        self.Data = None

        buttons = [[KeyboardButton(self.Start), KeyboardButton(self.Help), KeyboardButton(self.About)],[KeyboardButton(self.GenerateQR)]]

        username = update.message.chat.username

        welcome_message = f"""
    Welcome to Aurora QR Bot, @{username}!

    Aurora QR Bot - bot that generates a QR code with different types of customizations

    Customizations:

    - Color of QR Code
    - Logo on the QR Code 

    """


        context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message, reply_markup = ReplyKeyboardMarkup(buttons))



    def helpCommand(self, update: Update, context: CallbackContext):

        # Buttons that appear when help command is called
        buttons = [[KeyboardButton(self.GenerateQR)],[KeyboardButton(self.Start), KeyboardButton(self.About)]]

        help_msg = """
    Using the bot is pretty simple
    """ 
        
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_msg, reply_markup=ReplyKeyboardMarkup(buttons))




    def aboutCommand(self, update: Update, context: CallbackContext):

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


    def generateQR(self, update: Update, context: CallbackContext):

        """
        QR code generator Selection
        """
        # print(update.message.text)

        if update.message.text == 'GenerateQR':
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please enter data to encode (Link/Data): ")

        data = update.message.text

        if not self.Data and data != 'GenerateQR':
            self.Data = data

        if data == 'GenerateQR':
            return
        
        if data != 'GenerateQR':
            colors = {
                '🟥': 'Red',
                '🟧': 'Orange',
                '🟨': 'Yellow',
                '🟩': 'Green',
                '🟦': 'Blue',
                '🟫': 'Brown',
                '⬛': 'Black',
                '🟪': 'Purple',
                '⬜': 'White'
            }
            color_buttons = [
                    [KeyboardButton('🟥'),KeyboardButton('🟧'), KeyboardButton('🟨')],
                    [KeyboardButton('🟩'), KeyboardButton('🟦'),KeyboardButton('🟫')],
                    [KeyboardButton('⬛'), KeyboardButton('⬜'),KeyboardButton('🟪')]
                ]
        
            context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose the color of your QR code: ", reply_markup=ReplyKeyboardMarkup(color_buttons))
            color = colors[update.message.text]

        qr = qrcode.QRCode(version = 1, box_size = 10, border = 3)

        print(f'THIS: {self.Data}')
        qr.add_data(self.Data)

        qr.make(fit=True)
        
        image = qr.make_image(fill_color=color, back_color='White')
        image.save('YourQR.png')

        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('YourQR.png', 'rb'))

        

    def messageHandler(self, update: Update, context: CallbackContext):

        """
        Dynamic message handler
        """

        if self.Start in update.message.text:
            self.startCommand(update, context)
        elif self.Help in update.message.text:
            self.helpCommand(update, context)
        elif self.About in update.message.text:
            self.aboutCommand(update, context)
        elif self.GenerateQR in update.message.text:
            self.generateQR(update, context)
            

def main():
    updater = Updater(token="5508338510:AAHUc4tIS9edzMR_XD8gKP0rrzxKmA4LorU")
    dispatcher = updater.dispatcher

    bot = AuroraBot()

    dispatcher.add_handler(CommandHandler("start", bot.startCommand))
    dispatcher.add_handler(MessageHandler(Filters.text, bot.generateQR))
    dispatcher.add_handler(MessageHandler(Filters.text, bot.messageHandler))

    updater.start_polling()