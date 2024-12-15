from telegram import Bot
from telegram.ext import Application, CommandHandler

# توکن ربات تلگرام خود را وارد کنید
TOKEN = 'your-telegram-bot-token'

def start(update, context):
    update.message.reply_text("Welcome to SvM Panel!")

# ساخت و راه‌اندازی ربات تلگرام
application = Application.builder().token(TOKEN).build()

# ثبت فرمان start
application.add_handler(CommandHandler('start', start))

# راه‌اندازی ربات
application.run_polling()
