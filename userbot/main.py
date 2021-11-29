# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Golden Userbot

""" UserBot başlangıç noktası """
import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, GOLDEN_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

ALIVE_MSG = [
    "`GoldenUserBot'unuz İşləyəni çox oldu:` **{worktime}** ❤️",
    "🎆 `Narahat olma! Seninləyəm.` **{sirisahip}**, `userbot çalışıyor.`",
    "`⛈️ Yeni gib3i görünüyor!`, **{sirisahip}:3**",
    "✨ `Userb4ot sahibinin emirlerine hazır...`",
    "`Huh!` **{s5irisahip}** `beni çağırıyor 🍰 < bu senin için 🥺..`",
    "{mention} **Si6ri Senin İçin Çalışıyor✨**",
    "{username}, `S7iriOT {worktime} zamandır çalışıyor...`\n——————————————\n**Telethon sürümü :** `{telethon}`\n**Userbot sürümü  :** `{siri}`\n**Python sürümü    :** `{python}`\n**Plugin sayısı :** `{plugin}`\n——————————————\n**Emrine amadeyim dostum... 😇**"
]

DIZCILIK_STR = [
    "Stickeri dızlayıram...",
    "Sticker paketə əlavə edilir...",
    "Bu sticker artıq mənimdir!",
    "Bunu stickerlərimə əlavə etməliyəm... ",
    "Sticker həps edilir...",
    "Mən bir sticker oğrusuyam stickerin məndədi ;D!",
    "Nə gözəl stickerdi bu!"
]

AFKSTR = [
    "İndi burda deyiləm gələndə yazaram.",
    "Sahibim burda deyil gözlə gələndə yazar.",
    "Sahibim istirahətdədi onu narahat eləmə :)",
    "Zəng etdiyiniz şəxsə zəng çatmır, telefon ya söndürülüb yada əhatə dairəsi xaricindədir xaiş olunur daha sonra təkrar cəhd edin.",
    "Gizlenqaç oynayıram sakit durrr",
    "Bəli?",
    "Salam mən sahibimin meneceriyəm\nBuyurun istəklərinizi mənə deyə bilərsiz. Sizin üçün sahibimə çatdıraram.",
    "Hələdə anlamadınsa burda deyiləm.",
    "Salam, uzaq mesajıma xoş gəldiniz, sizə necə kömək edə bilərəm?",
    "Mən sahibimin xüsusi botuyam!, sizdə bot istəyirsizsə:",
    "Hal hazırda burdan çoox uzaqdayam.\nQışqırsan bəlkə eşitdim.",
    "Bu tərəfə gedirəm\n---->",
    "Bu tərəfə gedirəm\n<----",
    "Zəhmət olmasa mesajınızı yazın sahibim gələndə sizə cavab yazar.",
    "Sahibim burda deyil mənə yazmağı kəs artıq.",
    "Sahibim işi var onu narahat eləmə. O iş görərkən onu narahat etmək onu əsəbləşdirir:)",
    "Sahibim burda deyil. O gələnə qədər mənimlə danışa bilərsiz.",
    "Belə gözəl bir gündə niyə məni narahat edirsən?",
    "Sahibimə mesaj atmaq üçün zəhmət olmasa aşağıdakıları yazın:\nAdınız:\nSoyadınız:\nİsdifadəçi Adınız:\n\nƏgər yuxarıadakıları düzgün yazdızsa sahibim ən qısa zamanda sizə yazacaq.",
    "Hal hazırda burdayam amma mesajını görməzdən gələcəm :)",
]

UNAPPROVED_MSG = ("`Hey,` {mention}`! Bu bir bot. Narahat olma.\n\n`"
                  "`Sahibim sənə PM atma icazəsi verməyib. `"
                  "`Zəhmət olmasa sahibimin aktiv olmağını gözləyin, o adətən PM'ləri qəbul edir.\n\n`"
                  "`Bildiyim qədəri ilə o dəlilərə PM atma icazəsi vermir.`\n@GoldenUserBot")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nHATA: Girilen telefon numarası geçersiz' \
             '\n  Ipucu: Ülke kodunu kullanarak numaranı gir' \
             '\n       Telefon numaranızı tekrar kontrol edin'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []

    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)

            # GoldenPY
            Goldenpy = re.search('\"\"\"GOLDENPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Goldenpy == None:
                Goldenpy = Goldenpy.group(0)
                for Satir in Goldenpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin dışarıdan yüklenmiştir. Herhangi bir açıklama tanımlanmamıştır.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    asenabl = requests.get('https://gitlab.com/Emin-ahmedoff/gold/-/raw/main/goldenblacklist.json').json()
    if idim in asenabl:
        bot.disconnect()

    # ChromeDriver'ı Ayarlayalım #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Galeri için değerler
    GALERI = {}

    # PLUGIN MESAJLARI AYARLIYORUZ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": f"{str(choice(ALIVE_MSG))}",  "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`Güle Güle ben gidiyorum `🤠", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, yasaklandı!`", "mute": "{mention}`, sessize alındı!`", "approve": "{mention}`, bana mesaj gönderebilirsin!`", "disapprove": "{mention}`, artık bana mesaj gönderemezsin!`", "block": "{mention}`, engellendin!`"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("Pluginler Yükleniyor")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Zaten Yüklü " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Yükleme başarısız! Plugin hatalı.\n\nHata: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Lütfen pluginlerin kalıcı olması için PLUGIN_CHANNEL_ID'i ayarlayın.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Botunuz çalışıyor! Herhangi bir sohbete .alive yazarak Test edin."
          " Yardıma ihtiyacınız varsa, Destek grubumuza gelin t.me/Goldensupportaz")
LOGS.info(f"Bot sürümünüz: Golden {GOLDEN_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
