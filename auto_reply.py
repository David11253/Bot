from telethon import TelegramClient, events

api_id = 29266838 # замени на своё
api_hash = '682fed56429bcc3db215c0ee7e34ec2d'  # замени на своё

client = TelegramClient('auto_session', api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.is_private:  # только личные сообщения
        await event.reply("Привет! Это автоответчик, я отвечаю всем автоматически 😊")

client.start()
print("Бот запущен и ждёт сообщений...")
client.run_until_disconnected()

