# elif choice == "Загрузить БД": # если выбрали этот пункт
#             # загрузить из json
#             fname=fileopenbox('Выберите файл формата JSON') # открываем файл
#             with open(fname, 'r', encoding='utf-8') as fh: # открываем файл а чтение
#                 BD = json.load(fh) # загружаем из файла данные в словарь data
#             print ('БД успешно загружена')
#             loaded = True # меняем флаг загрузки БД
#         elif choice == 'Сохранить БД':# если выбрали этот пункт
#             # сохранить в json
#             with open ('BD.json', 'w', encoding='utf-8') as fh: # открываем файл на запись
#                 fh.write(json.dumps(BD, ensure_ascii = False)) # преобразовываем словарь data в unicode - строку и записываем в файл
#                 print('БД успешно сохранена')

sp = {'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктывкар', 'Статус': 'дядя'}, 
      'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}

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
        name = input('Введите имя нового контакта: ')
        if name not in sp:
            print('Контакта не существует!!!')
        else :
            phone = input('Введите номер: ')
            if phone in sp [name]['номер телефона']:
                print('Номер существует')
            else:
                sp [name]['номер телефона'].append(phone)

       
       
       
    #     sp.append(f)
    #     print('Контакт добавлен!')
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
