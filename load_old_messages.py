from telethon import TelegramClient, events, errors
from telethon.tl.patched import Message
import sys
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Use your own values from my.telegram.org
api_id = 00000000
api_hash = 'use your own hash'

# use your own chat ids
chat_id = -1
fwd_chat_id = -1

async def main():
    # Getting information about yourself
    me = await client.get_me()
    print(me.stringify())

    # You can print all the dialogs/conversations that you are part of.
    # Retrieve the id of the channel you're mirroring 
    # and set it at the top of the script.
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    # stop here if chat_id and fwd_chat_id are not set
    if chat_id == -1 or fwd_chat_id == -1:
        print("please set chat_id and fwd_chat_id")
        exit(1)

    # load the mirror chat with all previous messages
    messages = client.iter_messages(chat_id)
    async for message in reversed(messages):
        if type(message) is Message:
            await client.send_message(fwd_chat_id, message)

with TelegramClient('tg', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
