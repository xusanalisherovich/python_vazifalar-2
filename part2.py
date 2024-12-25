# integer - raqamlar 

# Raqamlar dasturlashda ko'pincha o'yinlarda ballni saqlash, 
# vizualizatsiyada ma'lumotlarni aks ettirish, veb-ilovalarda 
# ma'lumotlarni saqlash va hokazolar uchun ishlatiladi. 
# Python raqamlarni qanday ishlatilishiga qarab turli xil 
# usullarda ko'rib chiqadi. Keling, avval Python butun sonlarni 
# qanday boshqarishini ko'rib chiqaylik, chunki ular bilan ishlash 
# eng oddiy.

# integer yani sonlar bilan siz qushish(+) ayirish (-) kopaytirish(*) va bolish(/)
# shulardan foydalansangiz buladi

# terminaldagi misollar
# 3+3, 1+2, 3+4
# 1/5, 3/6, 4/7
# 10-5,11-12,100-1
# 10*2, 2*100

# Floats - kasr sonlar
# nuqta hammasi float turiga kiradi pytohnda

# Python kasrli har qanday raqamni float deb ataydi. 
# Ushbu atama ko'pchilik dasturlash tillarida qo'llaniladi va 
# u kasrli nuqta raqamning istalgan pozitsiyasida paydo bo'lishi 
# mumkinligini anglatadi. Har bir dasturlash tili o'nlik sonlarni 
# to'g'ri boshqarish uchun ehtiyotkorlik bilan ishlab chiqilgan bo'lishi kerak, 
# shuning uchun o'nli kasr qayerda paydo bo'lishidan qat'i nazar, raqamlar mos 
# ravishda harakat qiladi.

# 0.100000000

# terminal misollar

# >>> 0.1 + 0.1 
# 0.2
# >>> 0.2 + 0.2 
# 0.4
# >>> 2 * 0.1 
# 0.2
# >>> 2 * 0.2 
# 0.4

# Ammo shuni yodda tutingki, siz ba'zan 
# javobingizda o'nli kasrlarning ixtiyoriy sonini olishingiz mumkin:

# >>> 0.2 + 0.1 
# 0.30000000000000004 
# >>> 3 * 0.1 
# 0.30000000000000004

# comment yozish
#  biz kodlarimizni yoki kodlarni sharhlarini comentga olib yozsak buladi
# agar togrida togri yozsak hatolik yuz berishi mumkin

# kamentariya hamma dasturlash tilida har hil yoziladi lekin pytthon dasturlash tilida 
# komentariya (#) qoshtirnoq yordamida ochiladi

# say hello world 
# print('say hello world') 

# o'zingiz sinab ko'ring(vazifa-2)

# Sharh qo'shish: Siz yozgan dasturlardan ikkitasini tanlang va 
# har biriga kamida bitta sharh qo'shing. Agar hozirda dasturlaringiz 
# juda oddiy bo'lgani uchun yozish uchun maxsus biror narsangiz bo'lmasa, 
# har bir dastur faylining yuqori qismiga ismingiz va joriy sanani qo'shing. 
# Keyin dastur nima qilishini tavsiflovchi bitta jumla yozing.


# import 
# Pythonning Zeni
# Tajribali Python dasturchilari sizni murakkablikdan qochishga va 
# iloji boricha soddalikka intilishga undaydi. Python hamjamiyatining 
# falsafasi Tim Petersning "Python Zeni" asarida mavjud. Yaxshi Python kodini 
# yozish uchun ushbu qisqacha tamoyillar to'plamiga importni tarjimoningizga kiritish 
# orqali kirishingiz mumkin. Men bu erda "Python Zeni" ni to'liq takrorlamayman, 
# lekin Python dasturchisi sifatida nima uchun ular siz uchun muhim bo'lishi kerakligini 
# tushunishga yordam berish uchun bir nechta satrlarni baham ko'raman.


# >>> import this
# The Zen of Python, by Tim Peters 
# Beautiful is better than ugly.

# Uzoq raqamlarni yozayotganda, katta raqamlarni o'qilishi 
# mumkin bo'lgan pastki chiziq yordamida raqamlarni guruhlashingiz mumkin:

# raqam = 123_345_605
# print(raqam)

# natijani kordingiz demak bunday korinishda raqamlarni 
# yozganda python hatolik chiqarmas ekan python bunday vaziyatda 
# faqat raqamlarni taniydi

#  siz bir qator yozdamida 3 4 ta o'zgaruvchi ochib va ularga alohida qiymat 
# berishingiz mumkin buladi

# a, b, c = 1,2,3

# print(a)

# Konstantalar
# Konstanta o'zgaruvchiga o'xshaydi, uning qiymati dasturning butun 
# hayoti davomida bir xil bo'lib qoladi. Pythonda o'rnatilgan doimiy 
# turlar mavjud emas, lekin Python dasturchilari o'zgaruvchiga 
# doimiy sifatida qaralishi va hech qachon o'zgartirilmasligi 
# kerakligini ko'rsatish uchun barcha bosh harflardan foydalanadi:

# O'zgaruvchini kodingizda doimiy sifatida ko'rib c
# hiqmoqchi bo'lsangiz, o'zgaruvchi nomini barcha bosh 
# harflar bilan yozing.

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

# comentariya yozish bu biz uchun juda muhim o'tgan darsda 
# aytaman deb aytrish yodimdan kotarilib qolibdi 
# lekin hali hech narsa uchun kechmas (o'zbek halq maqoli:)

# dars boshidan beri so'zlarim komentariya 
# turibdi bunga ahamyat bergandirsiz

# komentariya qushtirnoq orqali ochiladi
# va ichiga yozilgan har qanday narsa kodimizga halaqit berolmaydi
# <--- comentariya

# Qanday izohlarni yozish kerak?
# Sharh yozishning asosiy sababi - kodingiz nima qilishi kerakligini va uni qanday 
# ishlashini tushuntirishdir. Loyiha ustida ishlashning o'rtasida bo'lganingizda, barcha 
# qismlar bir-biriga qanday mos kelishini tushunasiz. Ammo bir muncha vaqt o'tgach, 
# loyihaga qaytganingizda, siz unutgan bo'lishingiz mumkin
# ba'zi tafsilotlar. Siz har doim kodingizni bir muncha vaqt o'rganishingiz va 
# segmentlar qanday ishlashi kerakligini aniqlashingiz mumkin, ammo yaxshi sharhlar 
# yozish sizning umumiy yondashuvingizni aniq ingliz tilida umumlashtirib, vaqtingizni
# tejash imkonini beradi.
# Agar siz professional dasturchi bo'lishni yoki boshqa dasturchilar bilan hamkorlik 
# qilishni istasangiz, mazmunli sharhlar yozishingiz kerak. Bugungi kunda dasturiy 
# ta'minotning ko'pchiligi bitta kompaniyaning bir guruhi xodimlari yoki ochiq kodli 
# loyihada birgalikda ishlaydigan bir guruh odamlar tomonidan hamkorlikda yoziladi. 
# Malakali dasturchilar sharhlarni kodda ko'rishni kutishadi, shuning uchun dasturlaringizga 
# tavsiflovchi sharhlarni hozirdan qo'shishni boshlash yaxshidir. 
# Kodingizda aniq, qisqacha sharhlar yozish yangi dasturchi sifatida 
# shakllantirishingiz mumkin bo'lgan eng foydali odatlardan biridir.
# Izoh yozish yoki yozishga qaror qilganingizda, o'zingizdan so'rang, 
# biror narsani amalga oshirishning oqilona usulini o'ylab topishdan oldin 
# bir nechta yondashuvlarni ko'rib chiqishingiz kerak edi; agar shunday bo'lsa, 
# o'z yechimingiz haqida sharh yozing. Orqaga qaytib, kam sharhlangan dastur uchun 
# sharh yozishdan ko'ra, keyinroq qo'shimcha sharhlarni o'chirish ancha oson. Bundan 
# buyon men ushbu kitobdagi misollardagi sharhlardan kod bo'limlarini tushuntirishga 
# yordam berish uchun foydalanaman.




