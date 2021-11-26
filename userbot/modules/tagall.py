# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Gold UserBot 

import random
import asyncio
from userbot.events import register
from userbot import CMD_HELP, bot
from userbot import GOLDEN_VERSION
from telethon.tl.types import ChannelParticipantsAdmins as cp
from time import sleep
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.all(?: |$)(.*)")
async def _(q):
	if q.fwd_from:
		return

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(4)

@register(outgoing=True, pattern="^.toplutag$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()


@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(q):
	if q.fwd_from:
		return
	

	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if a_ == 5000:
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		sleep(4)



emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


class FlagContainer:
    is_active = False



@register(outgoing=True, pattern="^.emojitag.*")
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
   
@register(outgoing=True, pattern="^.stoptag")
async def m_fb(event):
  if event.fwd_from or not FlagContainer.is_active:
        return
await event.delete()
    FlagContainer.is_active = False

class FlagContainer:
    is_active = False


status = (
"Həyatda ən gözəl xoşbəxtlik, sevildiyindən əmin olmaqdır.",
"Ürəyi gözəl olanın, qisməti də gözəl olar.",
"Mənə baxıb niyə gülürsən? Güldüyüm başıma gəlsin deyə.",
"Vardır əlbət, hər kəsi  gecələr darıxdığı birisi.",
"Ayağına batan tikanlar, axtardığın güllərdən xəbər verir.",
"Başladığın cümləni özün bitirməsən, bir başqası gəlib nöqtəni qoyar.",
"Sirrini küləyə açırsansa, küləyi, sənin sirrini açdığına görə günahlandırmamalısan.",
"Həddini bilmədikdən sonra, çox şey bilmək mənasızdır. Susqunluq heç kimi çaşdırmasın, çünki susan danışsa dözən olmaz.",
"Heç kimi gözündə kiçiltmə! Gün gələr , gözündə kiçik gördüyün hər şey üçün böyük bədəllər ödəyərsən.",
"Hər zaman doğrunu söylə; nə dediyini xatırlamaq məcburiyyətində qalmarsan",
"Sevəcək qədər gözəl olmaqdansa, güvəniləcək qədər qeyrətli ol!",
"Xatirə keçmişin həqiqəti, ümid isə gələcəyin xəyalıdır.",
"Səni həyatının sonunadək qınayacaqlar. Ona görə də istədiyin kimi yaşa…",
"O qədərini də etməz deyə düşündüyüm hər kəs, tam olaraq da o qədərini etdi",
"Dürüst olmadıqca itirə-itirə gedəcəksiniz. Hər gün bir şeyinizi, bir gün hər şeyinizi!",
"Bəzilərinə sadəcə bunu demək istəyirəm: Bağışlayın səhv tanımışam.",
"Yazması belə çətin olan şeyləri yaşamaq var bir də.. Bilmirsiz!",
"Məsafə yaxşıdır: Nə həddini aşan var, nə də ki canını sıxan.",
"Mən keçmişimi bükdüm və qaldırıb zibilə atdım, bu zibilləri isə ancaq; pişiklər və itlər qarışdırar!",
"Tanrı sənə nəsə bir hədiyyə göndərəndə onu bir problemə bükür. Və problem nə qədər böyükdürsə içindəki hədiyyə də o qədər böyükdür..",
"Mənzərə nə qədər gözəl olsa da, sizə zərər verən pəncərələri bağlayın.",
"Heç kim sizi dəyərsiz hiss etdirə bilməz siz icazə vermədikcə.",
"Yaxşılıq etməyə davam et. Qarşındakı o yaxşılığa layiq olmasa belə, sən bu yaxşılığa layiqsən.",
"Ümidin olduğu yerdə, möcüzələr çiçək açar.",
"Xeyirlisi deyə bir söz var. Bütün Aminlər, Bütün inşAllahlar, bütün dualar onun içində."
)

@register(outgoing=True, pattern="^.statustag.*")
async def kfrtag(event):
      if event.fwd_from or FlagContainer.is_active:
          return
      try:
          FlagContainer.is_active = True
  
          sozcm = None
          jokisback = event.message.text.split(" ", 1)
          if len(jokisback) > 1:
              sozcm = jokisback[1]
  
          chat = await event.get_input_chat()
          await event.delete()
  
          tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", await event.client.get_participants(chat)))
          current_pack = []
          async for participant in event.client.iter_participants(chat):
              if not FlagContainer.is_active:
                  break
  
              current_pack.append(participant)
  
              if len(current_pack) == 1: 
                  tags = list(map(lambda m: f"[{random.choice(status)}](tg://user?id={m.id})", current_pack))
                  current_pack = []
  
                  if sozcm:
                      tags.append(sozcm)
  
                  await event.client.send_message(event.chat_id, " ".join(tags))
                  await asyncio.sleep(1.5) 
      finally:
          FlagContainer.is_active = False

CmdHelp("tagall").add_command(
	"all", "<sebep>", "Qrupdakı Userleri Tək-Tək Tağ edər."
).add_command(
	"alladmin", "<sebep>", "Qrupdakı Adminləri Tək-Tək Tağ edər."
).add_command(
	"emojitag", "<sebep>", "Qrupdakı Userləri Emojili Bir Şəkilde Tağ edər."
).add_command(
	"statustag",  "Qrupdakı Userləri Emojili Bir Şəkilde Tağ edər."
).add_command(
    "stoptag", None, "Emojili və Statuslu Tağı dayandirar."
).add()
