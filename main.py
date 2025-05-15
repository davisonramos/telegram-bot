from telegram.ext import Updater, CommandHandler
import os

# Coloque seu token aqui
TOKEN = os.environ['TELEGRAM_TOKEN']


# Função que será chamada quando o /start for enviado
def start(update, context):
    update.message.reply_text("Olá! Eu sou seu bot 😎")


# Função principal
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comando /start
    dp.add_handler(CommandHandler("start", start))

    # Inicia o bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
