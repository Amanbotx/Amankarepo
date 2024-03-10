from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)

@Client.on_message(filters.command(["refer"]))
async def refer_info(bot, update):
    refer = update.text.split(" ", 1)[1]
    
    info ="""(f"ʜᴇʏ {message.from_user.mention}, \nHᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʀᴇғғᴇʀᴀʟ ʟɪɴᴋ:\nhttps://t.me/movie_090_bot?start={message.from_user.id}\nShare this link with your friends, Each time they join, You will get 10 refferal points and after 100 points you will get 1 month Premium subscription.\n\nइस लिंक को दोस्तों के साथ Share करें, जब वे शामिल होंगे, तो आपको 10 रेफरल पॉइंट मिलेंगे ,और 100 पॉइंट के बाद आपको 1 महीने की प्रीमियम सदस्यता Automatically मिल जायगी। ",reply_to_message_id = message.id,reply_markup=reply_markup,)"""
    buttons=[[
       InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close_data')
    ]]
    try:
        await update.reply_photo(
            photo="https://telegra.ph/file/834750cfadc32b359b40c.jpg",
            refer=info,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
