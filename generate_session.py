"""
A small script to generate telethon session string
"""

from telethon import TelegramClient
from telethon.sessions import StringSession


async def send_session_string(client):
    session = StringSession.save(client.session)
    print(
        "\nDone your session string will be saved in your saved messages! Don't Share it with anyone else."
    )
    await client.send_message(
        "me",
        f"Your session String :\n\n`{session}`\n\nBy @sktechhub | [SkTechHub Product](https://t.me/sktechhub)",
    )


try:
    print(
        "Make sure you have API Client ID and Hash , If not goto my.telegram.org and generate it.\n\n"
    )
    API_ID = input("Enter Your API ID -  ")
    API_HASH = input("Enter Your API HASH -  ")

    print(
        "\n\nNow it will ask you to enter your phone number(in international format) and then follow the steps"
    )

    client = TelegramClient(StringSession(""), API_ID, API_HASH).start()

    client.loop.run_until_complete(send_session_string(client))


except Exception as ex:
    print(f"\nSome error occurred : {ex}")
