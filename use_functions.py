money = 0.0
history = []
while True:
    print("\n" * 2)
    print(f'на счету {money} руб')
    print('===================')
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')


    choice = input('Выберите пункт меню\n')
    if choice == '1':
        money += float(input('Выберите сумму:\n'))
        pass
    elif choice == '2':
        price = float(input('Выберите цену:\n'))
        if price>money:
            print('Денег не хватает.\n')
        else:
            money -= price
            history.append((input('Название покупки.\n'), price))
    elif choice == '3':
        for name, money in history:
            print(f"{name} => {money}")
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')