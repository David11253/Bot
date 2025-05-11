from telethon import TelegramClient, events

# 🔐 Вставь свои данные ниже
api_id = 29266838 # сюда твой API ID
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'  # сюда твой API Hash

client = TelegramClient('auto_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:  # только личные сообщения
        await event.reply("Привет! Я сейчас занят, отвечу позже :)")

client.start()
print("🤖 Автоответчик запущен. Ожидает сообщений...")
client.run_until_disconnected()
