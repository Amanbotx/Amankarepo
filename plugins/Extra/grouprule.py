# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackContext
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters


# def plan(update: Update, context: CallbackContext) -> None:
@Client.on_message(filters.private & filters.command(["grouprule"]))
async def plan(client,message):
    # Replace the following placeholders with your actual values
    button_text = '𝑩𝑼𝒀 𝑷𝑳𝑨𝑵'
    photo_url = 'https://graph.org/file/f8c26a2bda2c9ca9c6871.jpg'
    plan_text = '♨️ 𝗚𝗥𝗢𝗨𝗣 𝗥𝗨𝗟𝗘𝗦 ♨️\n\n🔹 Sᴇᴀʀᴄʜ Mᴏᴠɪᴇ Wɪᴛʜ Cᴏʀʀᴇᴄᴛ Sᴘᴇʟʟɪɴɢ :\n› ᴀᴠᴀᴛᴀʀ 2009 ✅\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ ✅\n› ᴀᴠᴀᴛᴀʀ ᴍᴏᴠɪᴇ ❌\n› ᴀᴠᴀᴛᴀʀ ʜɪɴᴅɪ\nᴅᴜʙʙᴇᴅ..❌\n\n🔹Sᴇᴀʀᴄʜ Wᴇʙ Sᴇʀɪᴇs Iɴ ᴛʜɪs Fᴏʀᴍᴀᴛᴇ : \n› ᴠɪᴋɪɴɢs S01 ✅\n› ᴠɪᴋɪɴɢs S01E01 ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ✅\n› ᴠɪᴋɪɴɢs S01 ʜɪɴᴅɪ ᴅᴜʙʙ. ❌\n› ᴠɪᴋɪɴɢs sᴇᴀsᴏɴ 1 ❌\n› ᴠɪᴋɪɴɢs ᴡᴇʙ sᴇʀɪᴇs❌ \n🔹 ᴅᴏɴ'ᴛ ᴅᴏ ᴀɴʏ sᴇʟғ ᴘʀᴏᴍᴏᴛɪᴏɴ.\n\n🔹 ᴅᴏɴ'ᴛ sᴇɴᴅ ᴀɴʏ ᴋɪɴᴅ ᴏғ ᴘʜᴏᴛᴏ, ᴠɪᴅᴇᴏ ᴅᴏᴄᴜᴍᴇɴᴛs, ᴜʀʟ ᴇᴛᴄ..\n\n🔹 ᴅᴏɴ'ᴛ ʀᴇǫᴜᴇsᴛ ᴀɴʏ ᴛʜɪɴɢs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴍᴏᴠɪᴇ sᴇʀɪᴇs ᴀɴɪᴍᴇs..\n\n⚙️ 𝖭ᴏᴛᴇ :- 𝖠ʟʟ ᴍᴇ𝗌𝗌ᴀɢᴇ𝗌 ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏ-ᴅᴇʟᴇᴛᴇᴅ ᴀғᴛᴇʀ 𝟷𝟶 ᴍɪɴᴜᴛᴇ𝗌 ᴛᴏ ᴀᴠᴏɪᴅ ᴄᴏᴘʏʀɪɢʜᴛ ɪ𝗌𝗌ᴜᴇ𝗌.'  # Add your plan details here

    # Create an inline keyboard with the buy plan button
    keyboard = [[ InlineKeyboardButton("𝑪𝒍𝒐𝒔𝒆",callback_data = "close_data")
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await client.send_photo(chat_id=message.chat.id,photo=photo_url, caption=plan_text, reply_markup=reply_markup)

