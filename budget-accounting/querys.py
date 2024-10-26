from connect import Database   
from datetime import datetime
import random as r     
import sqlite3
from sqlite3 import Error                                                      

class create_schema():
    global connect 
    def __init__():
        create_schema.create_tables()
        create_schema.create_trigger()
        
        
    def create_tables():
        create_users_table = """                                                     
        CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          balance integer
        );
        """                                     
        Database.execute_query(connect, create_users_table)                    #создание таблицы users
                                                                               #Создание таблицы покупки
        create_purchases_table = """                                                   
        CREATE TABLE IF NOT EXISTS purchases (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name_purchase TEXT,
          cost integer NOT NULL,    
          user_id INTEGER NOT NULL, 
          date DATE Not NULL,
          FOREIGN KEY (user_id) REFERENCES users (id)                                
        );
        """    
        Database.execute_query(connect, create_purchases_table)

        create_logins_table = """
        create table if not exists logins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login Text NOT NULL,
            password Text NOT NULL,
            user_id INTEGER NOT NULL,
            foreign key (user_id) references users (id)
        );
        """                                                                    #Создание таблицы с логинами и паролями                                    
        Database.execute_query(connect, create_logins_table) 
    def create_trigger():
        create_trigger_purchases = """                                               
        create trigger if not exists upd_balance after insert on purchases for each row
        begin
            update users
                set balance = balance - new.cost
                where id = new.user_id;
        end
        """                                                                    #Создание триггера
        Database.execute_query(connect, create_trigger_purchases)
connect = Database.create_connection('1.sqlite')                               #запрос к подключению к БД





# create_users = """                                                           #Запрос для ввода пользователей
# Insert into users(name, balance)
# values('Ранис', 100000),
# ('Чингис', 100000),
# ('Тимур', 100000);
# """
# Name = ['яблоки', 'груши', 'апельсины', 'мандарины', 'Сок', 'Энергетик']
# Cost = [50, 70, 120, 100, 200, 50]
# Users = ['Ранис', 'Чингис', 'Тимур']
# # query = """Delete from logins
# # """
# # Database.execute_query(connect, query)
# # create_schema.__init__()
# # query = """
# # insert into logins (login, password, user_id)
# # values ('rdznб', 'rdznб', '1'),
# # ('гoqjеrtбw', 'ъядсх', '2'),
# # ('зиeд', 'фыыьфупртсрj', '3');
# # """
# # Database.execute_query(connect, query)
# for i in range(30):                                                          #Запросы для ввода покупок
#     rand = []
#     rand.append(Name[r.randint(0, 5)])
#     rand.append(Cost[r.randint(0, 5)])
#     rand.append(r.randint(1, 3))
#     rand.append(datetime.today().strftime('%Y-%m-%d'))
#     create_purchases = f"""
#     INSERT INTO
#     purchases (name_purchase, cost, user_id, date)
#     values ('{rand[0]}', '{rand[1]}', '{rand[2]}', '{rand[3]}');
#     """

#     Database.execute_query(connect, create_purchases)
# Database.execute_query(connect, create_users)
# select_users = "SELECT * from users"
# users = Database.execute_read_query(connect, select_users)
# purch = Database.execute_read_query(connect, "SELECT * from purchases")
# for user in users:
#     print(user)
# for p in purch:
#     print(p)
