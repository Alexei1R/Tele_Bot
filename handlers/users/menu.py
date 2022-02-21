from  loader import dp
from  aiogram.types import Message
from  keyboards.default import menu
from  aiogram.dispatcher.filters import Command,Text

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Alegeti functia dorita",reply_markup=menu)


@dp.message_handler(Text(equals=["start" , "help"]))
async def get_comand(message: Message):
    await message.answer(f"Dumneavoastra ati ales {message.text}.")