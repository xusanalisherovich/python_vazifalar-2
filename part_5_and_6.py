# IF part-5
# Dasturlash ko'pincha shartlar to'plamini o'rganish va qaysi birini tanlashni o'z ichiga oladi
# ushbu shartlarga asoslanib harakat qilish. Python-ning if iborasi dasturning joriy holatini tekshirishga va 
# tegishli javob berishga imkon beradi

# if bilan ko'plab oson va murakkab shartlarni tuzishimiz mumkin
# if orqali qiyin shartlarni funksiyaga tiqib beramiz va bu ishhonada qolgan dasturchilar 
# uchun ham tushunarli va oson  buladi

# example

cars = ['audi', 'subaru', 'toyota']

for i in cars:
    if i == 'toyota':
        print('toyota'.upper())
    else:
        print(i.title())    
    print('sikl aylandi -------------\n')    

# natijani ko'rdingiz bu yerda for ni ichida 3ta qiymat aylanyapti yani bu 
# 3marta forni ichiadagi hamma funksiya ishlaydi degani  
# va siklni birinchi marta aylanganda 'audi' degan so'z chiqadi (buni hali forda yaxshi tushanasiz)
# demak audi ga teng bolganda if tekshiryapti bu toyoto emas if ishlamaganda else ishlaydi
# shu uchun ham bu yerda 1chi audi.title 2chi subaru.title va oxirida if ga toyoto mos keladi
# shuning uchun toyota.upper yani hammasi katta harflarda chiqadi

# == manabu 2ta tenglik esa berilayotgan qiymatga mosmi yoqmi tekshiradi

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

# bu yerda 2chi tekshirish belgisi o'rganamiz bu != agar teng bolmaganda degani
# yani shartni tekshirganda bir biriga mos kelmasa ishlaydi

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
    print("Hold the anchovies!")

# endi 2ta shartni birlashtiramiz

# and

if 2<3 and 3<4:
    print('2 kichkina 3dan va 3 kichkina 4dan')
else:
    print('hatolik')
 
# bu yerda if ishlaydi chunki tugri mantiq tuzdik
# lekin bittasi ishlab 2chisi ishlamasa else ishlaydi chunki bunda va deyapti yani bu va bu ishlasa degani

# faqat bittasi uchun qanyday kod yozsak buladi desangiz uni ham yoli bor
# or

# if 3<3 or 3<4:
#     print('3 3ga teng emas lekin 3 kichkina 4dan')
# else:
#     print('hatolik')

# Ro'yxatda qiymat bor yoki yo'qligini tekshirish
# Ba'zan biror chora ko'rishdan oldin ro'yxatda ma'lum qiymat mavjudligini tekshirish muhim. 
# Masalan, kimdirning veb-saytda ro'yxatdan o'tishini yakunlashdan oldin joriy foydalanuvchi nomlari ro'yxatida 
# yangi foydalanuvchi nomi allaqachon mavjudligini tekshirishni xohlashingiz mumkin. Xaritalash loyihasida siz 
# yuborilgan joylashuv ma'lum joylar ro'yxatida mavjudligini tekshirishni xohlashingiz mumkin.

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# biz if ni vazifasini tushundik yani shart beramiz togri bolsa ichidagi amallarni bajarishga otadi
# aks holda else keladi va bitta vazifa yoki suz bilan shartni yakunlaydi

# lekin biz kuplab shart bermoqchi bulsa elif dan foydalanamiz bu ketma ket ishlaydigan so'roq funksiyasi
# yani if ishlamasa elif u ham ishlamasa yana elif yoki else 
# elif ni hohlagancha yozsak buladi

age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $25.")
else:
 print("Your admission cost is $40.")

# misollar koramiz

age = 12
if age < 4:
    price = 0 
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings: 
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings: 
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#        print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")


# Dictiniory-Dict part-6

# Ushbu bobda siz Python lug'atlaridan qanday foydalanishni o'rganasiz, bu sizga imkon beradi
# tegishli ma'lumotlarning qismlarini ulang. Ma'lumotga ega bo'lgandan keyin qanday qilib kirishni o'rganasiz
# lug'atda va bu ma'lumotni qanday o'zgartirish mumkin.
# Chunki lug'atlar deyarli cheksiz narsalarni saqlashi mumkin
# ma'lumot miqdori, men sizga qanday qilib aylanishni ko'rsataman

# diktlar bizga judayam kerak albatta data scienceda kup malumotlar arrayda saqlanadi lekin pythonni boshqa
# yonalishlarida dict juda kop ishlatiladi 
# dickt bu kalit va uni qiymati
# passport misolida aytsak ham buladi jshr yani sizning shaxsiy raqamingizga koplab malumotlarni ulab quyishaadi
# dict - {} shunday qushtirnoq bilan yasaladi

# isimlar = {'Azamat': 17, 'Akmal': 36, 'komil': 24}
# bu yerda isimlar kalit soz va yoshlar ularni qiymati

# print(isimlar['Azamat'])
# endi men kalit soz orqali qiymatni olsam buladi

# qiymatga str list int bersak buladi 
# alien_0 = {'color': 'green'}
# print(alien_0['color'])

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# dictni uzimiz qolda toldirsak ham buladi

# dictni qiymatini uzgartirish
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points'] 
# print(alien_0)

# O'xshash ob'ektlar lug'ati
# Oldingi misol bitta ob'ekt, o'yindagi begona haqida turli xil ma'lumotlarni saqlashni 
# o'z ichiga olgan. Ko'p ob'ektlar haqida bir turdagi ma'lumotlarni saqlash uchun lug'atdan ham 
# foydalanishingiz mumkin. Misol uchun, siz bir nechta odamlarni so'roq qilmoqchi ekanligingizni 
# ayting va ulardan qaysi dasturlash tilini yoqtirishini so'rang. Lug'at oddiy so'rov 
# natijalarini saqlash uchun foydalidir, masalan:

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

language = favorite_languages['sarah'].title() 
print(f"Sarah's favorite language is {language}.")

# get() funksiyasi bor dictda bu bizga malumotlarni olib beradi [] huddi shunga uxshab faqat dictni qulayliklari bor

# Bu kabi xatolarni qanday hal qilish haqida 10-bobda koʻproq bilib olasiz. Lugʻatlar uchun, xususan, siz 
# soʻralgan kalit mavjud boʻlmasa qaytariladigan standart qiymatni belgilash uchun get() 
# usulidan foydalanishingiz mumkin.
# get() usuli birinchi argument sifatida kalitni talab qiladi. Ikkinchi ixtiyoriy 
# argument sifatida, agar kalit mavjud bo'lmasa, qaytariladigan qiymatni o'tkazishingiz mumkin:

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# bu yerda points abyekti yoq bulganligi uchun o'zimiz yozib quygan qiymatni chiqarib berdi

# dictda methodlar kop https://www.w3schools.com/python/python_ref_dictionary.asp bularni shu yerdan topsangiz buladi

# items method
# items ham kalit sozlarni ham qiymatni bitta tuple qilib chiqarib beradi
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.items()

# print(x)

# keys methods
# keys faqat kalit sozlarni chiqarib beradi
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.keys()

# print(x)

# values method
# values faqat qiymatlarni olib beradi
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.values()

# print(x)

# favorite_languages = {
#        'jen': 'python',
#        'sarah': 'c',
#        'edward': 'ruby',
#        'phil': 'python',
#        }

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title()) 
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2] 
# for alien in aliens:
#        print(alien)

# aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} 
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)
# print("...")

# bitta inson uchun juda katta malumot qushib tashlasak ham buladi bu uchun listni ham ishlatamiz

# azamats_information = {'Azamat Ergashev': ['Azamat','Ergashev',
#                                            {'otasi':'Avezov Erkin',
#                                             'onasi':'Davronova Nasiba',
#                                             },
#                                             {'proffessiyasi':'Dasturlash',
#                                              'python': 4}]}

# print(azamats_information['Azamat Ergashev'][2]['otasi'])

# ehh manashunaqa gaplar 😁
# BUguncha yetadi