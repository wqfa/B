import asyncio
import os
import random
import time
import pyrogram
import pyromod
import redis
import requests
import subprocess
import urllib.request
import uvloop
uvloop.install()
from time import time
from time import sleep
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.enums import ChatType
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import subprocess
import psutil


try:
    d = open("bio.txt").read()
    if not d:
        d= "𝐃𝐨𝐧𝐭 𝐓𝐫𝐲 𝐖𝐢𝐭𝐡 : @FLOOD_KINGS"
except:
        pass  
try:    
    q = open("name.txt").read()
    if not q:
        q= "R"
except:
        pass       
try:
	Info = open("info.txt").read()
except:
	Info = "VENOM"	
if ":" not in Info:
	token = input("- EnTeR ToKeN : ");reqtoken = requests.get(f"https://api.telegram.org/bot{token}/getme").json();req = reqtoken["ok"]
	if req == True:
		id = input("- EnTeR iD : ")
		o = open("info.txt",'a').write(str(token)+'\n'+str(id))
		print("- Done .")
	else:
		print("Erorr ToKeN .")
else:
    
	print("Ok .")
info = open("info.txt",'r').read();token = info.split('\n')[0];own_id = info.split('\n')[1]
app = Client("seeeeexy",api_id=17765175,api_hash="e77878aa96e80375b1272e60f746bbf2",bot_token=token)
r = redis.Redis()

@app.on_message(filters.command("start"))
async def start(app, message):
    id = message.from_user.id
    if str(id) == own_id:
           await app.send_video(message.chat.id,video="https://t.me/vd_d_dd/38",caption=f'''• 𝐇𝐢, {message.from_user.first_name}!\n• 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐈𝐧 𝐇𝐞𝐥𝐥,\n• 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐈𝐧 𝐁𝐨𝐭 𝐓𝐚𝐤𝐞 𝐅𝐥𝐨𝐨𝐝\n• 𝐅𝐨𝐫 𝐀𝐫𝐚𝐛𝐢𝐜 : /ar\n• 𝐁𝐲 : 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍''', reply_markup=ReplyKeyboardMarkup(
          [
              ["⌞𝐈𝐍𝐅𝐎⌝","/start"],
              ["⌞𝐀𝐝𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝","⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝"],
              ["⌞𝐏𝐢𝐧 𝐔𝐬𝐞𝐫⌝", "⌞𝐔𝐧𝐏𝐢𝐧 𝐔𝐬𝐞𝐫⌝"],
              ["⌞𝐑𝐮𝐧 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝", "⌞𝐒𝐭𝐨𝐩 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝"],
              ["⌞𝐑𝐮𝐧 𝐆𝐫𝐨𝐮𝐩⌝", "⌞𝐒𝐭𝐨𝐩 𝐆𝐫𝐨𝐮𝐩⌝"],
              ["⌞𝐑𝐮𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥⌝", "⌞𝐒𝐭𝐨𝐩 𝐂𝐡𝐚𝐧𝐧𝐞𝐥⌝"],
              ["⌞𝐂𝐡𝐚𝐧𝐠𝐞 𝐁𝐢𝐨⌝", "⌞𝐂𝐡𝐚𝐧𝐠𝐞 𝐍𝐚𝐦𝐞⌝"],
              ["⌞𝐂𝐡𝐞𝐜𝐤 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝","⌞𝐂𝐡𝐞𝐜𝐤 𝐔𝐬𝐞𝐫⌝"],
              ["⌞𝐒𝐞𝐫𝐯𝐞𝐫 𝐒𝐭𝐚𝐭𝐮𝐬⌝","⌞𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝"],
              ["⌞𝐂𝐥𝐞𝐚𝐧 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝","⌞𝐏𝐢𝐧𝐠⌝"],
              ["⌞𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬⌝","⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬⌝"],
              ["⌞𝐀𝐝𝐝 𝐒𝐥𝐞𝐞𝐩⌝", "⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐒𝐥𝐞𝐞𝐩⌝"],
              ["⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐥𝐥 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝"],
          ])) 
           
    else:
            await app.send_video(message.chat.id,video="https://t.me/vd_d_dd/37",caption=f'''• 𝐇𝐢, {message.from_user.first_name}!\n• 𝐓𝐡𝐢𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐅𝐨𝐫 𝐓𝐚𝐤𝐢𝐧𝐠 𝐅𝐥𝐨𝐨𝐝\n• 𝐁𝐲 ➞ : 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍''',reply_markup = InlineKeyboardMarkup(
           inline_keyboard = [
        [
            InlineKeyboardButton(text="𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍", url="https://t.me/u4060"),
            InlineKeyboardButton(text="𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/DevEviI"),
        ],
        [
            InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫 𝐎𝐅 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭", url=f"tg://user?id={own_id}"),
        ],

]))
@app.on_message(filters.command("ar"))
async def start(app, message):
    id = message.from_user.id
    if str(id) == own_id:
           await app.send_video(message.chat.id,video="https://t.me/vd_d_dd/38",caption=f'''• مرحبا, {message.from_user.first_name}\n• اهلا بك في بوت صيد الخاصيه\n• للغه الانجليزيه : /start \n• 𝐁𝐲 : 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍''', reply_markup=ReplyKeyboardMarkup(
          [
              ["⌝معلوماتك⌞","/start"],
              ["⌝اضف حساب⌞","⌝حذف حساب⌞"],
              ["⌝تثبيت يوزر⌞", "⌝ازاله يوزر⌞"],
              ["⌝تشغيل حساب⌞", "⌝ايقاف حساب⌞"],
              ["⌝تشغيل جروب⌞", "⌝ايقاف جروب⌞"],
              ["⌝تشغيل قناه⌞", "⌝ايقاف قناه⌞"],
              ["⌝تغير بايو⌞", "⌝تغير اسم⌞"],
              ["⌝تحقق سيشنات⌞","⌝تحقق يوزر⌞"],
              ["⌝حاله السيرفر⌞","⌝استخراج جلسه⌞"],
              ["⌝تنظيف سيشنات⌞","⌝بنج⌞"],
              ["⌝حسباتي⌞","⌝مسح قنوات + جروب⌞"],
              ["⌝اضف اسليب⌞", "⌝حذف اسليب⌞"],
              ["⌝حذف كل الحسابات⌞"],
          ])) 
    else:
            await app.send_video(message.chat.id,video="https://t.me/vd_d_dd/37",caption=f'''• 𝐇𝐢, {message.from_user.first_name}!\n• 𝐓𝐡𝐢𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐅𝐨𝐫 𝐓𝐚𝐤𝐢𝐧𝐠 𝐅𝐥𝐨𝐨𝐝\n• 𝐁𝐲 ➞ : 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍''',reply_markup = InlineKeyboardMarkup(
           inline_keyboard = [
        [
            InlineKeyboardButton(text="𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍", url="https://t.me/u4060"),
            InlineKeyboardButton(text="𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/DevEviI"),
        ],
        [
            InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫 𝐎𝐅 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭", url=f"tg://user?id={own_id}"),
        ],

]))

@app.on_message(filters.text)
async def main(app, message):
    id = message.from_user.id
    if str(id) == own_id:
        pass
    else:
           await app.send_video(message.chat.id,video="https://t.me/vd_d_dd/37",caption=f'''• 𝐇𝐢, {message.from_user.first_name}!\n• 𝐓𝐡𝐢𝐬 𝐂𝐡𝐞𝐜𝐤𝐞𝐫 𝐅𝐨𝐫 𝐓𝐚𝐤𝐢𝐧𝐠 𝐅𝐥𝐨𝐨𝐝\n• 𝐁𝐲 ➞ : 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍''',reply_markup = InlineKeyboardMarkup(
           inline_keyboard = [
        [
            InlineKeyboardButton(text="𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍", url="https://t.me/u4060"),
            InlineKeyboardButton(text="𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", url="https://t.me/DevEviI"),
        ],
        [
            InlineKeyboardButton(text="𝐎𝐰𝐧𝐞𝐫 𝐎𝐅 𝐓𝐡𝐢𝐬 𝐁𝐨𝐭", url=f"tg://user?id={own_id}"),
        ],

]))
           return
    
#####################################################################Sleeping    
    if message.text == '⌞𝐀𝐝𝐝 𝐒𝐥𝐞𝐞𝐩⌝' or message.text == '⌝اضف اسليب⌞':
        try:
            os.remove("sleep.txt")
        except:
            pass
        uss = await app.ask(message.chat.id, '• 𝐒𝐞𝐧𝐝 𝐒𝐥𝐞𝐞𝐩 𝐓𝐢𝐦𝐞 𝐓𝐨 𝐀𝐝𝐝 ➞ :')
        asleep = uss.text
        if asleep.replace('.', '', 1).isdigit():  
          with open('sleep.txt', 'a') as the_combo:
            the_combo.write(str(asleep))
          await message.reply_text(f'𝐃𝐨𝐧𝐞 𝐀𝐝𝐝𝐢𝐧𝐠 𝐒𝐥𝐞𝐞𝐩 𝐓𝐢𝐦𝐞 ➞ : {asleep}')
        else:
            await message.reply_text('من فضلك اضف ارقام فقط وليس حروف.')
    if message.text == '⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐒𝐥𝐞𝐞𝐩⌝' or message.text == '⌝حذف اسليب⌞':
        try:
            os.remove("sleep.txt")
        except:
            with open('sleep.txt', 'a') as the_combo:
                acc = 0
                the_combo.write(str(acc))
        await message.reply_text('• 𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐢𝐧𝐠 𝐒𝐥𝐞𝐞𝐩 𝐓𝐢𝐦𝐞 \n• 𝐀𝐧𝐝 𝐆𝐨 𝐁𝐚𝐜𝐤 𝐓𝐨 𝐒𝐥𝐞𝐞𝐩 : 𝟎')
#################################session
    if message.text=='⌞𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝' or message.text == '⌝استخراج جلسه⌞':
        chat = message.chat
        number = await app.ask(chat.id, "من فضلك ارسل لي رقم هاتفك +201142****** هكذا")
        phone = number.text.strip()
        try:
             glsa = Client(":memory:", api_id=6,api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")
        except Exception as e:
            await message.reply_text(f"**ERROR:** `{str(e)}`")
            return
        try:
            await glsa.connect()
        except ConnectionError:
           await glsa.disconnect()
           await glsa.connect()
        try:
            code = await glsa.send_code(phone)
            await asyncio.sleep(2)
        except PhoneNumberInvalid:
           await message.reply_text("الرقم الهاتف خطاء ❌")
           return

        try:
             otp = await app.ask(
            chat.id, ("تم ارسال لك رمز O T P, "
                      "من فضلك ارسل لي كود OTP بهذه الطريقه `1 2 3 4 5` __(راعي تواجد مسافه بين كل رقم من 5 ارقام)__"), timeout=300)

        except TimeoutError:
           await message.reply_text("تجاوزة 5 دقائق من فضلك حاول مره اخره")
           return
        otp_code = otp.text
        try:
            await glsa.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
        except PhoneCodeInvalid:
          await message.reply_text("رمز OTP خطاء ")
          return
        except PhoneCodeExpired:
            await message.reply_text("OTP is Expired.")
            return
        except SessionPasswordNeeded:
            try:
                two_step_code = await app.ask(
                chat.id,
                "حسابك يستخدم التحقق بخطوتين.\nمن فضلك ارسل لي الباسورد.",
                timeout=300
            )
            except TimeoutError:
               await message.reply_text("تجاوزة 5 دقائق من فضلك حاول مره اخره")
               return
            new_code = two_step_code.text
            try:
                await glsa.check_password(new_code)
            except Exception as e:
               await message.reply_text(f"**ERROR:** `{str(e)}`")
               return
        except Exception as e:
            await message.reply_text(f"**ERROR:** `{str(e)}`")
            return
        try:
            session_string = await glsa.export_session_string()
        except Exception as e:
           await message.reply_text(f"**ERROR:** `{str(e)}`")
           return
        await message.reply_text(f"جلسه بايروجرام اصدار :\n{session_string}")
        await glsa.disconnect()        
#####################################################################INFO        
    if message.text == '⌞𝐈𝐍𝐅𝐎⌝' or message.text == '⌝معلوماتك⌞':
        i = 'user.txt'
        ii = 'sleep.txt'
        us = 'None'
        anum = '0'
        sle = 'لا يوجد عدد اسليب !'
        try:
           sle = open(ii, 'r').read()
        except:
            pass   
        try:
            us = open(i, 'r').read()
        except :
          pass
        try:
           anum = len(open("account.txt").readlines())
        except:
          pass
        await message.reply_text(text=f"• 𝐔𝐬𝐞𝐫 ➞ : @{us}\n\n• 𝐒𝐥𝐞𝐞𝐩 ➞ : [ {sle} ]\n\n• 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ➞ : {anum}\n\n• 𝐁𝐲 ➞ : [𝐃𝐚𝐝𝐲](tg://user?id=5345637082)")
#####################################################################Pin, Revome        
    if message.text == "⌞𝐏𝐢𝐧 𝐔𝐬𝐞𝐫⌝" or message.text == "⌝تثبيت يوزر⌞":
        try:
            os.remove("user.txt")
        except:
            pass
        uss = await app.ask(message.chat.id, f"𝐒𝐞𝐧𝐝 𝐔𝐬𝐞𝐫 𝐍𝐚𝐦𝐞 𝐓𝐨 𝐏𝐢𝐧 ➞ :")
        acc = uss.text
        if acc.startswith("@"):
          acc = acc[1:]
          with open('user.txt', 'a') as the_combo:
              the_combo.write(str(acc))
          await message.reply_text(f"• 𝐃𝐨𝐧𝐞 𝐏𝐢𝐧 𝐔𝐬𝐞𝐫 𝐍𝐚𝐦𝐞")
        else:
          await message.reply_text("من فضلك اعد مجددا وارسل اليوزر نيم مع @")  
    if message.text == "⌞𝐔𝐧𝐏𝐢𝐧 𝐔𝐬𝐞𝐫⌝" or message.text == '⌝ازاله يوزر⌞':
        try:
            os.remove("user.txt")
        except:
            pass
        await message.reply_text(f"• 𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐞 𝐔𝐬𝐞𝐫 𝐍𝐚𝐦𝐞")
#####################################################################Sessions        
    if message.text == '⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐥𝐥 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝' or message.text == '⌝حذف كل الحسابات⌞':
        await message.reply_text("𝐈𝐟 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐒𝐮𝐫𝐞 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐥𝐥 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬, 𝐒𝐞𝐧𝐝 :\n/delete_all")
        if message.text == '/delete_all':
           os.remove("account.txt")
        await message.reply_text("• 𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐥𝐥 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬")
    if message.text == '⌞𝐌𝐲 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬⌝'or message.text == '⌝حسباتي⌞':
        m = len(open("account.txt").readlines())
        await message.reply_text(f"• 𝐍𝐮𝐦𝐛𝐞𝐫 𝐎𝐅 𝐘𝐨𝐮𝐫 𝐀𝐜𝐜𝐨𝐮𝐧𝐭𝐬 ➞ : {m}") 
    if message.text == '⌞𝐂𝐥𝐞𝐚𝐧 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝' or message.text == '⌝تنظيف سيشنات⌞':
           q = 0
           d = 0
           m = len(open("account.txt").readlines())
           venn = open("account.txt", "r").read().split("\n")[:-1]
           await message.reply_text("• 𝐖𝐚𝐢𝐭 𝐈 𝐖𝐢𝐥𝐥 𝐂𝐡𝐞𝐜𝐤.")
           for session in venn:
               try:
                   qt= Client("name_session", session_string=session, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                   await qt.start()
               except Exception as e:
                    with open("account.txt", "r") as file:
                        lines = file.readlines()
                    with open("account.txt", "w") as file:
                          for line in lines:
                              if session not in line:
                                 file.write(line)
                    q  +=1
           await message.reply_text(f"• 𝐃𝐨𝐧𝐞 𝐂𝐥𝐞𝐚𝐧\n• 𝐓𝐨𝐭𝐚𝐥 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 ➞ : {m}\n• 𝐒𝐞𝐬𝐬𝐢𝐨𝐧𝐬 𝐓𝐡𝐚𝐭 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐀𝐫𝐞 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 ➞ : {q}")
    if message.text == '⌞𝐂𝐡𝐞𝐜𝐤 𝐒𝐞𝐬𝐬𝐢𝐨𝐧⌝' or message.text == '⌝تحقق سيشنات⌞':
           n = 0
           q = 0
           d = 0
           t = 0
           m = len(open("account.txt").readlines())
           venn = open("account.txt", "r").read().split("\n")[:-1]
           await message.reply_text("• 𝐖𝐚𝐢𝐭 𝐈 𝐖𝐢𝐥𝐥 𝐂𝐡𝐞𝐜𝐤.")
           for session in venn:
               try:
                  qt= Client("name_session", session_string=session, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                  await qt.start()
               except Exception as e:
                  q  +=1
                  pass
               try:
                   await qt.set_username("r_r_b0")
               except FloodWait as e:
                   n += 1
               except Exception as e:
                pass   
           await message.reply_text(f"• 𝐓𝐨𝐭𝐚𝐥 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 ➞ : {m}\n• 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐅𝐥𝐨𝐨𝐝 ➞ : {n} ")
           await qt.stop()
    if message.text == "⌞𝐀𝐝𝐝 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝" or message.text == '⌝اضف حساب⌞':
       uss = await app.ask(message.chat.id, '• 𝐒𝐞𝐧𝐝 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐭𝐨 𝐀𝐝𝐝 ➞ :')
       session = uss.text
       count = sum(c.isalnum() for c in session)
       if count <= 50:
           await message.reply_text("• 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐍𝐨𝐭 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐂𝐨𝐝𝐞 !")
           return
       am = open('account.txt', 'r').read() 
       if str(session) in str(am):
          await message.reply_text("• 𝐓𝐡𝐢𝐬 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 !")
       else:
            try :
                 aps = Client("name_session", session_string=session, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                 await aps.start()
            except Exception as e:
                await message.reply_text('• 𝐓𝐡𝐢𝐬 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐅𝐚𝐢𝐥𝐞𝐝.')
                return
            with open('account.txt', 'a') as the_combo:
                    the_combo.write(str(session)+'\n')
                    await message.reply_text('• 𝐃𝐨𝐧𝐞 𝐀𝐝𝐝𝐞𝐝 𝐒𝐞𝐬𝐬𝐢𝐨𝐧')
    if message.text == '⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝' or message.text == '⌝حذف حساب⌞':
       uss = await app.ask(message.chat.id, f"• 𝐒𝐞𝐧𝐝 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐓𝐨 𝐃𝐞𝐥𝐞𝐭𝐞 ➞ :")
       session = uss.text
       amm = open("account.txt").read()
       count = sum(c.isalnum() for c in session)
       if count <= 50:
           await message.reply_text("• 𝐓𝐡𝐢𝐬 𝐈𝐬 𝐍𝐨𝐭 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐂𝐨𝐝𝐞 !")
           return
       if session in amm:
           with open("account.txt", "w") as file:
               file.write(amm.replace(session, ""))
           await message.reply_text("𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐞 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
       else:
        await message.reply_text("• 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 𝐈𝐒 𝐍𝐨𝐭 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐄𝐱𝐢𝐬𝐭𝐞𝐝")
#####################################################################Changes    
    if message.text == '⌞𝐂𝐡𝐚𝐧𝐠𝐞 𝐍𝐚𝐦𝐞⌝' or message.text == '⌝تغير اسم⌞':
        uss = await app.ask(message.chat.id, '• 𝐒𝐞𝐧𝐝 𝐍𝐚𝐦𝐞 𝐓𝐨 𝐂𝐡𝐚𝐧𝐠𝐞. ➞ :')
        name = uss.text
        f = open("name.txt","w+")
        f.write(name)
        f.close()
        await message.reply_text(f'𝐃𝐨𝐧𝐞 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐞 𝐍𝐚𝐦𝐞 𝐓𝐨 : {name}')
    if message.text == '⌞𝐂𝐡𝐚𝐧𝐠𝐞 𝐁𝐢𝐨⌝' or message.text == '⌝تغير بايو⌞':
        uss = await app.ask(message.chat.id, '• 𝐒𝐞𝐧𝐝 𝐁𝐢𝐨 𝐓𝐨 𝐂𝐡𝐚𝐧𝐠𝐞. ➞ :')
        name = uss.text
        f = open("bio.txt","w+")
        f.write(name)
        f.close()
        await message.reply_text(f'𝐃𝐨𝐧𝐞 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐞 𝐁𝐢𝐨 𝐓𝐨 : {name}')
#####################################################################Ping
    if message.text == '⌞𝐏𝐢𝐧𝐠⌝' or message.text == '⌝بنج⌞':
        d = subprocess.run("ping -c 1 google.com | grep -oP 'time=\\K[^ ]+'", shell=True, capture_output=True, text=True)
        await message.reply_text(f'• 𝐏𝐢𝐧𝐠 : {d.stdout}')  
    if message.text == '⌞𝐒𝐞𝐫𝐯𝐞𝐫 𝐒𝐭𝐚𝐭𝐮𝐬⌝' or message.text == '⌝حاله السيرفر⌞':
         memory = psutil.virtual_memory()
         total_memory = memory.total
         available_memory = memory.available
         used_memory = memory.used
         physical_cores = os.cpu_count()
         logical_cores = psutil.cpu_count(logical=True)
         total_memory = psutil._common.bytes2human(total_memory)
         available_memory = psutil._common.bytes2human(available_memory)
         used_memory = psutil._common.bytes2human(used_memory)
         print("Physical Cores:", physical_cores)
         print("Logical Cores:", logical_cores)
         disk_usage = psutil.disk_usage('/')
         total_space = disk_usage.total
         used_space = disk_usage.used
         free_space = disk_usage.free
         total_space = psutil._common.bytes2human(total_space)
         used_space = psutil._common.bytes2human(used_space)
         free_space = psutil._common.bytes2human(free_space)
         uptime = subprocess.check_output(["uptime"]).decode().strip()
         await message.reply_text(f'• 𝐌𝐞𝐦𝐨𝐫𝐲 𝐈𝐍𝐅𝐎 \n• 𝐓𝐨𝐭𝐚𝐥 ➞ : {total_memory}\n• 𝐀𝐯𝐚𝐢𝐥𝐚𝐛𝐥𝐞 ➞ : {available_memory}\n• 𝐔𝐬𝐞𝐝 ➞ : {used_memory}\n════════════════════\n• 𝐂𝐏𝐔 𝐈𝐍𝐅𝐎 \n• 𝐏𝐡𝐲𝐬𝐢𝐜𝐚𝐥 𝐂𝐨𝐫𝐞𝐬 ➞ : {physical_cores} \n• 𝐋𝐨𝐠𝐢𝐜𝐚𝐥_𝐜𝐨𝐫𝐞𝐬 ➞ : {logical_cores}\n════════════════════\n• 𝐃𝐢𝐬𝐤 𝐈𝐍𝐅𝐎 \n• 𝐓𝐨𝐭𝐚𝐥 𝐃𝐢𝐬𝐤 𝐒𝐩𝐚𝐜𝐞 ➞ : {total_space}\n• 𝐔𝐬𝐞𝐝 𝐃𝐢𝐬𝐤 ➞ : {used_space}\n• 𝐅𝐫𝐞𝐞 𝐃𝐢𝐬𝐤 𝐒𝐩𝐚𝐜𝐞 ➞ : {free_space}\n════════════════════\n• 𝐒𝐞𝐫𝐯𝐞𝐫 𝐔𝐩 𝐓𝐢𝐦𝐞 ➞ : {uptime}')

#####################################################################StopLoops
    wa = open('user.txt', 'r').read()        
    if message.text == '⌞𝐒𝐭𝐨𝐩 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝' or message.text == '⌝ايقاف حساب⌞':
        r.delete('on')
        await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐒𝐭𝐨𝐩 => @{wa}")
    if message.text == '⌞𝐒𝐭𝐨𝐩 𝐂𝐡𝐚𝐧𝐧𝐞𝐥⌝' or message.text == '⌝ايقاف قناه⌞':
        r.delete('onn')
        await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐒𝐭𝐨𝐩 => @{wa}")
    if message.text == '⌞𝐒𝐭𝐨𝐩 𝐆𝐫𝐨𝐮𝐩⌝' or message.text == '⌝ايقاف جروب⌞':
        r.delete('onnn')
        await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐒𝐭𝐨𝐩 => @{wa}")
#####################################################################Check,And Delete Cahnnel        
    if message.text == '⌞𝐂𝐡𝐞𝐜𝐤 𝐔𝐬𝐞𝐫⌝' or message.text =='⌝تحقق يوزر⌞':
       wa = open("user.txt").read()
       req = requests.get(f"https://t.me/{wa}").text
       if "tgme_username_link" not in req:
          await message.reply_text("𝐖𝐓𝐅 𝐓𝐡𝐢𝐬 𝐔𝐬𝐞𝐫 𝐔𝐬𝐞𝐝.")
       else:
          await message.reply_text("𝐓𝐡𝐢𝐬 𝐔𝐬𝐞𝐫 𝐢𝐬 𝐅𝐥𝐨𝐨𝐝 𝐍𝐨𝐰 !")
    if message.text == '⌞𝐃𝐞𝐥𝐞𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬⌝' or message.text == '⌝مسح قنوات + جروب⌞':
       await message.reply_text("𝐎𝐤𝐚𝐲 𝐖𝐚𝐢𝐭 𝐈 𝐖𝐢𝐥𝐥 𝐃𝐞𝐥𝐞𝐭𝐞𝐢𝐧𝐠..")
       ven = open("account.txt", "r").read().split("\n")[:-1]
       for sessi in ven:
            sub_client = Client("name_session", session_string=sessi, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
            await sub_client.start()
            async for dialog in sub_client.get_dialogs():
                if dialog.chat.type != ChatType.PRIVATE:
                  try:
                      await sub_client.leave_chat(dialog.chat.id, delete=True)
                      
                  except pyrogram.errors.exceptions.not_acceptable_406.ChannelPrivate:
                      pass
                  except Exception as e:
                    print(f"An error occurred while leaving chat: {e}")
                    pass
    wa = open('user.txt', 'r').read()  
    ven = open("account.txt", "r").read().split("\n")[:-1]
    d = open("bio.txt").read()
    q = open("name.txt").read()
    try:
                isl = open("sleep.txt", 'r').read()
    except:
                iso = open('sleep.txt', 'a')
                iso.write('0')
                isl = open("sleep.txt", 'r').read()  

############################Loops#########################################     
#############################Account#########################################
    if message.text == '⌞𝐑𝐮𝐧 𝐀𝐜𝐜𝐨𝐮𝐧𝐭⌝' or message.text == '⌝تشغيل حساب⌞':
            clicks = 0              
            r.set('on',1)
            await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐆𝐨 => @{wa}")
            req = requests.get(f"https://t.me/{wa}").text
            if "tgme_username_link" not in req:
                await message.reply_text(f"𝐔𝐧 𝐅𝐥𝐨𝐨𝐝 => @{wa}")
                return
            while r.get('on'):
                for session in ven:
                    if not r.get('on'): 
                       break
                    try:
                        clicks+=1
                        tele = Client("name_session", session_string=random.choice(ven), api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                        await tele.connect()
                        await asyncio.sleep(float(isl))
                        await tele.update_profile(first_name=q,bio=d)
                        await tele.set_username(wa)
                        me = await tele.get_me()
                        pho = me.phone_number
                        phone = pho[:-4] + "*****"
                        await app.send_video(message.chat.id, "https://t.me/vd_d_dd/35", caption=f"""• 𝐖𝐞 𝐀𝐫𝐞 𝐓𝐡𝐞 𝐊𝐢𝐧𝐠𝐬 𝐒𝐨 𝐖𝐡𝐨 𝐀𝐫𝐞 𝐲𝐨𝐮?\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐒𝐚𝐯𝐞𝐝 𝐈𝐧 ➞ : [ 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 ]\n• 𝐏𝐡𝐨𝐧𝐞 ➞ : [ {phone} ]\n• 𝐁𝐲 ➞ : [ [ 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍🇮🇶 ] ](https://t.me/u4060)""")
                        r.delete('on')
                    except Exception as e:
                        await message.reply_text(f'''• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐄𝐫𝐫𝐨𝐫 ➞ : \n\n{e}''') 
#############################Cahnnel#########################################       
    if message.text == '⌞𝐑𝐮𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥⌝' or message.text == '⌝تشغيل قناه⌞':
            await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐆𝐨 => @{wa}")
            clicks = 0              
            wa = open('user.txt', 'r').read()  
            ven = open("account.txt", "r").read().split("\n")[:-1]
            r.set('onn',1)
            id = info.split('\n')[1]
            user = await app.get_users(id)
            first_name = user.first_name
            req = requests.get(f"https://t.me/{wa}").text
            if "tgme_username_link" not in req:
                await message.reply_text(f"𝐔𝐧 𝐅𝐥𝐨𝐨𝐝 => @{wa}")
                r.delete('onn')
            while r.get('onn'):  
                for session in ven:
                    if not r.get('onn'):
                       break
                    try:
                        clicks+=1

                        t = Client("name_session", session_string=session, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                        await t.connect()
                        ch = (await t.create_channel("𝐅𝐥𝐨𝐨𝐝 𝐊𝐢𝐧𝐠𝐬 #𝟏", "@u4060 \ @DevEviI")).id
                        await asyncio.sleep(float(isl))
                        await t.set_chat_username(ch, wa)
                        phone = (await t.get_me()).phone_number[:-2] + "xx"
                        await t.send_video(ch,video=f"https://t.me/vd_d_dd/39",caption=f"• 𝐒𝐨𝐫𝐫𝐲 𝐖𝐞 𝐊𝐢𝐧𝐠𝐬 𝐅𝐥𝐨𝐨𝐝!\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐇𝐮𝐧𝐭𝐞𝐝 𝐁𝐲 ➞ : {first_name}")
                        await app.send_video(message.chat.id, "https://t.me/vd_d_dd/35", caption=f"""• 𝐖𝐞 𝐀𝐫𝐞 𝐓𝐡𝐞 𝐊𝐢𝐧𝐠𝐬 𝐒𝐨 𝐖𝐡𝐨 𝐀𝐫𝐞 𝐲𝐨𝐮?\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐒𝐚𝐯𝐞𝐝 𝐈𝐧 ➞ : [ 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ]\n• 𝐏𝐡𝐨𝐧𝐞 ➞ : [ {phone} ]\n• 𝐁𝐲 ➞ : [ [ 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍🇮🇶 ] ](https://t.me/u4060)""")
                        r.delete("onn")
                    except Exception as e:
                         await message.reply_text(f'''• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐄𝐫𝐫𝐨𝐫 ➞ : \n\n{e}''') 
                         if "406 AUTH_KEY_DUPLICATED" in str(e):
                            with open("account.txt", "r") as file:
                                 lines = file.readlines()
                            with open("account.txt", "w") as file:
                                 for line in lines:
                                     if session not in line:
                                        file.write(line)
                            await app.send_message(message.chat.id, "𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐁𝐚𝐧 𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐞!")
                            pass
                         
    if message.text == 'd':
        start = time()
        m_reply = await message.reply_text("**pinging...**")
        delta_ping = time() - start
        await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")

#############################Group#########################################       
    if message.text == '⌞𝐑𝐮𝐧 𝐆𝐫𝐨𝐮𝐩⌝' or message.text == '⌝تشغيل جروب⌞':
            await message.reply_text(f"𝐃𝐨𝐧𝐞 𝐆𝐨 => @{wa}")
            clicks = 0              
            wa = open('user.txt', 'r').read()  
            ven = open("account.txt", "r").read().split("\n")[:-1]
            r.set('onnn',1)
            id = info.split('\n')[1]
            user = await app.get_users(id)
            first_name = user.first_name
            req = requests.get(f"https://t.me/{wa}").text
            if "tgme_username_link" not in req:
                await message.reply_text(f"𝐔𝐧 𝐅𝐥𝐨𝐨𝐝 => @{wa}")
                r.delete('onnn')
            while r.get('onnn'):  
                for session in ven:
                    if not r.get('onnn'):
                       break
                    try:
                        clicks+=1
                        t = Client("name_session", session_string=session, api_id=17765175, api_hash="e77878aa96e80375b1272e60f746bbf2")
                        await t.connect()
                        x = (await t.create_supergroup("𝐅𝐥𝐨𝐨𝐝 𝐊𝐢𝐧𝐠𝐬 #𝟏", "@Flood_kings \ @R_R_B0")).id                        
                        await asyncio.sleep(float(isl))
                        await t.set_chat_username(x, wa)
                        await t.send_video(x,video=f"https://t.me/vd_d_dd/39",caption=f"• 𝐒𝐨𝐫𝐫𝐲 𝐖𝐞 𝐊𝐢𝐧𝐠𝐬 𝐅𝐥𝐨𝐨𝐝!\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐇𝐮𝐧𝐭𝐞𝐝 𝐁𝐲 ➞ : {first_name}")
                        phone = (await t.get_me()).phone_number[:-2] + "xx"
                        await app.send_video(message.chat.id, "https://t.me/vd_d_dd/35", caption=f"""• 𝐖𝐞 𝐀𝐫𝐞 𝐓𝐡𝐞 𝐊𝐢𝐧𝐠𝐬 𝐒𝐨 𝐖𝐡𝐨 𝐀𝐫𝐞 𝐲𝐨𝐮?\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐒𝐚𝐯𝐞𝐝 𝐈𝐧 ➞ : [ 𝐆𝐫𝐨𝐮𝐩 ]\n• 𝐏𝐡𝐨𝐧𝐞 ➞ : [ {phone} ]\n• 𝐁𝐲 ➞ : [ [ 𝐓𝐄𝐀𝐌 𝐍𝐄𝐎𝐍🇪🇬 ] ](https://t.me/u4060)""")
                        r.delete("onnn")
                    except Exception as e:
                         await message.reply_text(f'''• 𝐂𝐥𝐢𝐜𝐤𝐬 ➞ : [ {clicks} ]\n• 𝐔𝐬𝐞𝐫 ➞ : [ @{wa} ]\n• 𝐄𝐫𝐫𝐨𝐫 ➞ : \n\n{e}''')   
                         if "406 AUTH_KEY_DUPLICATED" in str(e):
                            with open("account.txt", "r") as file:
                                 lines = file.readlines()
                            with open("account.txt", "w") as file:
                                 for line in lines:
                                     if session not in line:
                                        file.write(line)
                            await app.send_message(message.chat.id, "𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐁𝐚𝐧 𝐃𝐨𝐧𝐞 𝐃𝐞𝐥𝐞𝐭𝐞!")
                            pass
app.run
