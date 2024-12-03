shot = 0
history = []
while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')
    choice = input('Выберите пункт меню: - ')
    if choice == '1':
      money = float(input('Введите сумму: - '))
      shot += money
    elif choice == '2':
        pok = float(input('Введите сумму покупок: - '))
        if pok > money:
            print('Недостаточно средств. Пополните пожалуйста счёт.')
            money_balance = float(input('Пополнить баланс: - '))
            shot += money_balance
        else:
            product_name = input('Ввести название покупки: - ')
            shot -= pok
            history.append((product_name, pok))
    elif choice == '3':
      if history:
        print("\nИстория покупок:")
        for name, pok in history:
          print(f"{name}: {pok}")
    elif choice == '4':
      print(shot)
      print('PROGRAM EXIT.')
      break
    else:
        print('Неверный пункт меню')