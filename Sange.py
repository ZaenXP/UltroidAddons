#credit @tofik_dn



"""
âœ˜ Commands Available -
â€¢ `{i}sange`
   To send random intake video.
â€¢ `{i}ange`
   To send a random wibu video.
"""


from userbot import CMD_HELP
from userbot.utils import ultroid_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputM

import requests

from . import *

@ultroid_cmd(pattern="ange ?(.*)")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@protprotviral", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Video**.")
        
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")


@ultroid_cmd(pattern="ange ?(.*)")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@notygirl", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Bokep jangan sange kontol**.")
        
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")
