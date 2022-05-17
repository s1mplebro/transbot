import logging
from config import *
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.types import CallbackQuery
from googletrans import Translator
import sqlite3
from classes import *

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
tr = Translator()
db = Sql()
Admin = 805235258
@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    db.baza_create()
    global user_id
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    data1 = db.user_id(user_id)
    if data1 is None:
        db.user_add(user_id,username,first_name)
    await message.reply(f"<strong>{message.from_user.full_name} 🇺🇿Botga xush kelibsiz,Matnni istalgan tilda kiriting, biz uni istalgan tilga tarjima qilamiz!n  </strong>\n \n <strong>{message.from_user.full_name} 🇷🇺Добро пожаловать в наш бот, Введите любой текст на любом языке мы его переведем в любой доступный язык! </strong> <strong>\n \n 🏴󠁧󠁢󠁥󠁮󠁧󠁿Hello {message.from_user.full_name}, Enter text in any language, we will translate it into any available language!</strong>",parse_mode='HTML',reply_markup=menu)
    await bot.send_message(Admin,f"id Пользователя: {user_id} Его юзернейм {username} ")

    

@dp.callback_query_handler(text="back")
async def send_welcome(call: CallbackQuery):
    await call.message.answer(f"<strong>{call.message.from_user.full_name} 🇺🇿Botga xush kelibsiz,Matnni istalgan tilda kiriting, biz uni istalgan tilga tarjima qilamiz!n  </strong>\n \n <strong>{call.message.from_user.full_name} 🇷🇺Добро пожаловать в наш бот, Введите любой текст на любом языке мы его переведем в любой доступный язык! </strong> <strong>\n \n 🏴󠁧󠁢󠁥󠁮󠁧󠁿Hello {call.message.from_user.full_name}, Enter text in any language, we will translate it into any available language!</strong>",parse_mode='HTML',reply_markup=menu)


@dp.message_handler(commands=['allusers'],user_id = 805235258)
async def send_welcome(message: types.Message):
    fo1 = db.sana()
    for i in fo1:
        b = i[0]
        await message.reply(f"Foydalanuvchilar soni {b} ta")

@dp.message_handler(commands=['reklama'],user_id = 805235258)
async def send_welcome(message: types.Message):
    rek1 = db.reklama()
    for j in rek1:
        user_id = j[0]
        await bot.send_message(chat_id = user_id,text = f"Assalom aleykum obunachilarimiz Sizlarga tavsiya qilib qolamiz\nKreativni motivatsiyali kanal kirib ko'rishingiz mumkin\nSizlarga yoqadigan umidaman\nKanal: https://t.me/sherbekblog")


@dp.callback_query_handler(text='begn')
async def perevd(call: CallbackQuery):
    await call.message.reply("<em>🇷🇺Введите любой текст, бот переведет его на доступные языки \n \n 🇬🇧Enter any text, the bot will translate it into available languages \n \n 🇺🇿Har qanday matnni kiriting, bot uni mavjud tillarga tarjima qiladi</em>",parse_mode='HTML')

@dp.callback_query_handler(text='writ')
async def perevd(call: CallbackQuery):
    await call.message.answer("<em>🇷🇺Если у вас есть какие то пожелания или идеи: @zaliv_dev </em>",parse_mode='HTML')

'''
@dp.message_handler(commands=['myinfo'])
async def send_welcome(message: types.Message):
     await message.reply(f"Ваш chat id: {user_id} \nВаше имя:{first_name} Ваше юзернейм {username} ")
'''
@dp.message_handler(commands=['info'])
async def send_welcome(message: types.Message):
    await message.answer("If you have any idea please write to @zaliv_dev")



@dp.message_handler()
async def send_welcome(message: types.Message):
    global t
    t = message.text
    await message.reply("<b>🇷🇺Доступные языки для перевода: \n 🇬🇧Available languages for translate: \n 🇺🇿Tarjima uchun mavjud tillar:</b>" ,parse_mode='HTML',reply_markup=langs)

@dp.callback_query_handler(text='rus')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="ru")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='eng')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="en")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='uzb')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="uz")
    await call.message.reply(tarj.text)
    


@dp.callback_query_handler(text='afr')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="af")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='ara')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ar")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='arm')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="hy")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='aze')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="az")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='bel')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="be")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='bul')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="bg")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='chi')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="zh-tw")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='cro')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="co")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='deu')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="nl")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='fre')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="fr")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='geo')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ka")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='det')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="de")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='alb')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="sq")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='amh')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="am")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='bng')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="bn")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='bos')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="bs")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='cta')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ca")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='seb')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="ceb")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='bas')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="eu")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='chichi')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ny")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='cors')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="co")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='chez')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="cs")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='dani')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="da")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='espa')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="eo")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='eston')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="et")
    await call.message.answer(tarj.text)
@dp.callback_query_handler(text='filip')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="tl")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='finn')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="fi")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='grek')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="el")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='gat')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ht")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='hasua')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="ha")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='izra')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="iw")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='hind')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="hi")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='iceland')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="is")
    await call.message.reply(tarj.text)

#######################################

@dp.callback_query_handler(text='igbo')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="ig")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='indo')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="id")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='irish')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="ga")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='ital')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="it")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='japan')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ja")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='canada')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="kn")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='javas')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="jw")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='kaza')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="kk")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='korea')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="ko")
    await call.message.reply(tarj.text)
############################

@dp.callback_query_handler(text='kgz')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="ky")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='latva')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="lo")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='luxem')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="lb")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='mace')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="mk")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='mala')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="ms")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='mongo')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="mn")
    await call.message.reply(tarj.text)
###
@dp.callback_query_handler(text='pers')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="fa")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='polsh')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="pl")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='port')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="pt")
    await call.message.reply(tarj.text)


@dp.callback_query_handler(text='roman')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="ro")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='serb')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="sr")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='span')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="es")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='tj')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="tg")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='swed')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="sv")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='turk')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="tr")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='uy')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="ug")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='viet')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="vi")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='som')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="so")
    await call.message.reply(tarj.text)

@dp.callback_query_handler(text='slov')
async def perevdrus(call: CallbackQuery):
    tarj = tr.translate(t,dest="sl")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='thai')
async def perevden(call: CallbackQuery):
    tarj = tr.translate(t,dest="th")
    await call.message.reply(tarj.text)
@dp.callback_query_handler(text='ukr')
async def perevd(call: CallbackQuery):
    tarj = tr.translate(t,dest="uk")
    await call.message.reply(tarj.text)











if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)