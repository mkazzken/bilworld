from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

main = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text= 'IELTS'), KeyboardButton(text= 'SAT')],
    [KeyboardButton(text= 'Motivational letter')],
], resize_keyboard = True, input_field_placeholder= 'Таңдаңыз')

ielts = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text= 'IELTS Academic 1')],
    [KeyboardButton(text= 'IELTS Academic 2')],
    [KeyboardButton(text= 'IELTS Academic 3')],
    [KeyboardButton(text= 'IELTS Academic 4')],
    [KeyboardButton(text= 'IELTS Academic 5')],
    [KeyboardButton(text= 'IELTS Academic 6')],
    [KeyboardButton(text= 'IELTS Academic 7')],
    [KeyboardButton(text= 'IELTS Academic 8')],
    [KeyboardButton(text= 'IELTS Academic 9')],
    [KeyboardButton(text= 'IELTS Academic 10')],
    [KeyboardButton(text= 'IELTS Academic 11')],
    [KeyboardButton(text= 'IELTS Academic 12')],
    [KeyboardButton(text= 'IELTS Academic 13')],
    [KeyboardButton(text= 'IELTS Academic 14')],
    [KeyboardButton(text= 'IELTS Academic 15')],
    [KeyboardButton(text= 'IELTS Academic 16')],
    [KeyboardButton(text= 'IELTS Academic 17')]
    ], resize_keyboard=True, 
    input_field_placeholder= 'You can scroll down')
    
nazad = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Артқа')]], resize_keyboard=True)





sat = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text= 'International'), KeyboardButton(text= 'USA')],
    [KeyboardButton(text= 'Артқа')],
    
], resize_keyboard = True, input_field_placeholder= 'Choose')




years_kb = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text= '2016'), KeyboardButton(text= '2017')],
    [KeyboardButton(text= '2018'), KeyboardButton(text= '2019')],
    [KeyboardButton(text= '2020'), KeyboardButton(text= '2021')],
    [KeyboardButton(text= '2022')], 
    [KeyboardButton(text= 'Артқа')],


], resize_keyboard = True, input_field_placeholder= 'Choose')


month_kb = ReplyKeyboardMarkup(keyboard=[ 
    [KeyboardButton(text= 'January')],
    [KeyboardButton(text= 'March')],
    [KeyboardButton(text= 'May')],
    [KeyboardButton(text= 'August')],
    [KeyboardButton(text= 'September')],
    [KeyboardButton(text= 'October')],
    [KeyboardButton(text= 'November')],
    [KeyboardButton(text= 'December')],
    [KeyboardButton(text= 'Артқа')],
], resize_keyboard = True, input_field_placeholder= 'You can scroll down')



subscribe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Жазылу🔗', url='https://t.me/bil_world')],
    [InlineKeyboardButton(text='Жазылдым✅',  callback_data='subs')],

])