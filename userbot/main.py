# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Golden UserBot 

""" UserBot başlangıç nöktəsi """
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

DIZCILIK_STR = [
    "Stikerdən nifrət edirəm...",
     "Yaşasın diz çökək...",
     "Bu stikeri öz paketimə dəvət edirəm...",
     "Mən bunu rişxənd etməliyəm..."
     "Hey, bu gözəl stikerdir!\nMən dərhal sidiyirəm..",
     "Stikerinizə nifrət edirəm\nhahaha.",
     "Hey bax oraya. (☉｡☉)!→\nMən bunu satarkən...",
     "Qızılgüllər qırmızıdır, bənövşələr mavidir, bu stikeri paketimə yapışdırsam sərin olaram...",
     "Stiker həbsdədir...",
      "Cənab zarafatcıl bu stikeri sızıldadır",
]

AFKSTR = [
    "Mən indi tələsirəm, sonra mənə yaza bilərsən? Onsuz da yenə gələcəm.",
    "Zəng etdiyiniz şəxs hazırda telefona cavab verə bilmir. Tondan sonra mesajınızı öz tarifinizdə qoya bilərsiniz. Mesajın qiyməti 49 qəpikdir. \n`biiiiiiiiiiiiiiiiiiiiiiiiiiiiip`!",
    "Bir neçə dəqiqəyə qayıdacağam. Amma etməsəm... bir az daha gözləyin.",
    "Hazırda burada deyiləm, yəqin ki, başqa yerdəyəm.",
    "Qızılgüllər qırmızıdır\nBənövşələr mavidir\nMənə mesaj buraxın\nMən sizə qayıdacağam.",
    "Bəzən həyatda ən yaxşı şeylər gözləməyə dəyər...\nMən tezliklə qayıdacağam.",
    "Mən tezliklə qayıdacağam, amma qayıtmasam, daha sonra qayıdacağam.",
    "Hələ başa düşmürsənsə,\nMən burada deyiləm.",
    "Salam, uzaq mesajıma xoş gəldin, bu gün səni necə görməməzliyə vura bilərəm?",
    "Mən 7 dəniz və 7 ölkədən,\n7 su və 7 qitədən,\n7 dağ və 7 təpədən,\n7 düzən və 7 kurqandan,\n7 hovuz və 7 göldən,\n7 bulaqdan və 7 çəmənlikdən,\n7 şəhərdən və 7 məhəllə, \n7 məhəllə və 7 ev...\n\nMənə mesajların belə çata bilməyəcəyi yer!",
    "Hazırda klaviaturadan uzaqdayam, amma ekranda kifayət qədər yüksək səslə qışqırsan, səni eşidirəm.",
    "Mən aşağıdakı istiqamətdə hərəkət edirəm\n---->",
    "Mən bu istiqamətdə gedirəm\n<----",
    "Lütfən, bir mesaj buraxın və məni artıq olduğumdan daha vacib hiss etdirin.",
    "Sahibim burada deyil, mənə mesaj yazmağı dayandırın.",
    "Burada olsaydım\nSənə harda olduğumu deyərdim.\n\nAmma mən deyiləm,\ngeri qayıdanda soruş...",
    "Mən uzaqdayam!\nBilmirəm nə vaxt qayıdacağam!\nİnşallah bir neçə dəqiqəyə!",
    "Sahibim hazırda müsait deyil. Adınızı, nömrənizi və ünvanınızı bildirsəniz, mən onu ona verə bilərəm ki, qayıdanda.",
    "Bağışlayın, ustadım burada deyil.\nO gələnə qədər mənimlə danışa bilərsiniz.\nAğam daha sonra sizinlə əlaqə saxlayacaq.",
    "Məhz edirəm ki, bir mesaj gözləyirdin!",
    "Həyat çox qısadır, görüləsi çox şey var...\nMən onlardan birini edirəm...",
    "Hal-hazırda burada deyiləm....\n amma olsam ...\n\nbu əla olmazdımı?",
]

UNAPPROVED_MSG = ("`Hey,` {mention}`! Bu botdur. Narahat olma.\n\n`"
                  "`Sahibim sənə pm göndərməyə icazə vermədi. `"
                  "`Xahiş edirəm sahibimin aktiv olmasını gözləyin, o, adətən PM-ləri təsdiqləyir.\n\n`"
                  "`Bildiyimə görə baş nazirdən dəlilərə icazə vermir.`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nHATA: Daxil edilən telefon nömrəsi yanlışdır' \
             '\n  Ipucu: Ölkə kodundan istifadə edərək nömrənizi daxil edin' \
             '\n       Telefon nömrənizi yenidən yoxlayın'

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
                CmdHelp.add_command(Komut, None, 'Bu plugin xaricdən yüklənir. Təsvir müəyyən edilməyib.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    goldenbl = requests.get('https://gitlab.com/Emin-ahmedoff/gold/-/raw/main/golden.json').json()
    if idim in goldenbl:
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
    ORJ_PLUGIN_MESAJLAR = {"alive": "`Byy Sahibim Məni çağirdin.? Narahat olma 🪙 GoldenUserBot İşləyir.`", "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`sağol mən gedirəm `🤠", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, qadağan edildi!`", "mute": "{mention}`, səssizə alındı!`", "approve": "{mention}`, mənə mesaj göndərə bilərsiniz!`", "disapprove": "{mention}`, daha mənə mesaj göndərə bilməzsən!`", "block": "{mention}`, siz bloklanmısınız!`"}

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
        LOGS.info("Pluginler Yüklənir")
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
                    LOGS.info("Bu Plugin Artıq Quraşdırılıb " + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Quraşdırma uğursuz oldu! Plugin nasazdır.\n\nHata: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Lütfən, pluginlərin daimi olduğundan əmin olun. PLUGIN_CHANNEL_ID'i təyin edin.`")
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

LOGS.info("Botunuz işləyir! İstənilən söhbətdə .alive yazaraq onu yoxlayın."
           "Köməyə ehtiyacınız varsa, Dəstək qrupumuza gəlin t.me/GoldenSupport")
LOGS.info(f"Bot sürümünüz: Golden {GOLDEN_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
