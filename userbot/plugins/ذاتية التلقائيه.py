from userbot import iqthon
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
import os
from userbot import *
#by reda @jepthon

@iqthon.on(admin_cmd(pattern="(الذاتية تشغيل|ذاتية تشغيل)"))
async def reda(event):
    if gvarstatus ("savepicforme"):
        return await edit_delete(event, "**᯽︙حفظ الذاتيات مفعل وليس بحاجة للتفعيل مجدداً **")
    else:
        addgvar("savepicforme", "reda")
        await edit_delete(event, "**᯽︙تم تفعيل ميزة حفظ الذاتيات بنجاح ✓**")
 
@iqthon.on(admin_cmd(pattern="(الذاتية تعطيل|ذاتية تعطيل)"))
async def Reda_Is_Here(event):
    if gvarstatus ("savepicforme"):
        delgvar("savepicforme")
        return await edit_delete(event, "**᯽︙تم تعطيل حفظت الذاتيات بنجاح ✓**")
    else:
        await edit_delete(event, "**᯽︙انت لم تفعل حفظ الذاتيات لتعطيلها!**")


@iqthon.on(incoming=True)
async def reda(event):
    if gvarstatus ("savepicforme"):
        if event.is_private:
            if event.media and event.media_unread:
                pic = await event.download_media()
                await bot.send_file(
                "me",
                pic,
                caption=f"""
                - تـم حفظ الصـورة بنجـاح ✓ 
                - غير مبري الذمه اذا استخدمت الامر للابتزاز
                - CH: @tipthon
                - Dev: @M_H_N
                """,
                )
                os.remove(pic)
