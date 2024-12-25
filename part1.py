# starting pthon language 

# birinchi navbatta python uzi nima uchun 
# kerakligin bilib olishimiz kerak buladi

# Nima uchun Python?
# Har yili men Python-dan foydalanishni davom ettirishni yoki boshqa tilga o'tishni 
# o'ylab ko'raman - ehtimol bu dasturlash dunyosi uchun yangiroqdir. 
# Lekin men ko'p sabablarga ko'ra Pythonga e'tibor qaratishda davom etaman. 
# Python - bu juda samarali til: sizning dasturlaringiz boshqa tillarga 
# qaraganda kamroq kod qatorlarida ko'proq ishlaydi. Python sintaksisi ham sizga 
# "toza" kod yozishga yordam beradi. Sizning kodingizni o'qish oson, 
# disk raskadrovka qilish oson va boshqa tillarga nisbatan kengaytirilishi 
# va tuzilishi oson bo'ladi.
# Odamlar Python-dan ko'p maqsadlarda foydalanadilar: o'yinlar yaratish, veb-ilovalarni 
# yaratish, biznes muammolarini hal qilish va barcha turdagi qiziqarli 
# kompaniyalarda ichki vositalarni ishlab chiqish. Python, shuningdek, 
# ilmiy tadqiqotlar va amaliy ishlar uchun ilmiy sohalarda keng qo'llaniladi.
# Python-dan foydalanishni davom ettirayotganimning eng muhim 
# sabablaridan biri bu juda xilma-xil va mehmondo'st odamlar 
# guruhini o'z ichiga olgan Python hamjamiyatidir. 
# Hamjamiyat dasturchilar uchun juda muhim, chunki dasturlash yolg'iz ish emas. 
# Ko'pchiligimiz, hatto eng tajribali dasturchilar ham shunga o'xshash muammolarni 
# hal qilgan boshqalardan maslahat so'rashimiz kerak. Yaxshi bog'langan va 
# qo'llab-quvvatlovchi hamjamiyatga ega bo'lish muammolarni hal qilishda muhim 
# ahamiyatga ega va Python hamjamiyati siz kabi Pythonni birinchi dasturlash tilingiz 
# sifatida o'rganayotgan odamlarni to'liq qo'llab-quvvatlaydi.
# Python - o'rganish uchun ajoyib til, shuning uchun boshlaylik!

# biz birinchi orinda python install qilib olishimiz kerak
# terminalda ishlaayotganligini tekshiramiz

# yangi python fayl ochib olamiz
# python faylni nomlashda uz qoidalari bor 
# fayl nomi har doim (.py) bilan tugashi shart
# fayl nomini orasini ochib yoki birinchi harfini orniga 
# son bilan boshalb bolmaydi
# main.py✅ 1main.py❌ main takrorlash.py❌ 
# son bilan boshlasangiz qabul qilishi mumkin lekin haqiqy 
# ish topshirish masalasida eshik ni qayerdaligini korsatib 
# yuborishi mumkin shu uchun fayl nomini o'zingizga tushunarli qlib va 
# boshqa insonlar faylni korganda ham tushuni shart bulgan nomalrda foydalaning

# 1-print

# birinchi organadigan narsamiz bu print funksiyasi 
# bu funksiya bizga terminalga narsalarimizni chop etib beradi
# bu nima uchun kerak albatta biz birinchii urinda natijani korishimiz uchun
# va keyinchalik katta proectlarda biz xatolikni mijozga korsatmay yechishimiz uchun kerak

print('hello world')
# print("hello world")
# print(1234)
# print('12azamat')
# bularni farqini pastroqda str int typlar mavzusida koramiz

# vazifa salom sozini yozib chiqarish

# variables - o'zgaruvchilar
# bu mavzu eng kerakli mavzu chunki biz internet olamidagi hamma malumotlarimiz qandaydir 
# # o'zgaruvchilarda saqlanadi har doim

# message = 'hello world' 
# print(message)

# va biz natijani terminal orqali korishimiz mumkin
# nega printga message sozini yozdik va bizga message emas hello world sozi chiqdi
# chunki message o'zgaruvchimiz o'z ichida yani uzini portali qaysidir raqamli joyida 
# shu hello wrold degan sozni saqlayapti va biz printga message yani hello world 
# turgan partal kodini berdik desam ham boladi 

# hamma narsa ozini orniga ega moshinamizni raqamlari kabi 
# misol uchun man dars otayotgan joyimni ham raqamli manzili bor 
# meni ozim ham qandaydir raqamlar bilan davlat hisobida yani fuqorosi bulib turibman

# endi ozgaruvchilar ham bir joylashu manzili kabidir ularni juda kop ishlatamiz 
# va hozir sal tushunarsiz bulishi mumkin lekin qayta qayta yozgan sari
# nimaga kerakli ekanligini tushunib borasiz 
# 
# hop bunga yana misollar koramiz



# raqamlar = 12344
# list_toplami = [1,2,3,4,5]
# print(raqamlar)
# print(list_toplami)

# salom_xush = 'salomlar'
# hisoblash = 12334
# salomlar = 'salomlashuv'
# 
# agar print(ichiga) o'zgaruvchi nomini hato yozsangi hatto 
# bitta harfga bolsa ham terminal hato chiqaraveradi
# 
# list haqida ham typlar mavzusida keladi birozdan song
# o'zgaruvchilarni nomlash
# 
# birinchi o'rinda ularga python funksiyalari nomini qoyib bulmaydi misol uchun print va 
# intertetdan korsataman
# 
# type-lar
# str - string
# Ko'pgina dasturlar ma'lum turdagi ma'lumotlarni aniqlaganligi
# va to'plaganligi va keyin u bilan foydali narsalarni qilganligi
# sababli, u har xil turdagi ma'lumotlarni tasniflashga yordam
# beradi. Biz ko'rib chiqadigan birinchi ma'lumotlar turi - bu satr. 
# Stringlar birinchi qarashda juda oddiy, ammo siz ularni turli yo'llar 
# bilan ishlatishingiz mumkin.
# String - bu belgilar qatori. Qo'shtirnoq ichidagi har qanday
# narsa Python-da satr hisoblanadi va siz satrlaringiz
# atrofida bitta yoki ikkita tirnoqdan foydalanishingiz mumkin:

# 1) bittalik qosh tirnoq
# 'salom mening ismim azamat'
# 2) iktalik qosh tinnoq bilan
# "salom mening ismim azamat o'zbek"
# har bir typeda uzini medhodlari buladi
# buladi bizni ishimizni ancha yengil qilib berad 

# 3talik qushtirnoq 

# methodlar ozgaruvchidan keyin nuqta bilan yoziladi va oxirida qavs buladi
# 1) .title() - bu sarlavha yozib beradi
# name = 'hush kelibsiz'
# print(name.title())

# 2) .upper() - yozuvni katta qlib beradi
# 3) .lower() - yozuvni kichkina qilib beradi

# name = 'Amad Lome'
# print(name.upper())
# print(name.lower())

# bazi vaziyatlarda biz 2ta o'zgaruvchini bitta o'zgaruvchi ichiga yoki bitta 
# print ichiga yozgimiz keladi 
# bunday vaziyatarda biz f string funksiyasidan foydalansak buladi 
# biz f string ichiga o'zgaruvchi yozishimiz uchun {} qushtirnoqdan foydalanamiz

# first_name = 'azamat'
# last_name = 'ergashev'
# full_name = f"ismim {first_name} familyam {last_name}"
# print(full_name)
# yoki printni ichiga togridan togri yozishimiz mumkin

# print(f"ismim {first_name} familyam {last_name}")

# bu f - format sozini qisqartmasi va dasturlash olamida ham f-string nomiga ega

# firstname = 'ada'
# lastname = 'lovelace'
# full_name = f"{firstname} {lastname}"
# print(f"Hello, {full_name.title()}!")


# biz hozir print ichiga yozgan narsamizmi yana bir ozgaruvchi yaratib yozib
# quyishimiz mumkin va 
# print ichiga ayanan usha uzgaruvchini choqirib ishlatib quyishimiz kerak


# firstname = 'ada'
# lastname = 'lovelace'
# full_name = f"{firstname} {lastname}"
# message = f"Hello, {full_name.title()}!"
# print(message)

# python 3.6 versiyasidan song yana bir f-string yozish usuli chiqqan
# format yani f-stringni toliq yozilishi bilan bunday tarzda ham ishlatsak buladi
# full_name = "{} {}".format(first_name, last_name)
# print(full_name)

# boshliq (tab) yoki enter tashlash
# bularni biz \t va \n yordamida amalga oshiramiz

# print('salom\tpython')
# print('salom\npython')

# stringdagi yana bir method .rstrip() faqat oxiridagi boshliqni olib tashlaydi
# language = "  python  "
# print(language.rstrip())
# .lstrip() boshidan bosh joylarni oladi faqat
# print(language.lstrip())
# .strip() ikkkala tarafdagi boshliqlarni olib tashlaydi
# print(language.strip())

# syntax error

# Siz muntazam ravishda ko'rishingiz mumkin bo'lgan xatolardan
#  biri bu sintaksis xatosi. Sintaksis xatosi Python dasturingizning
#  biror qismini yaroqli Python kodi sifatida tanimasa paydo bo'ladi.
#  Masalan, bitta tirnoq ichida apostrofdan foydalansangiz, xatoga yo'l
#  qo'yasiz. Buning sababi, Python birinchi qo'shtirnoq va apostrof
#  o'rtasidagi hamma narsani satr sifatida talqin qiladi. Keyin
#  matnning qolgan qismini Python kodi sifatida izohlashga harakat qiladi,
#  bu esa xatolarga olib keladi.

# message = "One of Python's strengths is its diverse community."
# print(message)
# bu kodda hatolik yoq chunki 2talik qush tirnoq ichiga bittalik qushtirnoq yozsa boladi

# message = 'One of Python's strengths is its diverse community.'
# print(message)

# lekin bunda hatolik chiqadi 

#  File "apostrophe.py", line 1
#     message = 'One of Python's strengths is its diverse community.'
# ^ SyntaxError: invalid syntax
# sizda ham shunga uxshash hatolar bulishi mumkin 

# hatolik qushtinoq ochilda va yopilda va yana qushtirnoq ochildi '  '   ', "   "   " 
# kod huddi shunga uxshab qaoldi va bu katta xato 
# python biz kodni yopdik deb uylaydi va keyingi kelayotgan narsani tushunamaydi
# misol

# o'zingiz sinab ko'ring - vazifa(1)

# Quyidagi mashqlarning har birini name_cases.py kabi nom bilan alohida fayl sifatida saqlang. Agar tiqilib qolsangiz, tanaffus qiling yoki C ilovasidagi tavsiyalarni ko'ring.
# 2-3. Shaxsiy xabar: shaxsning ismini ifodalash uchun o'zgaruvchidan foydalaning va u kishiga xabarni chop eting. Sizning xabaringiz oddiy bo'lishi kerak, masalan: "Salom Erik, bugun Python tilini o'rganmoqchimisiz?"
# 2-4. Ism hollari: Biror kishining ismini ifodalash uchun o'zgaruvchidan foydalaning, so'ngra bu shaxsning ismini kichik, katta va sarlavhali harflar bilan chop eting.
# 2-5. Mashhur iqtibos: Sizni hayratga soladigan mashhur odamning iqtibosini toping. Iqtibos va uning muallifining ismini chop eting. Sizning chiqishingiz quyidagi kabi ko'rinishi kerak, jumladan, tirnoq belgilari:
# Albert Eynshteyn shunday degan edi: "Hech qachon xato qilmagan odam hech qachon yangi narsani sinab ko'rmaydi".
# 2-6. Mashhur iqtibos 2: 2-5-mashqni takrorlang, lekin bu safar mashhur_shaxs deb nomlangan o'zgaruvchidan foydalanib mashhur odamning ismini ifodalang. Keyin xabaringizni tuzing va uni xabar deb nomlangan yangi o'zgaruvchi bilan ifodalang. Xabaringizni chop eting.
# 2-7. Ismlarni olib tashlash: shaxs nomini ifodalash uchun o'zgaruvchidan foydalaning va ismning boshi va oxirida bir nechta bo'sh joy belgilarini qo'shing. Har bir belgi birikmasidan, "\t" va "\n"dan kamida bir marta foydalanganingizga ishonch hosil qiling.
# Ismni bir marta chop eting, shuning uchun nom atrofidagi bo'sh joy ko'rsatiladi. Keyin lstrip(), rstrip() va strip() uchta yaroqsiz funksiyasidan foydalanib nomni chop eting.

