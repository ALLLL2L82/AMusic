"""
- 𝗕𝗬 : @O_U_Q1
- 𝗖𝗛 : @O_U_QA
- Copyright (©️) 2024-5-5 ABO SAQR
"""

from ZeMusic import app
from pyrogram import filters


@app.on_message(filters.command("ايدي", "id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
