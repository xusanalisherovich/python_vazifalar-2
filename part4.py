# working with list 

# Butun ro'yxat bo'ylab looping
# Siz har bir element bilan bir xil vazifani bajarib, ko'pincha ro'yxatdagi barcha yozuvlarni ko'rib chiqishni
# xohlaysiz. Misol uchun, o'yinda siz ekrandagi har bir elementni bir xil miqdorda ko'chirishingiz
# mumkin yoki raqamlar ro'yxatida har bir elementda bir xil statistik operatsiyani 
# bajarishingiz mumkin. Yoki veb-saytdagi maqolalar ro'yxatidan har bir sarlavhani ko'rsatishni 
# xohlaysiz. Roʻyxatdagi har bir element bilan bir xil amalni bajarmoqchi boʻlsangiz, Python’s for 
# loop-dan foydalanishingiz mumkin.

# Aytaylik, bizda sehrgarlarning ismlari ro'yxati bor va biz ro'yxatdagi har bir ismni 
# chop qilmoqchimiz. Buni roʻyxatdagi har bir nomni alohida olish orqali amalga oshirishimiz 
# mumkin, ammo bu yondashuv bir qancha muammolarni keltirib chiqarishi mumkin. Biri uchun,
# buni ismlarning uzun ro'yxati bilan qilish takrorlanadi. Bundan tashqari, har safar ro'yxat 
# uzunligi o'zgarganda kodimizni o'zgartirishimiz kerak bo'ladi. For loop Python-ga ushbu muammolarni 
# ichki boshqarish imkonini berib, bu ikkala muammodan qochadi.
# Sehrgarlar ro'yxatidagi har bir nomni chop etish uchun for tsiklidan foydalanamiz:

# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians:
#     print(magician)

# A Closer Look at Looping
# pythoning for methodi bizga har bir elementni aloxida oqishga yordam beradi 
# bu haqda addelni dars buladi lekin bu kitobda list ishlatish uchun berib ketgan ekan 
# hzoircha chuqur bilish shartmas asosiy etiborni listga qaratavering

# for va unga tegishli uzgaruvchi yaratamiz bu uzgaruvchi har aylanga aloxida narsani oladi
# for sonlarni qabul qilmaydi lekin listni oladi va listni ichidagi elementni aloxida element deb qaraydi

# ismlar = ['alisher','asad','sardor','qodir']
# for ism in ismlar:
#     print(ism)

# bu yordamida xar bir elementga narsa qushsak buladi
# misol hammasini familyasi bir xil bulsa

# ismlar = ['alisher','asad','sardor','qodir']
# for ism in ismlar:
#     print(ism+' Ergashev')


# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# range funksiyasi bizga sonlarni jadvalini yasab beradi desak buladi
# bu yordamida sonlarni qulda yozishimiz shar bumay qoladi
# kop hollarda for bilan ishlatiladi

# for i in range(1,10):
#     print(i)

# ammo list qilib ham ishlatsak buladi bir uzini ishlatsak hech qanday uzgarishsiz uzi chiqib qoladi

# print(range(1,10))

# endi listga qaytsak 😂

# listni ichidagilarni olishni aytgandim ushani yana bir kursak
# misol list bitta lik emas 2d 3d listlar bor ularni ham ichidagi elementlarni olishmiz kerak

# d1 = [1,2,3,4,5]
# print(d1[0])

# d2 = [[2,3,4,5], [1,2,3,4,5]]
# print(d2[0][0])

# d3 = [[2,3,4,5], [1,2,3,4,5, ['azamat']]]
# print(d3[1][5][0])

# hullas buguncha qisqa darsimiz shu lekin zerikib qomasliglariz uchun qisqa kod yasaymiz

