from telethon import TelegramClient, events, errors
from telethon.tl.patched import Message
import sys
import logging
import yaml

config = yaml.safe_load(open("config.yml"))

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)

api_id = config["telegram"]["api_id"]
api_hash = config["telegram"]["api_hash"]
chat_id = config["telegram"]["src_chat_id"] 
fwd_chat_id = config["telegram"]["fwd_chat_id"]

with TelegramClient('tg', api_id, api_hash, sequential_updates=True) as client:

    @client.on(events.NewMessage(chats=[chat_id]))
    async def callback(event):
        print(event)
        await client.send_message(fwd_chat_id, event.message)
    
    print("listening for new messages...")
    client.start() 
    client.run_until_disconnected()
