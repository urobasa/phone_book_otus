import json, os
def open_file(filename):
    contacts = []
    if os.path.exists(filename):
        if os.path.getsize(filename) > 0:
            with open(filename, 'r', encoding='utf-8') as read_fil:
               contacts = json.load(read_fil)
               if len(contacts) > 0:
                   print(f'Контакты загружены из файла {filename}')
                   input("Нажмите Enter для продолжения...")
               else:
                   print(f'Открыт файл {filename} не содержащий ни одного контакта')
                   input("Нажмите Enter для продолжения...")
        else:
            print(f'Открыт пустой файл {filename}')
            input("Нажмите Enter для продолжения...")
    else:
        while True:
            crea_fil = input('Файл не найден, создать новый файл? y/n ').lower().strip()
            if crea_fil == 'y':
                with open(filename, 'w', encoding='utf-8') as file_cre:
                    json.dump(contacts, file_cre, ensure_ascii=False, indent=4)
                print(f'Открыт новый файл справочника {filename}')
                input("Нажмите Enter для продолжения...")
                break
            elif crea_fil == 'n':
                return None
            else:
                print('Введите y/n')
    return contacts

def save_new(contacts):
    while True:
        save_new = input('Сохранить в новый файл телефонной книги? y/n ').strip().lower()
        if save_new == 'y':
                new_file = input('Введите имя файла: ')
                with open(new_file, 'w', encoding='utf-8') as file_cre:
                    json.dump(contacts, file_cre, ensure_ascii=False, indent=4)
                    print(f'Сохранен новый файл справочника {new_file}')
                    input("Нажмите Enter для продолжения...")
                    return new_file
        elif save_new == 'n':
            break
        else:
            print('Введите y/n')
    return

def print_contacts(contacts_list):
        print('\nКонтакты: ')
        print('-------------------------')
        for cont in contacts_list:
            print("ID:", cont['id'])
            print("Имя:", cont['name'])
            print("Тел:", cont['phone'])
            print("Коммент:", cont['comment'],'\n')
        print('-------------------------')
        input("Нажмите Enter для продолжения...")
        return

def create_contact():
    print('Введите')
    name = input('Имя: ')
    while True:
        phone = input('Телефон: ')
        if phone.startswith("+") and phone[1:].isdigit() or phone.isdigit():
            break
        else:
            print('Телефон должен начинаться с + и/или содержать только цифры')
    comment = input('Комментарий: ')
    new_cont_add = {
        'name': name,
        'phone': phone,
        'comment': comment
    }
    return new_cont_add

def search_contacts(contacts, querys):
    found = False
    print('\nКонтакты: ')
    print('-------------------------')
    for cont_ons in contacts:
        if querys.lower() in cont_ons['name'].lower() or querys.lower() in cont_ons['phone'].lower() or querys.lower() in cont_ons['comment'].lower():
            print("ID:", cont_ons['id'])
            print("Имя:", cont_ons['name'])
            print("Тел:", cont_ons['phone'])
            print("Коммент:", cont_ons['comment'], '\n')
            found = True
    if found:
        print('-------------------------')
        input("Нажмите Enter для продолжения...")
    if not found:
        print('не найдены\n')
        input("Нажмите Enter для продолжения...")
    return

def delete_contact(contacts_full):
    ret_contacts = []
    found_cont = None
    while True:
        contact_id_del = input('ID контакта для удаления: ')
        if contact_id_del.isdigit():
            found = False
            for one_cont in contacts_full:
                if one_cont['id'] == int(contact_id_del):
                    found = True
                    found_cont = one_cont
                    break
            if found:
                for cont_del in contacts_full:
                    if cont_del['id'] != int(contact_id_del):
                        ret_contacts.append(cont_del)
                print('---------Удален контакт----------')
                print(f"Имя: {found_cont['name']}")
                print(f"Телефон: {found_cont['phone']}")
                print(f"Комментарий: {found_cont['comment']}")
                print('-------------------------------------')
                input("Нажмите Enter для продолжения...")
                return ret_contacts
            else:
                print('Необходимо указать существующий ID')
        else:
            print('ID должен быть числом')

def exit_save_quest(get_fil_nam, loaded_contacts):
    with open(get_fil_nam, 'r+', encoding='utf-8') as file_read_write:
        load_cont_from_fil = json.load(file_read_write)
        if loaded_contacts != load_cont_from_fil:
            print(f'Изменения не сохраненны в файл телефонной книги {get_fil_nam}')
            while True:
                save_news = input(f'Сохранить изменения в {get_fil_nam}? y/n ').strip().lower()
                if save_news == 'y':
                    file_read_write.seek(0)
                    file_read_write.truncate()
                    json.dump(loaded_contacts, file_read_write, ensure_ascii=False, indent=4)
                    print(f'Изменения сохранены в файл телефонно книги {file_read_write}')
                    input("Нажмите Enter для выхода")
                    break
                elif save_news == 'n':
                    save_new(loaded_contacts)
                    print('Программа завершена')
                    break
                else:
                    print('Введите y/n')

def edit_contact(all_contacts):
    while True:
        contact_id_edit = input('ID контакта для редактирования: ')
        found_contact = None
        if contact_id_edit.isdigit():
            for one_conts in all_contacts:
                if one_conts['id'] == int(contact_id_edit):
                    found_contact = one_conts
                    break
            if found_contact is None:
                print("Контакт с таким ID не найден.")
                return all_contacts

            print('---------Изменяемый контакт----------')
            print(f"Имя: {found_contact['name']}")
            print(f"Телефон: {found_contact['phone']}")
            print(f"Комментарий: {found_contact['comment']}")
            print('-------------------------------------')
            print('Enter оставляет текущее значение изменяемого поля')
            ed_name = input(f'Изменить имя - {found_contact["name"]}:')
            if ed_name:
                found_contact['name'] = ed_name
            ed_phone = input(f'Изменить телефон - {found_contact["phone"]}:')
            if ed_phone:
                found_contact['phone'] = ed_phone
            ed_comment = input(f'Изменить коммент - {found_contact["comment"]}:')
            if ed_comment:
                found_contact['comment'] = ed_comment
            print("Контакт успешно изменен.")
            return all_contacts
        else:
            print('ID должен быть числом')
