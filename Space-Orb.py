import tkinter as tk
from tkinter import messagebox
import math
from tkinter import *
import tkinter as ttk





def validate_input(entry):
    content = entry.get()
    if content.replace('.', '', 1).isdigit():   
        return True
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение")
        return False


def calculate_orbital_velocity(radius_entry):
    if validate_input(radius_entry):
        radius = float(radius_entry.get())
        
        orbital_velocity = round((G * M / radius)**0.5, 2)   
        result_label.config(text=f"Орбитальная скорость: {orbital_velocity} м/с")


def show_information():
    info = "Первая космическая скорость V1 - скорость, необходимая для обращения спутника по круговой орбите вокруг Земли или другого космического объекта                           Первая космическая скорость: 7.9 км/с\n"
    info += "Вторая космическая скорость V2 - минимальная скорость, которую должно иметь свободно движущееся тело на расстоянии R от центра Земли или другого космического тела, чтобы, преодолев силу гравитационного притяжения, навсегда покинуть его.                                        Вторая космическая скорость: 11.2 км/с\n"
    messagebox.showinfo("Интересно знать", info)

bg = "white"
def change_theme():  
    global bg
    current_bg = window.cget("bg")  
    new_bg = "white" 
    if current_bg == "gray":
        new_bg = "white"
        window.configure(bg=new_bg) 
    else:
        new_bg = "gray"
        window.configure(bg=new_bg)
    

window = tk.Tk()
window.title("Space-Orb")
window.geometry("500x300")
window.iconbitmap("sp.ico")


def change_planet():
    
    
    planet = planet_variable.get()
    global G, M
    if planet == "Земля":
        G = 6.67430e-11   
        M = 5.972e24   
    elif planet == "Луна":
        G = 6.67430e-11   
        M = 7.342e22   
    elif planet == "Марс":
        G = 6.67430e-11   
        M = 6.39e23   
    elif planet == "Юпитер":
        G = 6.67430e-11   
        M = 1.989e30   
    elif planet == "Сатурн":
        G = 6.67430e-11  
        M = 5.683e26   
    elif planet == "Нептун":
        G = 6.67430e-11   
        M = 1.024e26   
    elif planet == "Уран":
        G = 6.67430e-11   
        M = 8.681e25   
    elif planet == "Меркурий":
        G = 6.67430e-11   
        M = 3.302e23   


planet_options = ["Земля", "Луна", "Марс", "Юпитер", "Сатурн", "Нептун", "Уран", "Меркурий"]   
planet_variable = tk.StringVar(window)
planet_variable.set(planet_options[0])   

planet_dropdown = tk.OptionMenu(window, planet_variable, *planet_options)
planet_dropdown.place(x = 0, y = 110)

change_planet_button = tk.Button(window, text="OK", command=change_planet)
change_planet_button.place(x = 75, y = 112)



radius_label = tk.Label(window, text="Введите радиус орбиты (в метрах):")
radius_label.place(x = 0, y = 0)

radius_entry = tk.Entry(window)
radius_entry.place(x = 200, y = 0)

calculate_button = tk.Button(window, text="Рассчитать орбитальную скорость", command=lambda: calculate_orbital_velocity(radius_entry))
calculate_button.place(x = 0, y = 20)

result_label = tk.Label(window, text="Ждём запрос")
result_label.place(x = 205, y = 22)

info_button = tk.Button(window, text="Справочник", bg = "#8B93FF", fg = "white", command=show_information)
info_button.place(x = 422, y = 275)

change_theme_button = ttk.Button(window, text="🌑", command=change_theme) 
change_theme_button.place(x = 460, y = 0)

text_point = tk.Label(window, text="Выберите планету", font=("Arial", 16)) 
text_point.place(x=0, y=80)

window.mainloop()