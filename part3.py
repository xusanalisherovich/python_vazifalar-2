# list nima?

# Ro'yxat - ma'lum bir tartibda bo'lgan narsalar to'plami. 
# Siz alifbo harflarini, 0 dan 9 gacha bo'lgan raqamlarni yoki 
# oilangizdagi barcha odamlarning ismlarini o'z ichiga olgan ro'yxatni tuzishingiz mumkin. 
# Siz ro'yxatga xohlagan narsani qo'yishingiz mumkin, va
# ro'yxatingizdagi narsalar biron bir tarzda bog'liq bo'lishi shart emas. 
# Ro'yxat odatda bir nechta elementlarni o'z ichiga olganligi sababli, ro'yxat nomini 
# harflar, raqamlar yoki nomlar kabi ko'plik qilish yaxshidir.
# Pythonda kvadrat qavslar ([]) ro'yxatni bildiradi va ro'yxatdagi alohida elementlar 
# vergul bilan ajratiladi. Bir necha turdagi velosipedlarni o'z ichiga olgan ro'yxatning 
# oddiy misoli

# asarlar = ['badiiy','dramatik','romantik','biznes', 'roman']
# print(asarlar)

# # pythondagi typelarni type() funksiyasi yordamida kurishingiz mumkin 
# print(type(asarlar))
# print(type(213123))

# Ro'yxatdagi elementlarga kirish
# Ro'yxatlar tartiblangan to'plamlardir, shuning uchun siz Python-ga kerakli elementning o'rnini yoki indeksini aytib, ro'yxatdagi istalgan elementga kirishingiz mumkin. Roʻyxatdagi elementga kirish uchun roʻyxat nomini, keyin esa kvadrat qavs ichiga olingan element indeksini yozing.
# Masalan, velosipedlar ro'yxatidagi birinchi velosipedni chiqaramiz:

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])

# hop list umuman olganda dasturlashda 0 dan boshlab sanaladi
# tepada aytgandim har bir narsani uzini joylashuvi buladi deb shu 
# joylashuv bizda index deb ataladi
# indexlar 0dan boshlanib cheksizgacha ketadi

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[0])

# savol print ichidagi narsani type qanaqa
# togri topolmadiz bu list emas bu string
# negaki biz list ichidagi string elementiga murojat qilyapmiz 

# print(type(bicycles[0]))

# list ni str bilan individual ishlatsak ham buladi

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# message = f"my list {bicycles[0].title()}"
# print(bicycles[0])

# avto = ['honda', 'yamaha', 'suzuki']

# suziki = avto[2]
# print(avto)
# print(suziki)

# listda ham strga uxshab bizga yordam beradigan methodlari bor
# .append('str') = bu qaysidir listga element qushadi(str,int,float kabilar)

# avto = ['honda', 'yamaha', 'suzuki']

# avto.append('mers')
# avto.append('bmw')

# print(avto)

# raqamlar = [1,2,3,4,5,6]

# raqamlar.append(10)
# raqamlar.append(11)
# raqamlar.append(12)
# raqamlar.append(13)

# print(raqamlar)

# append funksiyasi faqat oxiridan qushadi !!!
# .insert(index, 'str') = insert index buyicha malumotni hohlagan joyimizga qushsak buladi

# avto = ['honda', 'yamaha', 'suzuki']

# avto.insert(0,'mers')
# avto.insert(2,'bmw')

# print(avto)

# siz kop kod yozdiz va qaysidir listni ochirish kerak bulsa siz uni qidirib utirmay 
# del funksiyasi yordamida ochirib tashlashingiz mumkin


# avto = ['honda', 'yamaha', 'suzuki']

# avto.insert(0,'mers')
# avto.insert(2,'bmw')

# del avto

# print(avto)

# hohlasak index orqali faqat bitta elementni ochirishimiz mumkin
# avto = ['honda', 'yamaha', 'suzuki']

# avto.insert(0,'mers')
# avto.insert(2,'bmw')

# del avto[2]

# print(avto)

# keyingi organadiga methodimiz bu .pop()
# .pop() = oxiridagi elementni ozida olib qoladi

# names = ['gucci', 'pepsi', 'water', 'bonaqua']

# names.pop() # shu xolatda oxiridagi elementni kesib ozida olib qoldi
# print(names)

# names = ['gucci', 'pepsi', 'water', 'bonaqua']

# last_name_of_brands = names.pop() # agar buni ozgaruvchiga olsak
# print(names)
# print(last_name_of_brands.title())

# pop dan yana index orqali ham foydalansak buladi bunda qavs ichiga 
# kesib olmoqchi bulgan elementimizni indexnini yozamiz

# avto = ['honda', 'yamaha', 'suzuki']

# first_avto = avto.pop(0)
# print(avto)
# print(first_avto)

# .remove('value')
# .remove() = bizda qiymat buyicha ochiradi

# avto = ['honda', 'yamaha', 'suzuki']

# avto.remove('honda')
# # honda_remove = avto.remove('honda')
# print(avto)
# hondani olib tashladik olib tashlagan elementimizni kormoqchi 
# bulsak ozgaruvchi orqali korishimiz mumkin emas (bu elementni butunlay uchiradi)

#  man ozim kop ishlatadigan funksiyaladan biri bu sort
# .sort() bizda nomi bl malum elementlarni sortlab beradi

# cars = ['mers','bmw','toyoto','subaru','audi']

# cars.sort()
# print(cars)

# endi biz tezkari sortlamochi bulsak sort ichiga 
# reverse=True funksiyasini bajarsak buldi

# cars = ['mers','bmw','toyoto','subaru','audi']

# cars.sort(reverse=True)
# print(cars)

# .reverse() = buni uzi hech qanday qiymat qaytarmaydi
# vazifasi berilgan listni joyini almashtirish yoki uzgartirmaslik

# cars = ['mers','bmw','toyoto','subaru','audi']

# cars.reverse()
# print(cars)

# biz list str int royhatlarni sanaydigan python funksiyasi bor
# len() = ichida nechta element borligini sanaydi

# cars = ['mers','bmw','toyoto','subaru','audi']

# cars.sort()
# print(len(cars))

# [-1] -1 bu eng oxiridagi elementni oladi


# cars = ['mers','bmw','toyoto','subaru','audi']
# top = [1,2,3,4,5]

# print(cars[-1])
# print(top[2:-1])# bunda nega 5chiqmadi boshida bir aytgandim torburchak ichidagi bulinishda oxirgi elementni olmaydi deb
