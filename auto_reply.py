from telethon import TelegramClient, events
import os

api_id = 29266838  # замените на ваш api_id
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'  # замените на ваш api_hash
bot_token = '5910548947:AAE_7SOKfS_yU8CXPgsD8ClkWl4YSj-kGAs'  # замените на токен вашего бота

# Удаление старой сессии, если она существует
session_file = "auto_session.session"
if os.path.exists(session_file):
    os.remove(session_file)

# Используем токен бота для подключения
client = TelegramClient(session_file, api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage)
async def handler(event):
    # Проверка, является ли отправитель сообщением ботом
    if not event.sender.bot:  # Проверка, что это не бот
        print(f"Получено сообщение от пользователя: {event.sender_id}")

        # Ответить на сообщение
        await event.reply("Привет, я бот и готов помочь!")

async def main():
    print("Бот успешно авторизовался и теперь будет отвечать на сообщения, кроме ботов!")

# Запуск бота и выполнение действия
with client:
    client.loop.run_until_complete(main())
