from pyrogram import filters, Client
import bs4, requests, re, asyncio
import os, traceback, random
from info import LOG_CHANNEL, REQUESTED_CHANNEL as GRP_LNK
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
#    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "99",
    "Origin": "https://saveig.app",
    "Connection": "keep-alive",
    "Referer": "https://saveig.app/en",
}
@Client.on_message(filters.regex(r'https?://.*instagram[^\s]+') & filters.incoming)
async def link_handler(Mbot, message):
    link = message.matches[0].group(0)
    global headers
    try:
        m = await message.reply_sticker("CAACAgUAAxkBAAITAmWEcdiJs9U2WtZXtWJlqVaI8diEAAIBAAPBJDExTOWVairA1m8eBA")
        url= link.replace("instagram.com","ddinstagram.com")
        url=url.replace("==","%3D%3D")
        if url.endswith("="):
           dump_file=await message.reply_video(url[:-1],caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
        else:
            dump_file=await message.reply_video(url,caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
        if 'dump_file' in locals():
           await dump_file.forward(GRP_LNK)
        await m.delete()
    except Exception as e:
        try:
            if "/reel/" in url:
               ddinsta=True 
               getdata = requests.get(url).text
               soup = bs4.BeautifulSoup(getdata, 'html.parser')
               meta_tag = soup.find('meta', attrs={'property': 'og:video'})
               try:
                  content_value =f"https://ddinstagram.com{meta_tag['content']}"
               except:
                   pass 
               if not meta_tag:
                  ddinsta=False
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
             
                  if meta_tag.ok:
                     res=meta_tag.json()
               
                #     await message.reply(res)
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                     content_value = meta[0]
                  else:
                      return await message.reply("oops something went wrong")
               try:
                   if ddinsta:
                      dump_file=await message.reply_video(content_value,caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
                   else:
                       dump_file=await message.reply_video(content_value, caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
               except:
                   downfile=f"{os.getcwd()}/{random.randint(1,10000000)}"
                   with open(downfile,'wb') as x:
                       headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
                       x.write(requests.get(content_value,headers=headers).content)
                   dump_file=await message.reply_video(downfile,caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot") 
            elif "/p/" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.reply("oops something went wrong")
              #    await message.reply(meta)
                  for i in range(len(meta) - 1):
                     com=await message.reply_text(meta[i])
                     await asyncio.sleep(1)
                     try:
                        dump_file=await message.reply_video(com.text,caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
                        await com.delete()
                     except:
                         pass 
            elif "stories" in url:
                  meta_tag = requests.post("https://saveig.app/api/ajaxSearch", data={"q": link, "t": "media", "lang": "en"}, headers=headers)
                  if meta_tag.ok:
                     res=meta_tag.json()
                     meta=re.findall(r'href="(https?://[^"]+)"', res['data']) 
                  else:
                      return await message.reply("Oops something went wrong")
                  try:
                     dump_file=await message.reply_video(meta[0], caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
                  except:
                      com=await message.reply(meta[0])
                      await asyncio.sleep(1)
                      try:
                          dump_file=await message.reply_video(com.text,caption="ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ @mrtgcoderbot")
                          await com.delete()
                      except:
                          pass

        except KeyError:
            await message.reply(f"400: Sorry, Unable To Find It Make Sure Its Publically Available :)")
        except Exception as e:
          #  await message.reply_text(f"https://ddinstagram.com{content_value}")
            if LOG_CHANNEL:
               await Mbot.send_message(LOG_CHANNEL,text=f"#ɪᴍᴀɢᴇ_sᴇᴀʀᴄʜ\nʜᴇʏ {message.from_user.mention}\nʀᴇǫᴜᴇsᴛ ɪs {user_query}")
               await Mbot.send_message(LOG_CHANNEL, traceback.format_exc())
          #     await message.reply(tracemsg)
            ##optinal 
            await message.reply(f"400: Sorry, Unable To Find It  try another or report it  to @amal_nath_05 or support chat https://t.me/+1YR5aYuCdr40N2M1")

        finally:
            if 'dump_file' in locals():
               if GRP_LNK:
                  await dump_file.copy(GRP_LNK)
            await m.delete()
            if 'downfile' in locals():
                os.remove(downfile)
            await message.reply("<a href='https://t.me/mrtgcoderbot'>ᴜsᴇ ɴᴇᴡ ғᴇᴀᴛᴜʀᴇs</a>")
