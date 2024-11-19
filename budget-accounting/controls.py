from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from shifrator import shifrovka
from connect import Database
from querys import create_schema
from datetime import datetime
from plot import plotting

connect = Database.create_connection('1.sqlite')#запрос к подключению к БД

    
class app():
    def __init__(root):
        global ID_entry, balance_entry, balance_lbl, ID_lbl, btn_bal, cmb_amount, cmb_user, btn_show, entry_all, btn_add, name_entry,balance_entry
        if cmb.get() != '':                
            if cmb.get() == 'Вывести данные':                                  #При выборе "вывести данные" создаётся 1 текстовое сообщение, 2 поля ввода и кнопка для вызова функции
                app.frame_clear()
                Values = Database.execute_read_query(connect, """select name from users""")
                Values.append('Все')
                txt = Label(frame, text = 'Выберите количество строк и чьи операции вывести').place(x = 225, y = 50)
                cmb_amount = Combobox(frame, values = ['5', '10', '30'])
                cmb_amount.place(x = 5, y = 100)
                cmb_user = Combobox(frame, values = Values)
                cmb_user.place(x = 600, y = 100)
                btn_show = Button(frame, text = 'Вывести!', command = app.show_querry, width = 30).place(x = 275, y = 95)
                
            elif cmb.get() == 'Добавить покупку':                              #При выборе "добавить покупку" создаётся 1 текстовое сообщение, 1 поле ввода, 1 кнопка для вызова функции
                app.frame_clear()    
                txt = Label(frame,text = 'Введите, что купили, его стоимость и id купившего человека', font = ('Times New Roman', 14)).place(x = 150, y = 75)
                txt_entry = Label(frame,text = 'Наименование товара стоимость id пользователя', font = ('Times New Roman', 12)).place(x = 5, y = 100)
                entry_all = Entry(frame,width = 50)
                entry_all.place(x = 5, y = 125)
                btn_add = Button(frame,text = 'Добавить покупку', command = app.insert_purchase, width = 30)
                btn_add.place(x = 575, y = 125)
                
            elif cmb.get() == 'Добавить пользователя' and root == 1:           #При выборе "Добавить пользователя" создаётся 1 текстовое сообщение, 2 поля ввода и 1 кнопка для вызова функции
                app.frame_clear()
                txt = Label(frame, text = 'Введите имя, и начальный баланс пользователя', font = ('Times New Roman', 14)).place(x = 150, y = 75)
                name_entry = Entry(frame, width = 40)
                name_entry.place(x = 5, y = 100)
                balance_entry = Entry(frame, width = 40)
                balance_entry.place(x = 500, y = 100)
                btn_append = Button(frame, text = 'Добавить пользователя!', command = app.append_user).place(x = 300, y = 125)
                
            elif cmb.get() == 'Удалить пользователя' and root == 1:            #При выборе "Удалить пользователя" создаётся 1 текстовое сообщение, 1 поле ввода, 1 кнопка для вызова функции
                app.frame_clear()
                txt = Label(frame, text = 'Введите имя пользователя', font = ('Times New Roman', 14)).place(x = 250, y = 75)
                name_entry = Entry(frame, width = 40)
                name_entry.place(x = 500, y = 100)
                btn_delete = Button(frame, text = 'Удалить пользователя', command = app.delete_user).place(x = 5, y = 100)
                
            elif cmb.get() == 'Увеличить баланс' and root == 1:                #При выборе "увеличить баланс" создаёт 2 поля для ввода, 3 текстовых сообщения и кнопку для вызова функции
                app.frame_clear()
                txt = Label(frame,text = 'Введите имя и на сколько будет увеличен баланс')    #создание текста в окне приложения
                balance_entry = Entry(frame, width = 30)
                balance_entry.place(x = 525, y = 100)
                balance_lbl = Label(frame, text = 'Введите на сколько увеличить баланс', font = ('Times New Roman', 12)).place(x = 490, y = 75)
                ID_entry = Entry(frame, width = 30)
                ID_entry.place(x = 25, y = 100)
                ID_lbl = Label(frame,text = 'Введите кому добавить бюджет', font = ('Times New Roman', 12)).place(x = 5, y = 75)
                btn_bal = Button(frame, command = app.update_balance, text = 'Увеличить баланс!', width = 30)
                btn_bal.place(x = 275, y = 95)
                
            elif cmb.get() == 'Посмотреть баланс':
                app.frame_clear()
                app.show_balance()
            
            elif cmb.get() == 'Построить график трат':
                app.frame_clear()
                plotting.__init__(window, frame)
                
            else:
                text = 'Произошла ошибка в выборе функций приложения'
                app.show_window(text)                                          #Показывает сообщение об ошибке
    
    def frame_clear():
        global frame
        list = window.slaves()
        for i in list:
            i.destroy()
        frame = Frame(window)
        frame.pack(side="bottom", expand=False, fill="both", ipady = 300, ipadx = 300)
    
    def place_lbl(self, string, amount):                                       #Вывод результата запроса в окно приложения
        txt = ''
        if amount >= 15:
            amount -= 15 
            X = 80
            tbl_2 = Label(frame, text = 'Название || стоимость || ID пользователя || Дата покупки', font = ('Times New Roman', 8)).place(x = 5 * X, y = 150)
        else:
            X = 1
        for i in string:
            txt += str(i) + '||'                                               #Добавление разделителя
        self.lbl = Label(frame, text = txt, font = ('Times New Roman', 12))    #Вывод текста на экран
        self.lbl.place(x = 5 * X, y = (200 + 20*amount))

    def show_window(txt):                                                      #Создание окна в котором будет написано сообщение о ошибке/подтверждение выполнения запроса
        root = Tk()
        root.title('additional information')
        root.geometry('450x150')
        lbl = Label(root, text = txt, font = ('Times New Roman', 14)).place(x = 5, y = 5)
        root.mainloop()     
            
                
    def main(root):                                                            #Запуск ГПИ
        print(root)
        if root == (1,):
            values = ['Увеличить баланс', 'Вывести данные', 'Добавить покупку', 'Добавить пользователя', 'Удалить пользователя', 'Посмотреть баланс', 'Построить график трат']
        else:
            values = ['Вывести данные', 'Добавить покупку', 'Посмотреть баланс', 'Построить график трат']
        global cmb, window, frame
        window = Tk()
        window.title('Учёт покупок и бюджета')                                 #Присвоение загаловка приложению
        window.geometry('750x750')                                             #Задача размеров окна
        btn = Button(text = 'Выбрать!', width = 23, command = lambda root=root: app.__init__(root)).place(x = 600, y = 0)   #создание кнопки
        cmb = Combobox(value = values)                                         #создание выпадающего списка
        cmb.place(x = 5, y = 0)
        frame = Frame(window)
        frame.pack(side="bottom", expand=False, fill="both", ipady = 300, ipadx = 300)
        window.mainloop()                                                      #зацикливание работы приложения
        

    def show_balance():                                                        #Вывод баланса на экран
        query = """ select * from users;
        """                                                                    #Запрос к бд
        
        users = Database.execute_read_query(connect, query)
        for i in range(len(users)):
            app.place_lbl(app, users[i], i)                                    #вывод данных по пользователю на экран
    
    def delete_user():                                                         #Удаление пользователя и записей о нём из бд
        try:
            ID = Database.execute_read_query(connect, f"""select  user_id from purchases join users on purchases.user_id = users.id where name == '{name_entry.get()}'""") #Запрос на получение id пользователя подлежащему удалению
            
            query = f"""Delete from users
            where name == '{name_entry.get()}';
            """                                                                #Удаление пользователя
            
            Database.execute_query(connect, query)                             #Отправить запрос к БД
            
            query = f"""Delete from purchases where user_id = '{ID}';"""       #Удаление списка покупок пользователя
            
            Database.execute_query(connect, query)
            
            text = 'Запрос успешно выполнен'
            app.show_window(text)                                              #Вывод сообщения в отдельном окне о том, что запрос успешном выполнен
            
            
            
        except ValueError:
            text = 'Неверно введены параметры'
            app.show_window(text)                                              #Вывод сообщения в отдельном окне о том, что запрос не выполнен
    
    def append_user():                                                         #Добавление пользователя
        try:
            Name = name_entry.get()
            Balance = balance_entry.get()
            query = f"""
            insert into users (name, balance)
            values('{Name}', '{Balance}')
            """                                                                #Запрос на добавление пользователя в таблицу
            Database.execute_query(connect, query)
            
            text = 'Запрос успешно выполнен'
            app.show_window(text)                                               #Вывод сообщения в отдельном окне о том, что запрос успешном выполнен
        except ValueError:
            text = 'Неверно введены параметры'
            app.show_window(text)                                              #Показывает сообщение об ошибке
    def insert_purchase():                                                     #вставка строк в таблицу purchases 
        try:
            string = entry_all.get()
            Name, Cost, ID = string.split()
            Cost = str(Cost)
            ID = str(ID)
            
            querry = f"""insert into purchases(name_purchase, cost, user_id, date)
            values ('{Name}', '{Cost}', '{ID}', '{datetime.today().strftime('%Y-%m-%d')}');
            """                                                                #Запрос вставить в таблицу purchases строчку
            
            Database.execute_query(connect, querry)                            #Отправить запрос к БД
            text = 'Запрос успешно выполнен'
            app.show_window(text)                                              #Показывает сообщение о выполнении запроса к бд
            
        except ValueError:
            text = 'Неверно введены параметры'
            app.show_window(text)                                              #Показывает сообщение об ошибке
        
    def update_balance():                                                      #Обновление баланса
        try:
            ID = int(ID_entry.get())
            Bal = int(balance_entry.get())
            querry = f"""
            update users
            set balance = {Bal} + balance
            where id == {ID};
            """                                                                #Запрос на обновление баланса пользователю
    
            select_users = "SELECT * from users"
            users = Database.execute_read_query(connect, select_users)
            
            Database.execute_query(connect, querry)
            tbl = Label(text = 'ID  Имя  Баланс').place(x = 5, y = 125)
            for i in range(len(users)):
                app.place_lbl(app, users[i], i)
            
            text = 'Запрос успешно выполнен'
            app.show_window(text)                                              #Вывод сообщения в отдельном окне о том, что запрос успешном выполнен
            
        except ValueError:
            text = 'Неверно введены параметры'
            app.show_window(text)                                              #Показывает сообщение об ошибке
        

    def show_querry():                                                         #запрос вывода последних n покупок 
        names = cmb_user.get()
        k = int(cmb_amount.get())
        if names == 'Все':
            select_users = """
            select * from purchases;
            """                                                                #запрос на получение всех строк с таблицы purchases
        else:
            select_users = f"""
            Select name_purchase, cost, user_id, date from purchases join users on purchases.user_id = users.id 
            where users.name like '{names}';
            """                                                                #запрос на получение всех строк с таблицы purchases, где имя пользователя задано
        
        users = Database.execute_read_query(connect, select_users)             #отправление запроса к БД
        while len(users) > k:
            users.pop(0)
            if len(users) == k:
                break
        
        for i in range(k):
            if i == len(users):
                break
            for user in users:
                app.place_lbl(app, users[i], i)                                #Выведение строчек на экран
        tbl_1 = Label(text = 'Название || стоимость || ID пользователя || Дата покупки', font = ('Times New Roman', 8)).place(x = 5, y = 150)
