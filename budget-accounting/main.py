from connect import Database
from querys import create_schema
from LogIn import LogIn
      
def Main():
    connect = Database.create_connection('1.sqlite')                           #запрос к подключению к БД
    create_schema.__init__()                                                   #Создание/проверка наличия таблиц
    LogIn.__init__()                                                           #Запуск приложения

Main()      