from pyrogram import Client, filters
from pyrogram.types import Message

# Aapka Log Channel ID
LOG_CHANNEL = -1003166629808

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(bot: Client, message: Message):
    # Logging in small caps as requested
    log_text = (
        "ɴᴇᴡ ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ\n\n"
        f"ᴜsᴇʀ: {message.from_user.first_name}\n"
        f"ɪᴅ: {message.from_user.id}\n"
        f"ᴜsᴇʀɴᴀᴍᴇ: @{message.from_user.username if message.from_user.username else 'ɴᴏɴᴇ'}"
    )
    
    try:
        # Logging to your channel
        await bot.send_message(LOG_CHANNEL, log_text)
    except Exception as e:
        print(f"Logging Error: {e}")

    # Welcome message for the user
    await message.reply_text(
        f"ʜᴇʟʟᴏ {message.from_user.first_name}!\n\n"
        "ɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ.\n"
        "ᴜsᴇ /play ᴛᴏ sᴛᴀʀᴛ ʟɪsᴛᴇɴɪɴɢ."
    )
