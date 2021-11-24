# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Gold UserBot 

# @NaytSeyd tarafından portlanmıştır.
#

from telethon.tl.types import ChannelParticipantsAdmins
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

 import time
import requests

from collections import deque
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from userbot.cmdhelp import CmdHelp


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


class FlagContainer:
    is_active = False



@register(outgoing=True, pattern="^.jemall.*")
async def b(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        text = None
        args = event.message.text.split(" ", 1)
        if len(args) > 1:
            text = args[1]

        chat = await event.get_input_chat()
        await event.delete()

        tags = list(map(lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 5:
                tags = list(map(lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})", current_pack))
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(1.3) #floodwait 
    finally:
        FlagContainer.is_active = False
    await event.client(JoinChannelRequest("jokerpluginn"))
    await event.client(JoinChannelRequest("joksohbet"))

CmdHelp("jemall").add_command(
	"jemall", "<sebep>", "Gruptaki Üyeleri Emojili Bir Şekilde Etiketler."
).add_command(
    "kill all", None, "Etiketleme işlemini durdurur."
).add()
