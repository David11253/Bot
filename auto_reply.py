import os
from telethon import TelegramClient, events

# Получаем api_id и api_hash из переменных окружения
api_id = int(os.getenv('29266838'))  # Преобразуем в int, так как api_id должен быть числом
api_hash = os.getenv('682fed56429bcc3db215c0ee7e34ec2d')  # api_hash остается строкой

client = TelegramClient('auto_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:  # только личные сообщения
        await event.reply("Привет! Я сейчас занят, отвечу позже :)")

client.start()
print("🤖 Автоответчик запущен. Ожидает сообщений...")
client.run_until_disconnected()

