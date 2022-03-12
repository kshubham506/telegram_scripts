"""
A script to scrap members from groups/channels
"""


import asyncio
import time

import pandas
from telethon import TelegramClient
import re
from telethon.sessions import StringSession
from telethon import functions, types


"""
Enter details for the below four variables
"""
SESSION_ID = "<ENTER_YOUR_SESSION_HERE>"  # check README.md for this
API_ID = "<ENTER_API_ID_HERE>"
API_HASH = "<ENTER_API_HASH_HERE>"
CHANNEL_TO_SCRAP = []  # entity id goes here , can be more than one type is integer


async def start():
    client = TelegramClient(StringSession(SESSION_ID), int(API_ID), API_HASH)

    await client.connect()

    scrapChannels = []

    async for d in client.iter_dialogs():
        if d.entity.id in CHANNEL_TO_SCRAP:
            scrapChannels.append(d)

    print(f"SCaping from {len(scrapChannels)} channels")

    async def dump_all_users(channel):
        print(f"\n\nDumping users from chanel : {channel.name}")
        queryKey = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        all_participants = []
        error = ""
        for key in queryKey:
            offset = 0
            limit = 100
            while True:
                try:
                    participants = await client(
                        functions.channels.GetParticipantsRequest(
                            channel,
                            types.ChannelParticipantsSearch(key),
                            offset,
                            limit,
                            hash=0,
                        )
                    )
                    if not participants.users:
                        break
                    for user in participants.users:
                        try:
                            if (
                                re.findall(r"\b[a-zA-Z]", user.first_name)[0].lower()
                                == key
                            ):
                                all_participants.append(user)

                        except:
                            pass

                    offset += len(participants.users)
                    print(f"Found {len(all_participants)} users")
                except Exception as ex:
                    print("Error as ", ex)
                    break

        print("Total Members Scrapped: ", len(all_participants))

        to_write_data = [["first_name", "last_name", "username", "userid", "phone"]]
        for user in all_participants:
            to_write_data.append(
                [user.first_name, user.last_name, user.username, user.id, user.phone]
            )

        print("Writing to file.... ", channel.name)
        filename = f"{channel.name}_{str(int(time.time()))}.csv"
        try:
            pd = pandas.DataFrame(to_write_data)
            pd.to_csv(filename)
        except Exception as ex:
            print("Error while writing to file", ex)
        print("....Done writing to file ", filename)

    for channel in scrapChannels:
        await dump_all_users(channel)

    await client.disconnect()


if __name__ == "__main__":

    asyncio.run(start())
