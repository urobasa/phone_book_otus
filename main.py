import json
import functions
oper = functions
loaded_contacts = []
menu = ('''
--------------Телефонный справочник-------------
1) Открыть файл
2) Cохранить файл
3) Показать все контакты
4) Создать контакт
5) Найти контакт
6) Изменить контакт
7) Удалить контакт
8) Выход
''')

while True:
    print(menu)
    selected_menu = input('Введите номер пункта меню: ')
    match selected_menu:
        case '1':
            while True:
                print('Открыть файл')
                get_fil_nam = input('Введите имя файла или нажмите enter для для открытия файла phonebook.json: ')
                get_fil_nam = get_fil_nam if get_fil_nam != "" else 'phonebook.json'
                loaded_contacts = oper.open_file(get_fil_nam)
                if loaded_contacts is not None:
                    break
        case '2':
            try:
                with open(get_fil_nam, 'w', encoding='utf-8') as file_cre:
                    json.dump(loaded_contacts, file_cre, ensure_ascii=False, indent=4)
                    print(f'Сохранен файл справочника {get_fil_nam}')
                    input("Нажмите Enter для продолжения...")
            except NameError:
                print('Не открыт файл телефонной книги')
                get_fil_nam = oper.save_new(loaded_contacts)
        case '3':
            print('показ все')
            if len(loaded_contacts) > 0:
                oper.print_contacts(loaded_contacts)
            else:
                print('Ни одного контакта в списке контактов нет')
                input("Нажмите Enter для продолжения...")

        case '4':
            print('создать конт')
            new_cont = oper.create_contact()
            max_id = None
            if loaded_contacts:
                for cont_get in loaded_contacts:
                    if max_id is None or cont_get['id'] > max_id:
                        max_id = cont_get['id']
            if max_id is None:
                max_id = 1
                new_cont['id'] = max_id
            else:
                new_cont['id'] = max_id + 1
            loaded_contacts.append(new_cont)
            print(f"Контакт добавлен ID:{new_cont['id']}")
            input("Нажмите Enter для продолжения...")
        case '5':
            print('найти конт')
            if len(loaded_contacts) > 0:
                querys = input('Введите текст для поиска: ')
                if len(querys) > 0:
                    oper.search_contacts(loaded_contacts, querys)
                else:
                    print('Введен пустой поисковый запрос')
                    input("Нажмите Enter для продолжения...")
            else:
                print('Список контактов пуст, поиск невозможен')
                input("Нажмите Enter для продолжения...")
        case '6':
            print('изменить конт')
            if len(loaded_contacts) > 0:
                oper.edit_contact(loaded_contacts)

        case '7':
            print('удалить конт')
            if len(loaded_contacts) > 0:
                loaded_contacts = oper.delete_contact(loaded_contacts)
            else:
                print('Список контактов пуст')
        case '8':
            try:
                oper.exit_save_quest(get_fil_nam, loaded_contacts)
            except NameError:
                print('Найдены изменения не сохраненные в файл')
                print('Не открыт файл телефонной книги')
                oper.save_new(loaded_contacts)
            break
        case "":
            print('Выберите один из пунктов меню и введите цифру')
            input("Нажмите Enter для продолжения...")
        case _:
            print('Выберите один из пунктов меню и введите цифру')
            input("Нажмите Enter для продолжения...")
    print(' ')