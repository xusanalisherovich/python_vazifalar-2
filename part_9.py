# Funksiya

# Ushbu bobda siz kod bloklari deb ataladigan funktsiyalarni yozishni o'rganasiz
# ma'lum bir ishni bajarish uchun mo'ljallangan. Muayyan vazifani bajarmoqchi bo'lganingizda
# Agar siz funktsiyada aniqlagan bo'lsangiz, unga javob beradigan funktsiyani chaqirasiz. 
# Agar siz ushbu vazifani bajarishingiz kerak bo'lsa
# dastur davomida bir necha marta bir xil vazifa uchun barcha kodlarni qayta-qayta kiritishingiz 
# shart emas; siz shunchaki ushbu vazifani bajarishga bag'ishlangan funktsiyani chaqirasiz 
# va qo'ng'iroq Python-ga funksiya ichidagi kodni ishga tushirishni aytadi. Funktsiyalardan 
# foydalanish dasturlaringizni yozish, o'qish, sinab ko'rish va tuzatishni osonlashtirishini bilib olasiz.

# funksiyani def kalir so'zi bilan chaqiramiz va ichiga hohlagancha kod yozib qandaydir vazfa yuklaymiz
# dunksiyadan keyin uni nomini yozamiz odatda nomi kichkina harf bilan boshlanadi chunki katta harf 
# bilan yozsak classga uxshab qoladi class deb tushuniladi

# funksiya nomlari act()✅ 12_alish()❌ Azamat_codecode() ❌ add_plus()✅ 

def greet_user():
    # funksiyadan keyin 3lik qushtirnoqda narsa yozilganini kursanggiz demak bu funksiyani vazifasi boladi
    """Display a simple greeting."""
    print("Hello!") 

greet_user()

# Funktsiyaga ma'lumot uzatish
# Bir oz o'zgartirilgan greet_user() funksiyasi nafaqat foydalanuvchiga Salom! 
# balki ularni nomi bilan ham salomlashing. Funktsiya buni amalga oshirishi uchun 
# def greet_user() da funksiya taʼrifining qavslar ichiga foydalanuvchi nomini kiriting. 
# Bu yerga foydalanuvchi nomini qo'shish orqali siz funksiyaga siz ko'rsatgan foydalanuvchi 
# nomining istalgan qiymatini qabul qilishiga ruxsat berasiz.
# Funktsiya endi sizdan har safar chaqirganinggiza
#  qilganingizda foydalanuvchi nomi uchun qiymat berishingizni kutadi. 
# greet_user() ga qo'ng'iroq qilganingizda, unga qavslar ichida "jesse" kabi nom berishingiz mumkin:

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')


def describe_pet(animal_type, pet_name): 
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# google kodlaridan misollar tushuntiray

# uni tushuntirishdan avval funksiya deyapmiz va funksiya bizaga natija 
# qaytarsa uni yani usha kodlarimizni qayta yozmasdan ishlatsak buladi deyapmiz lekin tepadagi 
# kodlarimziga print ishlatdik bu degani bu kodlar bizga qaytmaydi togri terminalga chiqadi
# kodlar bizga qaytishi uchun def ni uzini funksiyaasi bor bu return return bizda natijani qaytaradi
# agar natijani print qilsak keyin terminalga chiqadi asil holida shunchaki qaytadi bu botlar 
# saytlar umuman hamma joyda ishlatidi

# oodiy misol

def add(son,son2):
    return son + son2

print(add(10,15))
def filter_even_numbers(numbers):
    """Listdagi faqat juft sonlarni qaytaradi."""
    return [num for num in numbers if num % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(numbers))  # [2, 4, 6]

import pandas as pd

def create_dataframe(data):
    """Dictionary ma'lumotlardan DataFrame yaratadi."""
    return pd.DataFrame(data)

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = create_dataframe(data)
print(df)

# learn

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')


def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
xmusician = get_formatted_name('john', 'hooker', 'lee') 
print(musician)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def print_models(unprinted_designs, completed_models): 
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed.""" 
    print("\nThe following models have been printed:") 
    for completed_model in completed_models:
           print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

def maumot_bazasi(malumot):
    while True:
        malumot_qoshish = input('maluumotni yozing: ')
        if malumot_qoshish == 'q':
            break
        elif malumot_qoshish == 'o':
            malumot_opchirish = input('malumotni ochirish')
            malumot.remove(malumot_opchirish)
            print(malumot)
        else:
            malumot.append(malumot_qoshish)
            print(malumot)

    return malumot
print(maumot_bazasi(['olma','nok','banana']))

# Ba'zan siz funktsiya qancha argumentlarni qabul qilishi kerakligini oldindan bilmay qolasiz. 
# Yaxshiyamki, Python funksiyaga chaqiruv bayonotidan ixtiyoriy sonli 
# argumentlarni to'plash imkonini beradi.
# Misol uchun, pitsa yasaydigan funksiyani ko'rib chiqing. 
# U bir qator qo'shimchalarni qabul qilishi kerak, lekin odam qancha 
# to'ldirishni xohlashini oldindan bilib bo'lmaydi. Quyidagi misoldagi 
# funksiya bitta parametrga ega, *toppings, lekin bu parametr chaqiruv 
# liniyasi taqdim etganicha ko‘p argumentlarni to‘playdi:❗️❗️❗️❗️
import pandas
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Parametr nomidagi yulduzcha *toppings Python-ga toppings deb ataladigan bo'sh kortej 
# yaratishni va u olgan qiymatlarni ushbu kortejga to'plashni aytadi. 
# Funktsiya tanasidagi print() chaqiruvi Python funksiya chaqiruvini bitta 
# qiymatli va uchta qiymatli qo'ng'iroqni boshqarishi mumkinligini ko'rsatadigan 
# natijani ishlab chiqaradi. U turli xil qo'ng'iroqlarni xuddi shunday ko'rib chiqadi. 
# E'tibor bering, Python argumentlarni kortejga to'playdi, hatto funktsiya faqat bitta qiymat olsa ham:

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# O'zboshimchalik bilan kalit so'z argumentlaridan foydalanish
# Ba'zan siz ixtiyoriy sonli argumentlarni qabul qilishni xohlaysiz, 
# lekin funktsiyaga qanday ma'lumotlar uzatilishini oldindan bilmaysiz. 
# Bunday holda siz chaqiruv bayonotida qancha kalit-qiymat 
# juftligini qabul qiladigan funksiyalarni yozishingiz mumkin. 
# Bir misol, foydalanuvchi profillarini yaratishni o'z ichiga oladi: 
# siz foydalanuvchi haqida ma'lumot olishingizni bilasiz, lekin qanday 
# ma'lumot olishingizga ishonchingiz komil emas. ichida build_profile() funktsiyasi
# Quyidagi misol har doim ism va familiyani oladi, lekin u ixtiyoriy sonli kalit 
# so'z argumentlarini ham qabul qiladi:
# qisqa mazmuni argument yani ozgaruvchilarni hohlagancha keyinchalik qaytayotgan qiymatga qushsak buladi

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

# yangi pizza.py nomli fayl yarating

# def make_pizza(size, *toppings):
#        """Summarize the pizza we are about to make."""
#        print(f"\nMaking a {size}-inch pizza with the following toppings:")
#        for topping in toppings:
#            print(f"- {topping}")



# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

