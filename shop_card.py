shopping_cart = []

while True:
    print("\nSavatcha:")
    print(shopping_cart)
    print("\nAmallar:")
    print("1. Mahsulot qo'shish")
    print("2. Mahsulot o'chirish")
    print("3. Savatchani ko'rish")
    print("4. Chiqish")

    tanlov = input("Tanlovingizni kiriting: ")

    if tanlov == '1':
        mahsulot = input("Mahsulot nomini kiriting: ")
        shopping_cart.append(mahsulot)
    elif tanlov == '2':
        mahsulot = input("O'chiriladigan mahsulot nomini kiriting: ")
        if mahsulot in shopping_cart:
            shopping_cart.remove(mahsulot)
        else:
            print(f"{mahsulot} savatchada mavjud emas.")
    elif tanlov == '3':
        print("Savatchadagi mahsulotlar: ", shopping_cart)
    elif tanlov == '4':
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring!")
