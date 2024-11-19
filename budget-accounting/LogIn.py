from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from controls import app
from connect import Database
from shifrator import shifrovka

class LogIn():                                                                 #Создание класса для входа в систему
    def __init__():                                                            #Создание окна и приложения
        global Root, connect
        connect = Database.create_connection('1.sqlite')                       #запрос к подключению к БД
        Root = Tk()                                                            #Создание окна входа в систему
        Root.title('Вход в систему')                                           #Название окна
        Root.geometry('400x350')                                               #Выставление размеров
        LogIn.main()
        Root.mainloop()
        
    def take_passwords():
        global root_q
        ans = []
        string = ''
        logins = []
        passwords = []
        query = """select * from logins"""                                     #получение закодированных логинов и паролей
        temp = Database.execute_read_query(connect, query)
        root = """select root from logins;"""
        root_q = Database.execute_read_query(connect, root)
        for i in range(len(temp)):
            string += temp[i][1] + ' ' + temp[i][2] + ' '                      #запись закодированных логинов и паролей в строку
        string = shifrovka.v_deshifr(string)                                   #Декодирование
        ans = string.split(' ')                                                #Сплит по пробелу
        ans.pop()                                                              #Удаление последнего элемента (пробела)
        for i in range(len(ans)):                                              #загрузка массивов из общего массива
            if i % 2 == 0:
                logins.append(ans[i])                   
            else:
                passwords.append(ans[i])
        LogIn.Login(logins, passwords)
        
    def main():                                                                #Создание 2 полей ввода, 1 текстового сообщения и 1 кнопки
        global entry_login, entry_pass
        txt = Label(text = 'Введите логин и пароль для входа в систему', font = ('Times New Roman', 14)).place(x = 5, y = 5)
        entry_login = Entry(width = 40)
        entry_login.place(x = 75, y = 100)
        entry_pass = Entry(width = 40, show = '*')
        entry_pass.place(x = 75, y = 200)
        btn = Button(text = 'Войти в систему', command = LogIn.take_passwords).place(x = 150, y = 250)
        
    def Login(logins, passwords):                                              #проверка, что введёный логин и пароль есть в системе
        if entry_login.get() != '' and entry_pass.get() != '':
            log = entry_login.get()
            pas = entry_pass.get()
            for i in range(len(logins)):
                if log == logins[i] and pas == passwords[i]:                   #Логин
                    Root.destroy()                                             #Уничтожение окна
                    print(root_q)
                    print(root_q[i])
                    app.main(root_q[i])                                        #Создание основного окна
                elif log != logins[i] or pas != passwords[i]:
                    ans = Label(Root, text = 'Логин или пароль введены не верно').place(x = 5, y = 300) #Выведение сообщения
