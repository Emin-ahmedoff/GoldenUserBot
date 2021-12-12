# Copyright (C) 2021 CyberUserBot
# This file is a part of < https://github.com/FaridDadashzade/CyberUserBot/ >
# Please read the GNU General Public License v3.0 in
# <https://www.github.com/FaridDadashzade/CyberUserBot/blob/master/LICENSE/>.

import time
import heroku3
import asyncio
import aiohttp
import ssl
import requests
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which
from os import remove
from userbot import (
    GOLDEN_VERSION,
    WHITELIST,
    MYID,
    bot
)
from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from userbot.main import PLUGIN_MESAJLAR
from userbot import HEROKU_APPNAME, HEROKU_APIKEY, BOTLOG_CHATID, BOTLOG


# ---------------------------------- #
from userbot.language import get_value
LANG = get_value("goldenlangs")
# ---------------------------------- #

LOGO_ALIVE = PLUGIN_MESAJLAR['salive']
CYBER_NAME = f"[{DEFAULT_NAME}](tg://user?id={SAHIB_ID})"

heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["saniyə", "dəqiqə", "saat", "gün"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ", ".join(time_list)

    return up_time


"""
@register(cyber=True, pattern="^.resalive (.*)")
async def salive_lang(event):
    cyber_logo = event.pattern_match.group(1)
    cyber_config = ALIVE_LOGO
    if cyber_logo == '':
        await event.edit("`Xahiş edirəm bir logo linki qeyd edin!`")
        return False
    if cyber_config in heroku_var:
        await event.edit("`Hazırlanır..\n(Biraz gözləyin)`")
        del heroku_var[cyber_config]
        return False
        heroku_var[cyber_config] = cyber_logo
"""

@register(outgoing=True, disable_errors=True, pattern=r"^\.salive(?: |$)(.*)")
async def salive(alive):
    user = await bot.get_me()
    islememuddeti = await get_readable_time((time.time() - StartTime))
    kecid = (
        f"**{ALIVE_TEXT}** \n"
        f"┏━━━━━━━━━━━━━━━━━━━━━━\n"
        f"┣[ 🧭 **Botun işləmə müddəti:** `{islememuddeti}`\n"
        f"┣[ 👤 **Mənim sahibim:** `{user.first_name}`\n"
        f"┣[ 🐍 **Python:** `3.8.6`\n"                               
        f"┣[ ⚙️ **Telethon:** `1.23.0`\n"
        f"┣[ 🛡 **Plugin sayı:** `{len(CMD_HELP)}`\n"
        f"┣[ 👁‍🗨 **İstifadəçi adı:** @{user.username}\n"
        f"┣[ 🗄 **Branch:** `Master`\n"
        f"┗━━━━━━━━━━━━━━━━━━━━━━\n"
        f"**C Y B Ξ R Version:** `{CYBER_VERSION}`"
    )
    if LOGO_ALIVE:
        try:
            logo = LOGO_ALIVE
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=kecid)
            await asyncio.sleep(100)
            await msg.delete()
        except BaseException:
            await alive.edit(
                kecid + "\n\n *`Təqdim olunan logo etibarsızdır."
                "\nKeçidin logo şəklinə yönəldiyindən əmin olun`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(kecid)
        await asyncio.sleep(100)
        await alive.delete()    
        
        
@register(incoming=True, from_users=SUPPORT, disable_errors=True, pattern="^.wlive$")
@register(incoming=True, from_users=JARVIS, disable_errors=True, pattern="^.alive$")
async def asistanalive(jarvis):
    if ups.fwd_from:
        return
    if ups.is_reply:
        reply = await jarvis.get_reply_message()
        replytext = reply.text
        reply_user = await jarvis.client.get_entity(reply.from_id)
        ren = reply_user.id
        if jarvis.sender_id == 1955246281:
            xitab = GOLDEN_NAME
        else:
            xitab = GOLDEN_NAME
        if ren == MYID:
            Version = str(GOLDEN_VERSION.replace("v","")) 
            await ups.reply(f"**{GOLDEN_NAME} C Y B Ξ R işlədir...**\n**C Y B Ξ R:** `{CYBER_VERSION}`")
        else:
            return
    else:
        return 


Help = CmdHelp('salive')
Help.add_command('salive', None, 'Gif-li alive mesajı.', 'salive')
Help.add_command('change salive', '<media/link>', 'Logo dəyişdirər.', 'change salive')
Help.add()
