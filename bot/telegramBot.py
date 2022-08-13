import telegram.ext


def start(update, context):
    update.message.reply_text("Welcome to Aurora QR Bot!")


def main():
    updater = telegram.ext.Updater("", use_context=True)

    disp = updater.dispatcher


    disp.add_handler(telegram.ext.CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()