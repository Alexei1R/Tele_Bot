from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="start")
        ],

        [
            KeyboardButton(text="help")
        ],

    ],
    resize_keyboard=True
)