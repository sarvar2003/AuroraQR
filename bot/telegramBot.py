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
    
    \t\t\tWelcome to Aurora QR Bot

    Aurora QR Bot - bot that generates a QR code with different types of customizations

    Customizations:

    - Color of QR Code
    - Logo on the QR Code 
    

    Available Commands:

    /start - Start the bot
    /help  - Guideline of using the bot
    /about - Brief information about bot credits and developer contact details

    Contact:
        - khaydaraliev99@gmail.com
    """

    update.message.reply_text(welcome_message)


def main():
    updater = telegram.ext.Updater("5508338510:AAHUc4tIS9edzMR_XD8gKP0rrzxKmA4LorU", use_context=True)

    disp = updater.dispatcher


    disp.add_handler(telegram.ext.CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()