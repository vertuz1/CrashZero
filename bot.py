import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎰 Добро пожаловать в CrashBot!\n"
        "Команды:\n"
        "/predict — Получить прогноз коэффициента\n"
        "/settings — Настройки (в разработке)"
    )

async def predict(update: Update, context: ContextTypes.DEFAULT_TYPE):
    predicted_x = round(random.uniform(1.5, 10.0), 2)
    await update.message.reply_text(f"🧠 Прогнозируемый коэффициент: x{predicted_x}")

if __name__ == '__main__':
    app = ApplicationBuilder().token("ВАШ_ТОКЕН_ОТ_BOTFATHER").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("predict", predict))

    print("Бот запущен...")
    app.run_polling()
