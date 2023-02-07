from aiogram import Bot, Dispatcher, executor, types
from settings import token
import json
from aiogram.dispatcher.filters import Text
from main import checking_updates1, checking_updates2, checking_updates3


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


# ALL ADS
@dp.message_handler(commands=['start'])
async def all_ads(message: types.Message):
    
    # first site
    with open('ads_dict1.json', encoding='utf-8') as f_file:
        ads_dict1 = json.load(f_file)

    for k, v in sorted(ads_dict1.items())[-10:]:
        ads1 = f"<b>{v['ad_time']}</b>\n<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>\n{v['ad_url']}"
        await message.answer(ads1)

    smile = '\U00002934' 
    await message.answer(f'Отправил последние 10 объявлений из первого сайта{smile}')

    # second site
    with open('ads_dict2.json', encoding='utf-8') as s_file:
        ads_dict2 = json.load(s_file)

    for k, v in sorted(ads_dict2.items())[-10:]:
        ads2 = f"<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>\n{v['ad_url']}"
        await message.answer(ads2)

    await message.answer(f'Отправил последние 10 объявлений из второго сайта{smile}')

    # third site
    with open('ads_dict3.json', encoding='utf-8') as t_file:
        ads_dict3 = json.load(t_file)

    for k, v in sorted(ads_dict3.items())[-10:]:
        ads3 = ads1 = f"<b>{v['ad_time']}</b>\n<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>|{v['ad_metro']}\n{v['ad_url']}"
        await message.answer(ads3)

    await message.answer(f'Отправил последние 10 объявлений из третьего сайта{smile}')

    # reply keyboard
    start_button = ['Свежие объявления']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer('Для получения свежих объявлений, нажми на кнопку "Свежие объявления"', reply_markup=keyboard)
    


# FRESH ADS
@dp.message_handler(Text(equals='Свежие объявления'))
async def fresh_ads(message: types.Message):
   
    # first site   
    new_ads1 = checking_updates1()

    if len(new_ads1) >= 1:
        for k, v in sorted(new_ads1.items()):
            ads1 = f"<b>{v['ad_time']}</b>\n<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>\n{v['ad_url']}"
            await message.answer(ads1)
    else:
        await message.answer('Пока нет свежих объявлений из первого сайта...')
    
    # second site
    new_ads2 = checking_updates2()

    if len(new_ads2) >= 1:
        for k, v in sorted(new_ads2.items()):
            ads2 = f"<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>\n{v['ad_url']}"
            await message.answer(ads2)
    else:
        await message.answer('Пока нет свежих объявлений из второго сайта...')

    # third site
    new_ads3 = checking_updates3()

    if len(new_ads3) >= 1:
        for k, v in sorted(new_ads3.items()):
            ads3 = ads1 = f"<b>{v['ad_time']}</b>\n<u>{v['ad_title']}</u>\n<code>{v['ad_desc']}</code>\n<b>{v['ad_salary']}</b>|{v['ad_metro']}\n{v['ad_url']}"
            await message.answer(ads3)
    else:
        await message.answer('Пока нет свежих объявлений из третьего сайта...')




if __name__ == '__main__':
    executor.start_polling(dp)