from telethon import TelegramClient, events, errors
from telethon.tl.patched import Message
import sys
import logging

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)

# use your own values from my.telegram.org
api_id = 00000000
api_hash = 'get your own hash!'

# use your own chat ids
chat_id = -1
fwd_chat_id = -1

with TelegramClient('tg', api_id, api_hash, sequential_updates=True) as client:

    @client.on(events.NewMessage(chats=[chat_id]))
    async def callback(event):
        await client.send_message(fwd_chat_id, event.message)

    client.start() 
    client.run_until_disconnected()