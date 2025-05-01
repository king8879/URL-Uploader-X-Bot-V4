from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from utils.user_settings import get_user_settings, update_user_settings

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    settings = get_user_settings(user_id)
    keyboard = [
        [InlineKeyboardButton("🖼️ See thumbnail", callback_data='see_thumb')],
        [InlineKeyboardButton("🧨 Spoiler effect: " + ("ON" if settings.get("spoiler") else "OFF"), callback_data='toggle_spoiler')],
        [InlineKeyboardButton("📤 Upload as Document: " + ("ON" if settings.get("upload_as_doc", True) else "OFF"), callback_data='toggle_upload_type')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("⚙️ Settings", reply_markup=reply_markup)

async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    settings = get_user_settings(user_id)

    if data == "toggle_spoiler":
        settings["spoiler"] = not settings.get("spoiler", False)
    elif data == "toggle_upload_type":
        settings["upload_as_doc"] = not settings.get("upload_as_doc", True)

    update_user_settings(user_id, settings)
    await query.answer("Updated!")
    await settings(query, context)