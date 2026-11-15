import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💼 ملف منحة البطالة"],
        ["🎒 ملف المنحة المدرسية"],
        ["📄 وثائق إدارية"],
        ["ℹ️ خدمات أخرى"],
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "مرحبًا بك في بوت الخدمات الإدارية 🇩🇿\n\n"
        "اختر الخدمة التي تريد معرفة معلومات عنها:",
        reply_markup=reply_markup
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "💼 ملف منحة البطالة":
        await update.message.reply_text(
            "💼 معلومات ملف منحة البطالة\n\n"
            "سيتم إضافة الوثائق المطلوبة هنا بعد التحقق من المصادر الرسمية."
        )

    elif text == "🎒 ملف المنحة المدرسية":
        await update.message.reply_text(
            "🎒 معلومات ملف المنحة المدرسية\n\n"
            "سيتم إضافة الوثائق المطلوبة هنا بعد التحقق من المصادر الرسمية."
        )

    elif text == "📄 وثائق إدارية":
        await update.message.reply_text(
            "📄 اختر لاحقًا نوع الوثيقة الإدارية التي تريد معلومات عنها."
        )

    elif text == "ℹ️ خدمات أخرى":
        await update.message.reply_text(
            "ℹ️ سيتم إضافة خدمات إدارية أخرى قريبًا."
        )


def main():
    if not TOKEN:
        print("لم يتم العثور على BOT_TOKEN")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("البوت يعمل...")
    app.run_polling()


if __name__ == "__main__":
    main()
