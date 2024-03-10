from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("𝑺𝑯𝑨𝑹𝑬 𝒀𝑶𝑼𝑹 𝑳𝑰𝑵𝑲" ,url=f"https://t.me/share/url?url=https://t.me/movie_hub09_bot?start={message.from_user.id}") ]   ])
    # Replace the following placeholders with your actual values
    button_text = '𝑺𝑯𝑨𝑹𝑬 𝒀𝑶𝑼𝑹 𝑳𝑰𝑵𝑲'
    photo_url = 'https://graph.org/file/f8c26a2bda2c9ca9c6871.jpg'
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention}, \n\nHᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʀᴇғғᴇʀᴀʟ ʟɪɴᴋ:\nhttps://t.me/movie_090_bot?start={message.from_user.id}\n\nShare this link with your friends, Each time they join, You will get 10 refferal points and after 100 points you will get 1 month Premium subscription.\n\nइस लिंक को दोस्तों के साथ Share करें, जब वे शामिल होंगे, तो आपको 10 रेफरल पॉइंट मिलेंगे ,और 100 पॉइंट के बाद आपको 1 महीने की प्रीमियम सदस्यता Automatically मिल जायगी।.",reply_to_message_id = message.id,reply_markup=reply_markup,)  # Add your plan details here

    # Create an inline keyboard with the buy plan button
    keyboard = [[InlineKeyboardButton(button_text, url='https://t.me/share/url?url=https://t.me/movie_hub09_bot?start={message.from_user.id}')
                ]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the plan details, photo, and the buy plan button
    await client.send_photo(chat_id=message.chat.id,photo=photo_url, caption=reply_text, reply_markup=reply_markup)
