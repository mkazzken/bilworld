
from aiogram import F, Router, types, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, callback_query
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import TOKEN

import app.keyboards as kb

bot = Bot(token=TOKEN)

router = Router()


class SAT(StatesGroup):
    region = State()
    year = State()
    month = State()



def sub_check(result):
    
    if result.status in ['member', 'administrator', 'creator']:
        return True
    else:
        return False

@router.message(CommandStart())
async def cmd_start(message: Message):
    result = await bot.get_chat_member(chat_id='@bil_world', user_id=message.from_user.id)
    if sub_check(result):
        await message.answer('Сәлем мен BIL_bot-пын. Өзіңе керек тесттерді таңда')
        await menu(message)
    else:
        await message.answer('Ботты қолдану үшін арнамызға жазылыңыз', reply_markup=kb.subscribe)


@router.callback_query(F.data == 'subs')
async def subscriber(callback: callback_query):
    result = await bot.get_chat_member(chat_id='@bil_world', user_id=callback.from_user.id)
    
    if result.status in ['member', 'administrator', 'creator']:
        await callback.message.answer('Сәлем мен BIL_bot-пын. Өзіңе керек тесттерді таңда')
        await menu(callback)
    else:
        await callback.message.answer('Ботты қолдану үшін арнамызға жазылыңыз', reply_markup=kb.subscribe)
        await callback.message.delete()




@router.message(F.text == 'Motivational letter')
async def aa(message: Message):
    await message.answer('Қазіргі уақытта қолжетімді емес😢...', reply_markup=kb.main)


async def menu(message: Message):
    await message.answer('Main menu', reply_markup=kb.main)


@router.message(F.text == 'Артқа')
async def exitmenu(message: Message):
    await menu(message)



@router.message(F.text == 'IELTS')
async def ielts_menu(message: Message):
    if await subscriber1(message):
        await message.answer('Таңдаңыз', reply_markup=kb.ielts)


@router.message(Command('help'))
async def get_help(message: types.Message):
    await message.answer("this command is hjelp")


@router.message(lambda message: message.text.startswith('IELTS Academic'))
async def academ_sender(message: types.Message):
    try:
        number = int(message.text.split()[-1])
        file_path = f'ielts/IELTS Academic {number}.pdf'
        document = types.FSInputFile(file_path)
        await message.answer('Күте тұрыңыз файл жіберілуде (бұл біраз уақыт алуы мүмкін)... ')
        await message.answer_document(document, reply_markup=kb.nazad)
    except (ValueError, FileNotFoundError):
        await message.reply("oops oops puki puki")


@router.message(F.text == 'SAT')
async def aa(message: Message, state: FSMContext):
    if await subscriber1(message):
        await state.set_state(SAT.region)
        await message.answer('Таңдаңыз', reply_markup=kb.sat)

@router.message(SAT.region)
async def region(message: Message, state: FSMContext):
    await state.update_data(region=message.text)
    await state.set_state(SAT.year)
    await message.answer('Таңдаңыз', reply_markup=kb.years_kb)

@router.message(SAT.year)
async def year(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    await state.set_state(SAT.month)
    await message.answer('Таңдаңыз', reply_markup=kb.month_kb)

@router.message(SAT.month)
async def month(message: Message, state: FSMContext):
    await state.update_data(month=message.text)
    data = await state.get_data()
    await state.clear()
    region = data["region"]
    year = data["year"]
    month = data["month"]

    try:
        sat_file_path = f'SAT/{region}/{year}/{month}.pdf'
        sat_document = types.FSInputFile(sat_file_path)
        await message.answer('Күте тұрыңыз файл жіберілуде (бұл біраз уақыт алуы мүмкін)...')
        await message.answer_document(sat_document, reply_markup=kb.nazad)

    except FileNotFoundError:
        await message.reply("Өкінішке орай біздің базада жоқ😢")
        await menu(message)

    except Exception as e:
        await message.reply(f"Өкінішке орай біздің базада жоқ😢")
        await menu(message)


async def subscriber1(message: Message) -> bool:
    result = await bot.get_chat_member(chat_id='@bil_world', user_id=message.from_user.id)
    
    if result.status in ['member', 'administrator', 'creator']:
        return True
    else:
        await message.answer('Ботты қолдану үшін арнамызға жазылыңыз', reply_markup=kb.subscribe)
        await message.delete()
        return False