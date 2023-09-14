
sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктывкар', 'Статус': 'дядя'}, 
      'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктывкар', 'Статус': 'тетя'}}

print('Добро пожаловать в телефонный справочник. \n Доступные команды:\n /all - показать список контактов, \n /add.contact - добавить контакт, \n /add.number - добавить номер к существующему контакту, \n /delete.contact - удалить контакт')

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров') 
        for k, v in sp.items():
            print(k, v)

    elif command == '/add.contact':
        name = input('Введите имя нового контакта: ')
        if name in sp:
            print('Контакт существует!')
        else:
            coll = int(input('Сколько номеров вы хотите ввести: '))
            numbers = []
            for i in range(coll):
                number = input(f'Введите {i + 1} номер: ')
                numbers.append(number)
            city = input('Введите название города: ')
            status = input('Введите статус: ')
            sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}

    if command == '/add.number':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакт не существует!!!')
        else :
            phone = input('Введите номер: ')
            if phone in sp [name]['номер телефона']:
                print('Номер существует')
            else:
                sp [name]['номер телефона'].append(phone)

    if command == '/delete.contact':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакт не существует!!!')
        else:
            del sp[name]

    # if command == '/delete.number':
    #     name = input('Введите имя контакта для изменения номера: ')
    #     if name not in sp:
    #         print('Такой записи в справочнике нет!!!')
    #     else :
    #         phone = input('Введите номер: ')
    #         if phone in sp [phone]['номер телефона']:
    #             print('Номер существует')
    #         else:
    #             sp [phone]['номер телефона'].pop(phone)
    
    if command == '/modify.contact':
        name = input('Введите имя контакта для внесения изменений: ')
        # if name not in sp:
        #     print('Контакт не существует!!!')
        new_number = input('Введите новый номер: ')
        new_city = input('Введите новый город: ')
        new_status = input('Введите новый статус: ')
        sp[name] = {'номер телефона': new_number, 'город': new_city, 'Статус': new_status}
        


       




    # elif command == '/help':
    #     print('Здесь какойто мануал')











# phonebook = {"Дядя Ваня": {"phones": ["+78002553535", "+79772562534"], "BD": "12.11.1973", 'eMail': "qwerty@yandex.ru"}}
# print(phonebook['Дядя Ваня']['phones'])
# def  Search():
#     pass

# def Add():
#     pass

# phonebook_txt = open("pjone.txt", "a", encoding='utf-8')
# phonebook_txt.close()


# while True:
#     print("Enter choice: ")
#     print("1. Add names")
#     print("2. Add number")
#     print("3. Search number")
