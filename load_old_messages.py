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

async def main():
    if chat_id == -1 or fwd_chat_id == -1:
        print("\nERROR: you must set chat_id and fwd_chat_id.\n")
        print("channel ids in your account: \n")
        # retrieve the id of the channel you're mirroring 
        # from the output and set it at the top of the script.
        async for dialog in client.iter_dialogs():
            print('{0:15} {1}'.format(dialog.id, dialog.name))
        exit(1)

    # load the mirror chat with all previous messages
    messages = client.iter_messages(chat_id)
    async for message in reversed(messages):
        if type(message) is Message:
            await client.send_message(fwd_chat_id, message)
    print("messages mirrored into channel.")

with TelegramClient('tg', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
