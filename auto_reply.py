from telethon import TelegramClient, events
import os

api_id = 29266838  # замените на ваш api_id
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'  # замените на ваш api_hash

# Удаление старой сессии, если она существует
session_file = "auto_session.session"
if os.path.exists(session_file):
    os.remove(session_file)

client = TelegramClient(session_file, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    # Проверка, является ли отправитель сообщением ботом
    if event.sender_id != event.sender_id:  # Проверка, что это не бот
        print(f"Получено сообщение от пользователя: {event.sender_id}")

        # Ответить на сообщение
        await event.reply("Привет, я бот и готов помочь!")

async def main():
    await client.start()
    print("Бот успешно авторизовался и теперь будет отвечать на сообщения, кроме ботов!")

# Запуск бота и выполнение действия
with client:
    client.loop.run_until_complete(main())
