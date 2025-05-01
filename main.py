from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from handlers.start import start
from handlers.url_handler import handle_url
from handlers.settings_handler import settings, button_handler
from handlers.thumbnail import save_thumbnail
from handlers.rename import handle_rename

app = ApplicationBuilder().token("8054577554:AAHDFaD-VPMoSnSKST7LjqdsoFnyBHtXDTo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("settings", settings))
app.add_handler(MessageHandler(filters.PHOTO, save_thumbnail))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_url))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r'.+\..+'), handle_rename))

app.run_polling()
