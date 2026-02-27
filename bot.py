import telebot
import random
import os
import time

# Токен будет браться из переменных окружения Railway (это безопасно!)
TOKEN = os.environ.get('TELEGRAM_TOKEN')

# Если токен не найден — ошибка
if not TOKEN:
    print("ОШИБКА: TELEGRAM_TOKEN не найден в переменных окружения!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Список любовных записок
messages = [
    "❤️ Я люблю тебя также сильно, как мы любим пить пиво в пятницу вечером",
    "🌸 Ты прекрасна, как первый весенний цветок",
    "💃 С тобой даже понедельник feels like пятница",
    "😺 Я люблю тебя больше, чем котики любят спать",
    "☕ Ты — мое утро, мой кофе и мое счастье",
    "💕 Спасибо, что ты есть. Серьезно, каждый день спасибо",
    "☀️ Ты делаешь мою жизнь ярче, чем весеннее солнце",
    "📺 Я люблю тебя также сильно, как ты любишь смотреть сериалы до 3 ночи",
    "😊 Ты — причина моей улыбки каждый день",
    "🍕 Я люблю тебя больше, чем пиццу (а это серьезное заявление)",
    "📱 Ты — мое любимое уведомление в телефоне",
    "🎁 Ты — лучший подарок, который у меня есть",
    "🌟 Ты — мой персональный источник счастья",
    "🎉 С тобой каждый день как праздник",
    "💝 Ты — самое лучшее, что случилось в моей жизни"
]

# Команда /start
@bot.message_handler(commands=['start'])
def start_message(message):
    user_name = message.from_user.first_name
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton("💌 Скажи что-нибудь")
    markup.add(button)
    
    bot.send_message(
        message.chat.id,
        f"🌸 Привет, {user_name}!\n\n"
        "Этот бот создан специально для тебя. 💝\n"
        "Нажми на кнопку ниже, и я скажу тебе что-то очень важное.",
        reply_markup=markup
    )

# Обработка нажатия на кнопку
@bot.message_handler(func=lambda message: message.text == "💌 Скажи что-нибудь")
def send_love_message(message):
    love_message = random.choice(messages)
    bot.send_message(
        message.chat.id,
        f"✨ *Тебе записка:* ✨\n\n{love_message}",
        parse_mode='Markdown'
    )

# Обработка любых других сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton("💌 Скажи что-нибудь")
    markup.add(button)
    
    bot.send_message(
        message.chat.id,
        "Нажми на кнопку внизу, я хочу тебе что-то сказать 💌",
        reply_markup=markup
    )

# Запуск бота
print("Бот запускается...")
while True:
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
        continue
