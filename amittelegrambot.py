from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('שלום!')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # בודק אם המילה "עמית" מופיעה בהודעה
    if "עמית" in update.message.text:
        response = "שלום אני הבוט של עמית, הוא עסוק כרגע אני אעביר לו את ההודעה והוא ישיב בהקדם, תודה והמשך יום טוב! :)"
        await update.message.reply_text(response)

def main():
    application = ApplicationBuilder().token("6998805989:AAGeXzmy8B1EZ2R44b9VNGA0dK9NgNVoWpw").build()

    # הוסף את הפקודה start
    application.add_handler(CommandHandler("start", start))

    # הוסף את ה-handler להודעות טקסט ובדיקה אם הן מכילות את המילה "עמית"
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # הפעל את הבוט
    application.run_polling()

if __name__ == '__main__':
    main()
