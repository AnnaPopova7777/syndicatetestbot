from aiogram import F, Router
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, InputMediaVideo, FSInputFile
import keyboard as kb

router = Router()


@router.message(CommandStart())
async def com_start(message: Message):
    video = FSInputFile(r'C:\Users\epicg\PycharmProject\pythonProject1\syndicatetestbot2\video\jetton_logo_rus.mp4')

    await message.answer_video(video=video,
                               caption=
                               "🎰 Более 10 000 игр: слоты, краш, покер, 3D-экшн, live-игры\n\n"
                               "💰 Моментальные выплаты\n\n"
                               "🎁 200% бонус на первый депозит + 200 бесплатных вращений\n\n"
                               "🏆 Еженедельные турниры с призовым фондом до $100 000!\n\n"
                               "📞 Поддержка 24/7, отвечаем в течение 30 секунд\n\n"
                               "👑 VIP-клуб и эксклюзивные привилегии",
                               reply_markup=kb.start_game)
