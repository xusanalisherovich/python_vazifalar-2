# classes 

"""
Python - bu ob'ektga yo'naltirilgan dasturlash tili

Ob'ektga yo'naltirilgan dasturlash dasturiy ta'minotni yozishning eng samarali usullaridan biridir. 
Ob'ektga yo'naltirilgan dasturlashda siz haqiqiy narsalarni ifodalovchi sinflarni yozasiz
va vaziyatlar, va siz shular asosida ob'ektlar yaratasiz
sinflar. Sinf yozganingizda, siz umumiyni aniqlaysiz
ob'ektlarning butun toifasi ega bo'lishi mumkin bo'lgan xatti-harakatlar.


Sinfdan ob'ekt yaratish instantsiya deb ataladi va siz sinf misollari bilan ishlaysiz. 
Ushbu bobda siz sinflarni yozasiz va bu sinflarning namunalarini yaratasiz. Siz misollarda 
saqlanishi mumkin bo'lgan ma'lumotlar turini belgilaysiz va bu misollar 
bilan bajarilishi mumkin bo'lgan harakatlarni belgilaysiz. 
Shuningdek, siz mavjud sinflarning funksiyalarini kengaytiradigan sinflarni yozasiz, shuning uchun

shunga o'xshash sinflar kodni samarali almashishi mumkin. 
Siz o'z sinflaringizni modullarda saqlaysiz va boshqa dasturchilar tomonidan 
yozilgan sinflarni o'zingizning dastur fayllaringizga import qilasiz.

"""

"""
Ob'ektga yo'naltirilgan dasturlashni tushunish sizga dasturchi kabi dunyoni ko'rishga yordam beradi. 
Bu sizning kodingizni bilishingizga yordam beradi, balki
faqat satr satr nima bo'layotganini, balki uning ortidagi kattaroq tushunchalarni ham. 
Darslar ortidagi mantiqni bilish sizni mantiqiy fikrlashga o'rgatadi, shuning uchun 
siz duch keladigan deyarli har qanday muammoni samarali hal qiladigan dasturlarni yozishingiz mumkin.
Sinflar, shuningdek, siz va siz bilan birga ishlaydigan boshqa dasturchilar uchun 
hayotni osonlashtiradi, chunki siz borgan sari murakkab vazifalarni hal qilasiz. Siz va boshqa dasturchilar bir xil mantiqqa asoslangan kod yozsangiz, bir-biringizning ishini tushunishingiz mumkin bo'ladi. Sizning dasturlaringiz ko'plab hamkorlar uchun mantiqiy bo'lib, hammaga ko'proq narsani bajarishga imkon beradi.

"""
# class My_one_class:
#     x = 5


# p1 = My_one_class()
# print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# class nomi katta harf bilan boshlanadi class profisianal tarzda organish kerak 
# class malum bir toliq vazifani bajarish uchun ishlatiladi katta proectlarda asosan class islatiladi
# dog klasini yaratib koramiz

class Dog:
    """ it ni modellashtirishga oddiy urinish """

    def __init__(self, name, age):
        """intalizatsiya qilamiz name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """ buyruq bulishi bilan otirsin"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """ buyruqga binoan agdarilish """
        print(f"{self.name} rolled over!")

dog = Dog('alisa',5)
print(dog.sit())

"""
__init__() usuli
Sinfning bir qismi bo'lgan funksiya - bu usul. 
Funktsiyalar haqida o'rgangan hamma narsa usullarga ham tegishli; 
Hozircha yagona amaliy farq - bu usullarni chaqirish usuli. 
__init__() usuli - bu maxsus usul bo'lib, Python har doim yangi misol asosida yaratilganda 
avtomatik ravishda ishlaydi.
Itlar sinfida. Ushbu usulda ikkita asosiy pastki chiziq va ikkita pastki 
chiziq mavjud bo'lib, bu Pythonning standart usul nomlari sizning usul 
nomlaringiz bilan zid kelishini oldini olishga yordam beradi. __init__() ning 
har ikki tomonida ikkita pastki chiziqdan foydalanganingizga ishonch hosil qiling. 
Agar siz har tomondan bittadan foydalansangiz, sinfingizdan foydalanganda usul 
avtomatik ravishda chaqirilmaydi, bu esa aniqlash qiyin bo'lgan xatolarga olib kelishi mumkin.

Biz __init__() usulini uchta parametrga ega bo'lish uchun aniqlaymiz: o'z, ism va yosh. 
Usul ta'rifida self parametri talab qilinadi va u boshqa parametrlardan 
oldin birinchi o'rinda turishi kerak. Bu ta'rifga kiritilishi kerak, 
chunki Python bu usulni keyinroq chaqirganda (Dog misolini yaratish uchun), 
usul chaqiruvi avtomatik argumentni avtomatik ravishda uzatadi. Misol bilan 
bog'langan har bir usul chaqiruvi avtomatik ravishda o'z-o'zidan o'tadi, 
bu misolning o'ziga havoladir; u individual misolga sinfdagi atributlar va 
usullarga kirish imkonini beradi. Biz Dog misolini yaratganimizda, 
Python Dog sinfidan __init__() usulini chaqiradi. Biz itdan o'tamiz()
dalil sifatida ism va yosh; self avtomatik ravishda uzatiladi, shuning 
uchun biz uni topshirishimiz shart emas. Qachonki biz Dog sinfidan namuna 
yaratmoqchi bo'lsak, biz faqat oxirgi ikkita parametr, ism va yosh uchun qiymatlarni beramiz.

qisqacha

__init__() funktsiyasi

Yuqoridagi misollar eng oddiy shakldagi sinflar va ob'ektlar bo'lib, ular haqiqiy hayotda qo'llanilmaydi.

Sinflarning ma'nosini tushunish uchun biz o'rnatilgan __init__() funktsiyasini tushunishimiz kerak.

Barcha sinflarda __init__() funksiyasi mavjud bo'lib, u har doim sinf ishga tushirilganda bajariladi.

Ob'ekt xususiyatlariga qiymatlarni belgilash yoki ob'ekt yaratilayotganda bajarilishi kerak bo'lgan 
boshqa operatsiyalar uchun __init__() funksiyasidan foydalaning:


"""


# endi tepadagi dog fayilini choqirib ishlatib koramiz

my_dog = Dog("wiliam",'6')

# # endi my_dog o'zgaruvchisida dogni hamma malumotlari bor undan olib ishlataversak boladi
print(f'mening itimning ismi {my_dog.name}')
print(f"mening itimning yoshi {my_dog.age}")

"""
Keling, mashinani ifodalovchi yangi sinf yozaylik. 
Bizning sinfimiz biz ishlayotgan mashina haqida ma'lumotni saqlaydi 
va bu ma'lumotni umumlashtiradigan usulga ega bo'ladi:

"""

class Car: 
    """A simple attempt to represent a car.""" 
    def __init__(self, make, model, year, engine): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name.""" 
        long_name = f"{self.year} {self.make} {self.model}"  
        return long_name.title()
    def ignition(self):
        igniti = f"ignition {self.engine}"
        return igniti
my_new_car = Car('audi', 'a4', 2019, 'v12 biturbo') 
print(my_new_car.ignition())


"""
Car sinfida biz __init__() usulini avval o'z-o'zidan parametr bilan aniqlaymiz, 
xuddi it sinfida bo'lgani kabi. Biz ham beramiz
yana uchta parametr: ishlab chiqarish, model va yil. __init__() 
usuli ushbu parametrlarni oladi va ularni ushbu sinfdan yaratilgan 
misollar bilan bog'langan atributlarga tayinlaydi. Yangi avtomobil 
namunasini yaratganimizda, namunamiz uchun marka, model va yilni 
ko'rsatishimiz kerak bo'ladi.
Atvwe get_descriptive_name() deb nomlangan usulni belgilaydi, u 
mashinaning yilini, ishlab chiqarishini va modelini mashinani aniq 
tasvirlaydigan bitta qatorga joylashtiradi. Bu bizni har bir atribut 
qiymatini alohida chop etishimizdan xalos qiladi. Ushbu usulda atribut 
qiymatlari bilan ishlash uchun biz self.make, self.model va self.year dan 
foydalanamiz. Atwwe Car sinfidan misol yaratamiz va uni my_new_car 
o'zgaruvchisiga tayinlaymiz. Keyin qanday mashinani ko'rsatish uchun 
get_descriptive_name() ni chaqiramiz
bizda ... bor:

yana biz qushimchasiga ingition tugmasini qushdik moshinani yoqish uchun 

"""

# default qiymat yaratish

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()


    def read_odometer(self):
        print(f'bu mashina {self.odometer_reading} miles')

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# default qiymatni ozgartirsak ham boladi

# my_new_car.odemeter_reading = 23 
# my_new_car.read_odometer()


"""
Usul orqali atribut qiymatini o'zgartirish
Siz uchun ma'lum atributlarni yangilaydigan usullarga ega bo'lish foydali bo'lishi mumkin. 
Atributga to'g'ridan-to'g'ri kirish o'rniga, siz yangi qiymatni ichki 
yangilashni boshqaradigan usulga o'tkazasiz.
Mana update_odometer() deb nomlangan usulni ko'rsatadigan misol:
"""


class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()

    def read_odometer(self):
        print(f'bu mashina {self.odometer_reading} miles')

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.""" 
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.update_odometer(23) 
my_new_car.read_odometer()



"""
Usul orqali atribut qiymatini oshirish
Ba'zan siz butunlay yangi qiymat o'rnatish o'rniga, 
atributning qiymatini ma'lum miqdorga oshirishni xohlaysiz. 
Aytaylik, biz eski mashina sotib olamiz va uni sotib olganimizdan uni 
ro'yxatdan o'tkazganimizgacha 100 milya yo'l bosib o'tamiz. 
Mana, bu qo'shimcha miqdorni o'tkazish va bu qiymatni odometr 
ko'rsatkichiga qo'shish imkonini beradigan usul:
"""

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()

    def read_odometer(self):
        print(f'bu mashina {self.odometer_reading} miles')

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.""" 
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100) 
my_used_car.read_odometer()

# intalizatsiyani tushundik ya'ni intalizatsiya usha class uchun qilinadiga variablar (o'zgaruvchilar) ekan
# endi intalizatsiyaga uxshagan class ga yordamlashadigan funksiyalar bor ular zarur emas lekin bilib 
# quyish zarar qimaydi

# __str__
"""
str funksiyasi class da ishlaganda classni nomi bilan choqirganda 
<__main__.Student object at 0x7f9c8c8c8970> shunaqa ko'rinishda ma'lumot chiqadi buni 
to'girlash uchun __str__ ishlatiladi desak ham buladi

"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def my_str(self):
    return self.name

p1 = Person("John", 36)

print(p1)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}"

student = Student("Ali", 20)

# __str__ chaqiriladi
print(student) 

# del
# del funksiya yordamida classni butunlay uchirib tashlasak boladi


class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage.""" 
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
           Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100) 
my_used_car.read_odometer()

"""
Bolalar sinfi uchun __init__() usuli
Mavjud sinfga asoslangan yangi sinf yozayotganda, siz ko'pincha ota-sinfdan __init__() 
usulini chaqirishni xohlaysiz. Bu ota-ona __init__() usulida belgilangan har qanday atributlarni 
ishga tushiradi va ularni bolalar sinfida mavjud qiladi.
Misol tariqasida, keling, elektromobilni modellashtiraylik. 
Elektr avtomobil - bu faqat o'ziga xos avtomobil turi, shuning uchun biz yangi 
ElectricCar sinfimizni avval yozgan Avtomobil sinfiga asoslashimiz mumkin.
Keyin biz faqat elektromobillarga xos xususiyatlar va xatti-harakatlar uchun kod yozishimiz kerak bo'ladi.
"""


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# super class da eng kerakli ishlardan birini meros op qolishni bajaradi biz class nomini yozib ham 
# choqirishim mumkin lekin bu maslahat berilmaydi


# kelik elektirimizga narsalar qushamiz

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) 
        self.battery_size = 75
    
    def describe_battery(self):
        """Print a statement describing the battery size.""" 
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()


# keling endi intensive atribute yaratib kuramiz

class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def __init__(self, make, model, year): 
        """Initialize attributes to describe a car.""" 
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}" 
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage.""" 
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
           Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading.""" 
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015) 
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500) 
my_used_car.read_odometer()

my_used_car.increment_odometer(100) 
my_used_car.read_odometer()

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75): 
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size.""" 
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) 
        self.battery = Battery()
    
    def describe_battery(self):
        """Print a statement describing the battery size.""" 
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()

# endi bu yerda bitta class ichidagi funksiyadan boshqa class ichidagi 
# funksiyaning malumotiga murojat qilyapmiz

# from va import qilib class choqirishni o'rganamiz