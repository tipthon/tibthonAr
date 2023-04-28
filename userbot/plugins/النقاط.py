from userbot import iqthon
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
import asyncio
from telethon import events
c = requests.session()
bot_username = '@zmmbot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
HuRe = ['yes']


@iqthon.on(admin_cmd(pattern="(تجميع المليار|تجميع مليار)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await iqthon.get_entity(bot_username)
        await iqthon.send_message('@zmmbot', '/start')
        await asyncio.sleep(3)
        msg0 = await iqthon.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await iqthon.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(1)

            list = await iqthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await iqthon.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await iqthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await iqthon(ImportChatInviteRequest(bott))
                msg2 = await iqthon.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await iqthon.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await iqthon.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await iqthon.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@iqthon.on(admin_cmd(pattern="(تجميع الجوكر|تجميع جوكر)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت الجوكر , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await iqthon.get_entity(bot_username2)
        await iqthon.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(2)
        msg0 = await iqthon.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await iqthon.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await iqthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await iqthon.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await iqthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await iqthon(ImportChatInviteRequest(bott))
                msg2 = await iqthon.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await iqthon.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await iqthon.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await iqthon.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@iqthon.on(admin_cmd(pattern="(تجميع العقاب|تجميع عقاب)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await iqthon.get_entity(bot_username3)
        await iqthon.send_message('@MARKTEBOT', '/start')
        await asyncio.sleep(3)
        msg0 = await iqthon.get_messages('@MARKTEBOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(3)
        msg1 = await iqthon.get_messages('@MARKTEBOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(3)

            list = await iqthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await iqthon.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await iqthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await iqthon(ImportChatInviteRequest(bott))
                msg2 = await iqthon.get_messages('@MARKTEBOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await iqthon.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await iqthon.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await iqthon.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
@iqthon.on(admin_cmd(pattern="(تجميع المليون|تجميع مليون)"))
async def _(event):
    if HuRe[0] == "yes":
        await event.edit("**᯽︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بلانظمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
        channel_entity = await iqthon.get_entity(bot_username4)
        await iqthon.send_message('@qweqwe1919bot', '/start')
        await asyncio.sleep(2)
        msg0 = await iqthon.get_messages('@qweqwe1919bot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(2)
        msg1 = await iqthon.get_messages('@qweqwe1919bot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            if HuRe[0] == 'no':
                break
            await asyncio.sleep(2)

            list = await iqthon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await iqthon.send_message(event.chat_id, f"**لاتوجد قنوات للبوت**")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await iqthon(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await l313l(ImportChatInviteRequest(bott))
                msg2 = await iqthon.get_messages('@qweqwe1919bot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await iqthon.send_message("me", f"تم الاشتراك في {chs} قناة")
            except:
                await iqthon.send_message(event.chat_id, f"**خطأ , ممكن تبندت**")
                break
        await iqthon.send_message(event.chat_id, "**تم الانتهاء من التجميع !**")

    else:
        await event.edit("يجب الدفع لاستعمال هذا الامر !")
