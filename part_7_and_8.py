# input and while loop

# Ko'pgina dasturlar oxirgi foydalanuvchining muammosini hal qilish uchun yozilgan. 
# Buning uchun odatda sizga kerak bo'ladi
# foydalanuvchidan ba'zi ma'lumotlarni olish uchun

# input bizga terminalda asosan malunmot olish uchun ishlatiladi input bilan pythonda ishlatiladigan yozuv turlaridagi 
# malumotlar asosan olinadi

# message = input("menga nimadir ayting : ")
# print(message)

# Input() funksiyasi bitta argumentni oladi: foydalanuvchi nima qilish kerakligini bilishi uchun 
# biz ko'rsatmoqchi bo'lgan taklif yoki ko'rsatmalar. Ushbu misolda, 
# Python birinchi qatorni ishga tushirganda, foydalanuvchi menga biror 
# narsa ayting degan so'rovni ko'radi va men buni sizga takrorlayman: . 
# Dastur foydalanuvchi javobini kiritguncha kutadi va foydalanuvchi 
# Enter tugmasini bosgandan keyin davom etadi. Javob o'zgarmaydigan xabarga tayinlanadi, 
# keyin chop etish (xabar) foydalanuvchiga kiritilgan ma'lumotlarni ko'rsatadi:

# bu yerda malumotlar input() yozganimizda avtomatichiski str formatda oladi 
# nima bersak ham hozir ichiga nima bersak ham str oladi

# Aniq so'rovlarni yozish
# Input() funksiyasidan har safar foydalanganda foydalanuvchiga aynan qanday ma’lumotni 
# qidirayotganingizni ko‘rsatadigan aniq, bajarilishi oson so‘rovni kiritishingiz kerak. 
# Foydalanuvchiga nima kiritish kerakligini aytadigan har qanday bayonot ishlashi kerak. 
# Masalan:

# name = input("iltimos ismingizni yozing: ")
# print(f"\nSalom, {name}!")

# input() ichiga 'str' malumot yozsak buladi va bu foydalanuvchiga so'rov sifatida boradi

# bazi paytlarda so'rovni uzun qilish kerak boladi

# prompt = "If you tell us who you are, we can personalize the messages you see." 
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# age = input("How old are you? ")

# endi biz bu sonni str shaklida oldik va buni ustida matematik amallarni ishlatib bulmaydi 
# lekin buni yechimi bor

# age = int(input("How old are you? "))# kelayotgan malumotni ozimiz hoohlaga type otqazib olsak buladi

# print(f'yoshingiz {age} yilingiz {2024-age}')


# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")

# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# while loops

# For tsikli elementlar to'plamini oladi va to'plamdagi har bir element uchun bir marta kod blokini bajaradi. 
# Bundan farqli o'laroq, while tsikli ma'lum bir shart to'g'ri bo'lguncha while davom etadi.

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# HAR DOIM WHILE TRUE BULGANDA ISHLAYDI demak bu yerda 5dan kichik yoki teng bulsa true buladi 
# agar 5dan katta bulsa false va while ishalshdan tohtaydi


# Birinchi qatorda joriy_raqamga 1 qiymatini belgilash orqali biz 1 dan hisoblashni boshlaymiz. 
# So‘ngra while sikli joriy_raqam qiymati 5 dan kichik yoki unga teng bo‘lganda ishlashni davom ettiradigan 
# qilib o‘rnatiladi. Loop ichidagi kod qiymatini chop etadi. joriy_raqam va keyin joriy_raqam += 1 bilan 
# ushbu qiymatga 1 qo'shiladi. (+= operatori joriy_raqam = joriy_raqam + 1 ning qisqartmasi).
# Agar joriy_raqam <= 5 sharti to'g'ri bo'lsa, Python tsiklni takrorlaydi. 1 5 dan kichik bo'lganligi 
# sababli, Python 1 ni chop etadi va keyin 1 ni qo'shib, joriy raqamni 2 qiladi. 2 5 dan kichik bo'lgani 
# uchun Python 2 ni chop etadi va yana 1 ni qo'shib, joriy raqamni 3 ga aylantiradi va hokazo. 
# Joriy_raqam qiymati 5 dan katta bo'lsa, tsikl ishlashni to'xtatadi va dastur tugaydi:


# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# bu yerda message ni quit yani input qiymat quit bulmagancha davom etaveradi qayta qayta

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# while uzi asosan igralarda ishlatida va igradan chiqmaguncha 
# yana quit qimaguncha igra davom etishi uchun bizga yordam beradi

# va while kopincha virus yaratishda ishltiladi yani kutib yotadigan viruslar shunda qilinadi 
# misol
# a = input()
# if a == 'turn on':
#     while True:
#         print('virus virus virus\n')
# else:
#     print('still dont wake up')

# bunda aytayptiku usha qaysidir inson kamputeridagi qaysidir malumotni 
# ishga tushurganda virus ishga tushadi va komputerdagi hamma malumotlarni bizga qaytarib junatyapti

# current_number = 0
# while current_number < 10: 
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x= 1
# while x <= 5:
#        print(x)
#        x += 1


# whilega misollarni cheksiz korsak buladi lekin vaqt kam

# qiymat=0
# while qiymat != "exit":
#     qiymat = input()
#     print(int(qiymat) **2)
# print("Dastur tugadi")