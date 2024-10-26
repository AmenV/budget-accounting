import pandas as pd 
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from connect import Database
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

connect = Database.create_connection('1.sqlite')                               #запрос к подключению к БД
class plotting():
    def __init__(window):                                                      #Создание текстового сообщения, поля ввода и кнопки
        global entry_name
        txt = Label(window, text = 'Введите id пользователя, чей график будет выведен', font = ('Times New Roman', 14)).place(x = 5, y = 100)
        entry_name = Entry(window, width = 15)
        entry_name.place(x = 5, y = 125)
        btn_plot = Button(window, text = 'Построить график', command = lambda window = window: plotting.main(window))
        btn_plot.place(x = 250, y = 200)
        
    def main(window):
        purchase = []
        date = []
        name = []
        ID = entry_name.get()
        if ID != '':    
            select_purchases = f"""select cost, date from purchases where user_id like '{ID}';
            """                                                                #Получение данных покупок человека с вышевведённым ID
            array = Database.execute_read_query(connect, select_purchases)
            select_user = f"""select name from users where id = '{ID}'"""      #Получени имени 
            array2 = Database.execute_read_query(connect, select_user)
            for i in range(len(array)):                                        #размещение полученных данных в 2ух массивах
                purchase.append(array[i][0])
                date.append(array[i][1])
            fig = Figure(figsize = (6, 6), dpi = 100) 
            plot1 = fig.add_subplot(111) 
            
            plot1.bar(date, purchase)                                          #Построение графика
            plot1.legend(array2[0])                                            #Надпись
            canvas = FigureCanvasTkAgg(fig, master=window)                     #Создание полотна и размещение фигуры в окне
            canvas.draw()                                                      #Отрисовка полотна
            canvas.get_tk_widget().pack(side = TOP, expand = True)             #Размещение полотна
