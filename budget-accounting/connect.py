import sqlite3
from sqlite3 import Error
class Database():

    def create_connection(path):                                               #коннект к БД/её создание
        connection = None
        try:
            connection = sqlite3.connect(path)                                 #Подключение к бд
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
    
        return connection
    
    
    def execute_query(connection, query):                                      #Создание запроса к бд
        cursor = connection.cursor()                                           #создание курсора
        try:
            cursor.execute(query)                                              #выведение запроса
            connection.commit()                                                #подтверждение связи с бд
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")
            
    def execute_read_query(connection, query):                                 #чтение результата запроса
        cursor = connection.cursor()                
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")
            
            
connect = Database.create_connection('1.sqlite')                               #запрос к подключению к БД