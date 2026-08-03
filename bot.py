import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from ai import ask_ai

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بك في KingAI!\n\nاكتب أي سؤال وسأحاول مساعدتك."
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    reply = ask_ai(user_message)

    await update.message.reply_text(reply)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

print("KingAI is running...")

app.run_polling()
