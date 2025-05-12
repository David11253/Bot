from telethon import TelegramClient, events

# 🔐 Твои данные (заменены на реальные)
api_id = 29266838
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'

# 👤 Имя файла сессии (ты загружаешь его сам в GitHub)
client = TelegramClient("auto_session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:
        await event.respond("Привет! Я занят!")

async def main():
    await client.start()
    print("✅ Бот запущен и ждёт сообщений...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
