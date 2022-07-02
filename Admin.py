import os

if not os.path.exists('C:/Users/User/PycharmProjects/Xakaton_Progect/Teachers'):
    os.mkdir('Teachers')
    os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect/Teachers')
    os.mkdir('Task')
if not os.path.exists('C:/Users/User/PycharmProjects/Xakaton_Progect/Students'):
    os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect')
    os.mkdir('Students')

login_dict = {}
os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect')

with open('All_persons.txt', 'a+', encoding='utf-8') as tabl:
    tabl.seek(0)
    for line in tabl:
        line = line.split()
        login_dict[line[0]] = [line[-2], line[-3], line[-1]]


class Admin:

    def add_teacher(self, add_login, add_name, add_password, add_title='Teach'):
        if add_login == Admin:
            print('Недопустимый логин')
        else:
            os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect')
            login_list = []
            with open('All_persons.txt', 'a+', encoding='utf-8') as tabl:
                tabl.seek(0)
                if len(tabl.read()) == 0:
                    tabl.write(f'{add_login} {add_name} {add_password} {add_title}\n')
                    login_list.append(add_login)
                else:
                    tabl.seek(0)
                    for line in tabl:
                        login, name, password, title = line.split()
                        if login not in login_list:
                            login_list.append(login)
                    if add_login not in login_list:
                        tabl.write(f'{add_login} {add_name} {add_password} {add_title}\n')


class Teacher:

    def list_student(self):
        for k, v in login_dict.items():
            if v[-1] == 'Stud':
                print(f"- {k}, {v[1]}")

    def send_task(self, name, test):
        os.replace(f'Task/{test}', f'Students/{name}/{test}')


class Student:

    def registration(self, add_login, add_name, add_password, add_title="Stud"):
        if add_login == Admin:
            print('Недопустимый логин')
        else:
            os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect')
            with open('All_persons.txt', 'a+', encoding='utf-8') as tabl:
                login_list = []
                tabl.seek(0)
                if len(tabl.read()) == 0:
                    tabl.write(f'{add_login} {add_name} {add_password} {add_title}\n')
                    login_list.append(add_login)
                    os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect/Students')
                    os.mkdir(add_login)
                else:
                    tabl.seek(0)
                    for line in tabl:
                        login, name, password, title = line.split()
                        if login not in login_list:
                            login_list.append(login)
                    if add_login not in login_list:
                        tabl.write(f'{add_login} {add_name} {add_password} {add_title}\n')
                        os.chdir('C:/Users/User/PycharmProjects/Xakaton_Progect/Students')
                        os.mkdir(add_name)


sign_in_login = input('Введите логин: ')
if sign_in_login == 'a':
    sign_in_password = input('Введите пароль: ')
    if sign_in_password == 'a':
        account = Admin()
    while True:
        command = input(f'Выберите команду:\n1. Добавить учителя\n2. Выйти из программы\n')
        if command == '1':
            account.add_teacher(input('Введите логин: '), input('Введите имя: '), input('Введите пароль: '))
        elif command == '2':
            break

elif sign_in_login in login_dict:
    sign_in_password = input(('Введите пароль: '))
    if sign_in_password == login_dict[sign_in_login][0] and login_dict[sign_in_login][-1] == 'Teach':
        account = Teacher()
        command = input(f'Выберите команду:\n1. Список учащихся.\n2. Отправить задание.\n3. Проверка работ.\n')
        if command == '1':
            account.list_student()
        elif command == '2':
            account.send_task(input('Введите имя ученика: '), input('Введите название файла задания: '))
        elif command == '3':
            pass

    elif sign_in_password == login_dict[sign_in_login[0]] and login_dict[sign_in_login[-1]] == 'Stud':
        account = Student()
        account.registration(input('Введите логин: '), input('Введите имя: '), input('Введите пароль: '))
else:
    title = input(f'Вы \n1. Студент или \n2. Преподователь\n')
    if title == '1':
        Student().registration(input('Введите логин: '), input('Введите имя: '), input('Введите пароль: '))
    elif title == '2':
        print('У вас недостаточно прав для регистрации учителя')
