# 🍀 © @tofik_dn
# ⚠️ Do not remove credits
# 👀 recode by @TeleUdahRusak

"""
✘ Commands Available -
• `{i}sange`
   To send random intake video.
• `{i}ange`
   To send a random wibu video.
"""

import requests

from . import *

@ultroid_cmd(pattern="sange ?(.*)")
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
        await event.edit("Tidak bisa menemukan video video.")


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
        await event.edit("Tidak bisa menemukan video video.")
