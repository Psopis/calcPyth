import asyncio
import pprint
from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor

loop = asyncio.get_event_loop()
mere = MemoryStorage()
bot = Bot("1750619081:AAHGHAfO-aNp6yg-TKW41UP-88b1OWp8lXk")
dp = Dispatcher(bot, loop=loop, storage=mere)
operations = ["+", "-", "*", "/"]
btnPlus = KeyboardButton("+")
btnMinus = KeyboardButton("-")
btnUmnozh = KeyboardButton("*")
btnDelen = KeyboardButton("/")
btnProc = KeyboardButton("%")
menuCalc = ReplyKeyboardMarkup(resize_keyboard=True).add(btnPlus, btnMinus, btnUmnozh, btnDelen,btnProc)


class Form(StatesGroup):
    first = State()
    second = State()
    third = State()


@dp.message_handler(commands="start")
async def start(message: Message):
    await message.answer("первое саня")
    await Form.first.set()


@dp.message_handler(state=Form.first)
async def start(message: Message, state: FSMContext):
    await message.answer("второе саня")
    await state.update_data(firstNum=message.text)

    await Form.second.set()


@dp.message_handler(state=Form.second)
async def start(message: Message, state: FSMContext):

    await state.update_data(secNum=message.text)
    await message.answer("операция саня", reply_markup=menuCalc)
    await Form.third.set()


@dp.message_handler(state=Form.third)
async def start(message: Message, state: FSMContext):

    data = await state.get_data()
    for i in operations:
        if message.text == i:
            await message.answer(f"саня  это  -  {eval(data['firstNum']+ i +data['secNum'])}")

    await state.finish()


executor.start_polling(dispatcher=dp)


