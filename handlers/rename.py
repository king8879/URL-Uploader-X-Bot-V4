import os
from telegram import Update
from telegram.ext import ContextTypes

async def handle_rename(update: Update, context: ContextTypes.DEFAULT_TYPE):
    old = context.user_data.get("old_filename")
    new = update.message.text.strip()
    os.rename(old, new)
    await update.message.reply_document(document=open(new, "rb"))
    os.remove(new)