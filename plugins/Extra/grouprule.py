# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


# def plan(update: Update, context: CallbackContext) -> None:
@Client.on_message(filters.private & filters.command(["grouprule"]))
async def grorule(client,message):
    # Replace the following placeholders with your actual values
    button_text = '𝑩𝑼𝒀 𝑷𝑳𝑨𝑵'
    photo_url = 'https://graph.org/file/f8c26a2bda2c9ca9c6871.jpg'
    grorule_text = '<code>♨️ 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 ♨️

🔹 Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :
› ᴀᴠᴀᴛᴀʀ 2009 ✅
› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅
› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌
› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ᴅᴜʙʙᴇᴅ..❌

🔹Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : 
› ᴠɪᴋɪɴɢs S01 ✅
› ᴠɪᴋɪɴɢs S01E01 ✅
› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅
› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌
› ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌
› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs❌ 
🔹 ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.

🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..

🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..

⚙️ 𝖭ᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.</code>.'  # Add your plan details here

    # Create an inline keyboard with the buy plan button
    keyboard = [[ InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆",callback_data = "close_data")
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await client.send_photo(chat_id=message.chat.id,photo=photo_url, caption=grorule_text, reply_markup=reply_markup)
