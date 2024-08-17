from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

start_game = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Играть💰', web_app=WebAppInfo(url='https://ocean.demo-stage.com/?lang=ru'))]
])