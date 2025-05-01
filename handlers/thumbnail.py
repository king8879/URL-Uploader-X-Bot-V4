from telegram import Update
from telegram.ext import ContextTypes
from utils.user_settings import get_user_settings, update_user_settings

async def save_thumbnail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    photo = update.message.photo[-1]
    file_id = photo.file_id

    settings = get_user_settings(user_id)
    settings["thumbnail"] = file_id
    update_user_settings(user_id, settings)

    await update.message.reply_text("✅ Thumbnail saved!")