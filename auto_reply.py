import os
from telethon import TelegramClient, events

# Получаем значения из переменных окружения
api_id = 29266838
api_hash = "682fed56429bcc3db215c0ee7e34ec2d"

client = TelegramClient('auto_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:
        await event.reply("Привет! Я сейчас занят, отвечу позже :)")

client.start()
print("🤖 Автоответчик запущен. Ожидает сообщений...")
client.run_until_disconnected()
