from telethon.sync import TelegramClient, events

api_id = 29266838
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'

client = TelegramClient("auto_session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    if event.is_private:
        await event.respond("Привет! Я бот, который отвечает автоматически.")
        print(f"Ответил {event.sender_id}")

client.start()
print("Бот запущен.")
client.run_until_disconnected()
