"""Available Commands:
.konhumai
CREDITS TO @knowledge_masterr"""

from telethon import events

import asyncio

from uniborg.util import admin_cmd

{DEFAULTUSER} = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

@borg.on(admin_cmd(pattern="MY INFO"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 36)

    #input_str = event.pattern_match.group(2)

  #  if input_str == "konhumai":

    await event.edit("mai kon hu batata hoo bsdk...")

    animation_chars = [
        
                      "{DEFAULTUSER} tera pehla baap",
                      "{DEFAULTUSER} teri maa ka 100th pati",
                      "{DEFAULTUSER} tere khandaan ka owner",
                      "{DEFAULTUSER} tujhe paida krne wala",
                      "{DEFAULTUSER} tujhe chakka sabit krne wala",
                      "{DEFAULTUSER} tera bhai is duniya me laane wala",
                      "{DEFAULTUSER} teri maa ko kothe me baithane wala",
                      "{DEFAULTUSER} ke talwe tera baaap chatta hai",
                      "{DEFAULTUSER} aakhir tera baap hi to hai",
                      "{DEFAULTUSER} hoo mai",
 ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 10])
