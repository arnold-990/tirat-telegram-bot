import logging
from aiogram import Bot, Dispatcher, types, executor
import os

# Вставь свой токен сюда
API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["📰 שלח חדשות", "📢 פרסום עסק", "💬 צור קשר"]
    keyboard.add(*buttons)
    await message.answer("ברוכים הבאים לבוט החדשות של טירת כרמל!", reply_markup=keyboard)

# Обработка кнопок
@dp.message_handler(lambda message: message.text == "📰 שלח חדשות")
async def handle_news(message: types.Message):
    await message.answer("✉️ אתם יכולים לשלוח כאן חדשות, והמערכת תבדוק אותן לפני הפרסום.")

@dp.message_handler(lambda message: message.text == "📢 פרסום עסק")
async def handle_ads(message: types.Message):
    await message.answer("🔔 לפרסום העסק שלך, שלח את כל הפרטים כאן ונחזור אליך בהקדם.")

@dp.message_handler(lambda message: message.text == "💬 צור קשר")
async def handle_contact(message: types.Message):
    await message.answer("📞 צור קשר עם המערכת כאן או שלח מייל ל: contact@example.com")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

