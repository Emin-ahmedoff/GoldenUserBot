import codecs
import heroku3
import asyncio
import aiohttp
import math
import os
import ssl
import requests

from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    BOTLOG,
    BOTLOG_CHATID,
    ALIVE_NAME
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp

heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None


"""Config Vars dəyəri əlavə edin və ya silin."""


@register(outgoing=True, pattern=r"^.(get|del) var(?: |$)(\w*)")
async def variable(var):
    exe = var.pattern_match.group(1)
    if app is None:
        await var.edit("`[HEROKU]"
                       "\n**HEROKU_APPNAME** quraşdırın.")
        return False
    if exe == "get":
        await var.edit("`Heroku Məlumatları Gətirilir..`")
        variable = var.pattern_match.group(2)
        if variable != '':
            if variable in heroku_var:
                if BOTLOG:
                    await var.client.send_message(
                        BOTLOG_CHATID, "#CONFIGVAR\n\n"
                        "**ConfigVar**:\n"
                        f"`{variable}` = `{heroku_var[variable]}`\n"
                    )
                    await var.edit("`BOTLOG qrupuna göndərdim!`")
                    return True
                else:
                    await var.edit("`Zəhmət olmasa BOTLOG grupu təyin edin...`")
                    return False
            else:
                await var.edit("`Error ith Noİnfo`")
                return True
        else:
            configvars = heroku_var.to_dict()
            if BOTLOG:
                msg = ''
                for item in configvars:
                    msg += f"`{item}` = `{configvars[item]}`\n"
                await var.client.send_message(
                    BOTLOG_CHATID, "#CONFIGVARS\n\n"
                    "**ConfigVars**:\n"
                    f"{msg}"
                )
                await var.edit("`BOTLOG_CHATID alındı...`")
                return True
            else:
                await var.edit("`Zəhmət olmasa BOTLOG 'u True olaraq təyin edin!`")
                return False
    elif exe == "del":
        await var.edit("`Məlumatları silirəm...`")
        variable = var.pattern_match.group(2)
        if variable == '':
            await var.edit("`Silmək istədiyiniz ConfigVars'ı seçin və mənə bildirin...`")
            return False
        if variable in heroku_var:
            if BOTLOG:
                await var.client.send_message(
                    BOTLOG_CHATID, "#DELCONFIGVAR\n\n"
                    "**ConfigVar Silindi**:\n"
                    f"`{variable}`"
                )
            await var.edit("`Məlumatlar silindi!`")
            del heroku_var[variable]
        else:
            await var.edit("`Məlumatlar yoxdu!`")
            return True


@register(outgoing=True, pattern=r'^.set var (\w*) ([\s\S]*)')
async def set_var(var):
    await var.edit("`Verilənlər Herokuya Yazılır...`")
    variable = var.pattern_match.group(1)
    value = var.pattern_match.group(2)
    if variable in heroku_var:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#SETCONFIGVAR\n\n"
                "**ConfigVar Dəyişikliyi**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Verilənlər Herokuya Yazılır...`")
    else:
        if BOTLOG:
            await var.client.send_message(
                BOTLOG_CHATID, "#ADDCONFIGVAR\n\n"
                "**ConfigVar Əlavə**:\n"
                f"`{variable}` = `{value}`"
            )
        await var.edit("`Verilənlər əlavə edildi!`")
    heroku_var[variable] = value


"""Hesabınızdakı dynonu yoxlamağa yarayan userbot modulu"""

@register(incoming=True, husu=True, pattern=r"^Nə qədər dyno qalıb?$")
@register(outgoing=True, pattern=r"^.dyno(?: |$)")
async def dyno_usage(dyno):
    """Bu qisimdə bot istifadə edilmiş dynonu əldə etməyə çalışır"""
    await dyno.edit("`Zəhmət Olmasa Gözləyin...`")
    useragent = ('Mozilla/5.0 (Linux; Android 10; SM-G975F) '
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/80.0.3987.149 Mobile Safari/537.36'
                 )
    u_id = Heroku.account().id
    headers = {
     'User-Agent': useragent,
     'Authorization': f'Bearer {HEROKU_APIKEY}',
     'Accept': 'application/vnd.heroku+json; version=3.account-quotas',
    }
    path = "/accounts/" + u_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("`Error: something bad happened`\n\n"
                               f">.`{r.reason}`\n")
    result = r.json()
    quota = result['account_quota']
    quota_used = result['quota_used']

    """ - Used - """
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    day = math.floor(hours / 24)

    """ - Current - """
    App = result['apps']
    try:
        App[0]['quota_used']
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]['quota_used'] / 60
        AppPercentage = math.floor(App[0]['quota_used'] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)

    await asyncio.sleep(1.5)

    return await dyno.edit(
                f"☛ Dyno Məlumatı: {app.name}\n"
                f"╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                f"┣[• İstifadə olunan Dyno🥺: \n"
                f"┣[•  ▸ {AppHours} saat - {AppMinutes} dəqiqə. \n"
                f"┣[•  ▸ Faizlə: {AppPercentage}% \n"
                f"┣✠╼━━━━━━❖━━━━━━━✠\n"
                f"┣[• İstifadə edə biləcəyiniz Dyno😊: \n"
                f"┣[•  ▸ {hours} saat - {minutes} dəqiqə\n"
                f"┣[•  ▸ Faizlə : {percentage}%. \n"
                f"┣✠╼━━━━━━❖━━━━━━━✠\n"   
                f"┣[• Təxmini bitmə müddəti🤭\n"
                f"┣[• ▸ {day} gün\n"
                f"┣[• 👮Sahibim: {ALIVE_NAME} \n"
                f"╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                          )


@register(outgoing=True, pattern=r"hlogs")
async def _(dyno):
    if app is None:
        return await dyno.edit(
            "**Heroku Xətası** `HEROKU_APPNAME` **və** `HEROKU_APIKEY` **doldurun**"
        )
    await dyno.edit("**Heroku Hesabatı alınır**")
    with open("logs.txt", "w") as log:
        log.write(app.get_log())
    await dyno.client.send_file(
        entity=dyno.chat_id,
        file="logs.txt",
        thumb="userbot/log/goldenlogs.jpg",
        caption="**Bu {ALIVE_NAME}-nin Heroku Qeydidir**",
    )
    await dyno.delete()
    return os.remove("logs.txt")


CmdHelp('heroku').add_command(
'dyno', None, 'Dyno saatı haqqında məlumat verir..'
    ).add_command(
        'set var', None, 'set var <Yeni Dəyər adı> <Dəyər> Botunuza yeni ConfigVar əlavə edir.'
    ).add_command(
        'get var', None, 'Mövcud VARlarınızı əldə edin, yalnız botlog qrupunuzda istifadə edin.'
    ).add_command(
        'del var', None, 'del var <Dəyər adı> Seçdiyiniz ConfigVarı silər sildikdən sonra botunuza .restart verin.'
    ).add_command(
        'hlogs', None, 'Heroku logunuza baxın'
    ).add()
