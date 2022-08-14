import os
import environ
import telegram.ext


env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


TOKEN = env('TOKEN')

def start(update, context):
    
    welcome_message = """
Welcome to Aurora QR Bot

Aurora QR Bot - bot that generates a QR code with different types of customizations

Customizations:

- Color of QR Code
- Logo on the QR Code 

"""

    update.message.reply_text(welcome_message)

def about(update, context):

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
    update.message.reply_text(about_text)

def help(update, context):

    help_msg = """
To learn more about the bot, please head over to /about

List of available commands:

/start - start the bot
/help  - guidelines of using the bot
/about - brief info about the bot
"""
    update.message.reply_text(help_msg)


def main():
    updater = telegram.ext.Updater(TOKEN, use_context=True)

    disp = updater.dispatcher


    disp.add_handler(telegram.ext.CommandHandler("start", start))
    disp.add_handler(telegram.ext.CommandHandler("about", about))
    disp.add_handler(telegram.ext.CommandHandler("help", help))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

