import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "I'm alive! 🤖 Send me a message."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n/start - Start the bot\n/help - Show this help"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"You said: {update.message.text}"
    )


TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
