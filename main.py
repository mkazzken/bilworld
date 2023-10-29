import telebot
from telebot import types





bot = telebot.TeleBot('6883811654:AAEu5yd4aJ4ESpGjPoYOyQtWFWbiBwpTuYA')





start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn1 = types.KeyboardButton('IELTS')
btn2 = types.KeyboardButton('SAT')
btn3 = types.KeyboardButton('NUET')
btn4 = types.KeyboardButton('BTS')
start_markup.row(btn1, btn2)
start_markup.row(btn3, btn4)

mainmenu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn1 = types.KeyboardButton('IELTS')
btn2 = types.KeyboardButton('SAT')
btn3 = types.KeyboardButton('NUET')
btn4 = types.KeyboardButton('BTS')
mainmenu_markup.row(btn1, btn2)
mainmenu_markup.row(btn3, btn4)

nazad_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
knopka = types.KeyboardButton('Артқа')  
nazad_markup.add(knopka)

ielts_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
cambr = types.KeyboardButton('Camrbridge Practice Tests')
longman = types.KeyboardButton('Longman Practice Tests')
ielts_markup.add(cambr, longman)


cambr_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False )
cambr1 = types.KeyboardButton('📘 Test Book 1')
cambr2 = types.KeyboardButton('📘 Test Book 2')
cambr3 = types.KeyboardButton('📘 Test Book 3')
cambr4 = types.KeyboardButton('📘 Test Book 4')
cambr5 = types.KeyboardButton('📘 Test Book 5')
cambr6 = types.KeyboardButton('📘 Test Book 6')
cambr7 = types.KeyboardButton('📘 Test Book 7')
cambr8 = types.KeyboardButton('📘 Test Book 8')
cambr9 = types.KeyboardButton('📘 Test Book 9')
cambr10 = types.KeyboardButton('📘 Test Book 10')
cambr11 = types.KeyboardButton('📘 Test Book 11')
cambr12 = types.KeyboardButton('📘 Test Book 12')
cambr13 = types.KeyboardButton('📘 Test Book 13')
cambr14 = types.KeyboardButton('📘 Test Book 14')
cambr15 = types.KeyboardButton('📘 Test Book 15')
cambr16 = types.KeyboardButton('📘 Test Book 16')
cambr17 = types.KeyboardButton('📘 Test Book 17')
nazd = types.KeyboardButton('Артқа')
cambr_markup.row(cambr1)
cambr_markup.row(cambr2)
cambr_markup.row(cambr3)
cambr_markup.row(cambr4)
cambr_markup.row(cambr5)
cambr_markup.row(cambr6)
cambr_markup.row(cambr7)
cambr_markup.row(cambr8)
cambr_markup.row(cambr9)
cambr_markup.row(cambr10)
cambr_markup.row(cambr11)
cambr_markup.row(cambr12)
cambr_markup.row(cambr13)
cambr_markup.row(cambr14)
cambr_markup.row(cambr15)
cambr_markup.row(cambr16)
cambr_markup.row(cambr17)
cambr_markup.row(nazd)

nazad_markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
knopka1 = types.KeyboardButton('Артқа')  
nazad_markup1.add(knopka1)


longman_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False )
long1 = types.KeyboardButton('📕 Plus 1')
long2 = types.KeyboardButton('📕 Plus 2')
long3 = types.KeyboardButton('📕 Plus 3')
backck = types.KeyboardButton('Артқа')
longman_markup.row(long1)
longman_markup.row(long2)
longman_markup.row(long3)
longman_markup.row(backck)  





@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Сәлем, {message.from_user.first_name} {message.from_user.last_name}, Мен BilBot сенімен Practice Test-термен бөлісуге дайынмын',
                     reply_markup=mainmenu_markup)
    bot.register_next_step_handler(message, on_click)




def on_click(message):
    if message.text == 'IELTS':
        bot.send_message(message.chat.id, 'Select', reply_markup=ielts_markup)
        bot.register_next_step_handler(message, ieltscheck)


    

    elif message.text == 'SAT':
        bot.send_message(message.chat.id, 'Қазіргі уақытта қол жетімді емес')
        mainmenu(message)

    elif message.text == 'NUET':
        bot.send_message(message.chat.id, 'Қазіргі уақытта қол жетімді емес')
        mainmenu(message)

    elif message.text == 'BTS':
        bot.send_message(message.chat.id, 'Қазіргі уақытта қол жетімді емес')
        mainmenu(message)


    elif message.text == 'Артқа':
        mainmenu(message)  




def ieltscheck(message):
    if message.text == 'Camrbridge Practice Tests':
        bot.send_message(message.chat.id, "Таңдаңыз", reply_markup=cambr_markup)
        bot.register_next_step_handler(message, ielts_sender)


        
    elif message.text == "Longman Practice Tests":
        bot.send_message(message.chat.id, "Таңдаңыз", reply_markup=longman_markup)
        bot.register_next_step_handler(message, longman_sender)


            
def longman_sender(message):
    for i in range(1, 4): 
        if message.text == f"📕 Plus {i}":
            bot.send_message(message.chat.id, 'Файл жіберілуде, күте тұрыңыз...')  # Send a processing message
            

            file_path1 = f'./Longman/IELTS Practice Tests Plus {i}.pdf'
            document1 = open(file_path1, 'rb')
            bot.send_document(message.chat.id, document1, on_click)
            bot.send_message(message.chat.id, 'Артқа', reply_markup=nazad_markup)
            bot.register_next_step_handler(message, mainmenu)
    
        elif message.text == "Артқа":
             mainmenu(message)
        


def ielts_sender(message):
    for i in range(1, 18): 
        if message.text == f"📘 Test Book {i}":
            bot.send_message(message.chat.id, 'Файл жіберілуде, күте тұрыңыз...')  # Send a processing message
            

            file_pathr = f'./ielts/IELTS Academic {i}.pdf'
            document = open(file_pathr, 'rb')
            bot.send_document(message.chat.id, document, on_click)
            bot.send_message(message.chat.id, 'Артқа', reply_markup=nazad_markup)
            bot.register_next_step_handler(message, mainmenu)
    
        elif message.text == "Артқа":
             mainmenu(message)
        
    
        

def mainmenu(message):
    bot.send_message(message.chat.id, 'Main Menu', reply_markup=mainmenu_markup)
    bot.register_next_step_handler(message, on_click)



bot.infinity_polling()




