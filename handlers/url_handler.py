import os
from telegram import Update
from telegram.ext import ContextTypes
from utils.file_downloader import download_file_from_url
from utils.user_settings import get_user_settings

async def handle_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()
    filename = url.split("/")[-1] or "file"
    user_id = update.message.from_user.id
    settings = get_user_settings(user_id)
    try:
        await update.message.reply_text("Downloading...")
        download_file_from_url(url, filename)
        context.user_data["old_filename"] = filename

        if settings.get("upload_as_doc", True):
            await update.message.reply_text(f"Downloaded `{filename}`. Send new filename with extension or /skip to upload as-is.")
        else:
            await update.message.reply_video(video=open(filename, "rb"))
            os.remove(filename)
    except Exception as e:
        await update.message.reply_text(f"Failed: {str(e)}")