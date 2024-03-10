from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
@Client.on_message(filters.private & filters.command(["refer"]))
async def refer(client,message):
    reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("𝑺𝑯𝑨𝑹𝑬 𝒀𝑶𝑼𝑹 𝑳𝑰𝑵𝑲" ,url=f"https://telegram.me/share/url?url=https://t.me/Testing_00100_bot?start=reff_{message.from_user.id}&text=Hello%21%20Experience%20a%20bot%20that%20offers%20a%20vast%20library%20of%20unlimited%20movies%20and%20series.%20%F0%9F%98%83")
              ],[
                InlineKeyboardButton('00', callback_data='00'),
                InlineKeyboardButton('00', callback_data='00')
              ]   ])
    
    await message.reply_text(f"ʜᴇʏ {message.from_user.mention}, \n\nHᴇʀᴇ ɪꜱ ʏᴏᴜʀ ʀᴇғғᴇʀᴀʟ ʟɪɴᴋ:\nhttps://t.me/Testing_00100_bot?start=reff_{message.from_user.id}\n\nShare this link with your friends, Each time they join, You will get 10 refferal points and after 100 points you will get 1 month Premium subscription.\n\nइस लिंक को दोस्तों के साथ Share करें, जब वे शामिल होंगे, तो आपको 10 रेफरल पॉइंट मिलेंगे ,और 100 पॉइंट के बाद आपको 1 महीने की प्रीमियम सदस्यता Automatically मिल जायगी। ",reply_to_message_id = message.id,reply_markup=reply_markup,)
    

