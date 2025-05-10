from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from handlers.start import start
from handlers.url_handler import handle_url
from handlers.settings_handler import settings, button_handler
from handlers.thumbnail import save_thumbnail
from handlers.rename import handle_rename
from threading import Thread
from flask import Flask

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive", 200

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

app = ApplicationBuilder().token("7742796316:AAELKOTlaSavyVcnd39LdMpkNGqdkHfbobE").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("settings", settings))
app.add_handler(MessageHandler(filters.PHOTO, save_thumbnail))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'.+\..+'), handle_rename))

app.run_polling()
