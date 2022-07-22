"""
A script to respond to private messages
"""


import time
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import json

"""
Enter details for the below four variables
"""
SESSION_ID = "<ENTER_YOUR_SESSION_HERE>"  # check README.md for this
API_ID = "<ENTER_API_ID_HERE>"
API_HASH = "<ENTER_API_HASH_HERE>"
MESSAGE = "TESTING"  # message to send goes here
RESPONDED_USERS = {}


def start():
    client = TelegramClient(StringSession(SESSION_ID), int(API_ID), API_HASH).start()

    @client.on(events.NewMessage(incoming=True))
    async def my_event_handler(event):
        if event.is_private is True:
            if event.chat_id not in RESPONDED_USERS:
                await event.respond(MESSAGE)
                RESPONDED_USERS[event.chat_id] = time.time()
                print(
                    f"[started oon 22-07-2022]responded for user {event.chat_id} at {time.time()}"
                )
                json.dump(RESPONDED_USERS, open("responded_users.json", "w+"))

    client.run_until_disconnected()


if __name__ == "__main__":

    start()
