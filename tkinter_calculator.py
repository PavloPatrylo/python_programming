
import tkinter as tk
from tkinter import messagebox 
import matplotlib.pyplot as plt
import math as m
import sys

def add():
    entered = input.get()
    numbers = [float(num) for num in entered.split()]

    result = 0
    if len(numbers) == 1:
        result = numbers[0]
    if len(numbers)>1:
        for i in range(len(numbers)):
            result += numbers[i]

    output.delete(0, tk.END)
    output.insert(0, str(result))

def diff():
    entered = input.get()
    numbers = [float(num) for num in entered.split()]

    result = 0
    if len(numbers) == 1:
        result = numbers[0]
    if len(numbers)>1:
        for i in range(len(numbers)):
            result = numbers[i] - numbers[i-1]

    output.delete(0, tk.END)
    output.insert(0, str(result))

def square():
    entered = input.get()
    numbers = [float(num) for num in entered.split()]

    numbers.sort()

    result = [n**2 for n in numbers]
    
    output.delete(0, tk.END)
    output.insert(0, ' '.join(map(str, result)))

    graph(numbers, result)

def graph(numbers, result):
    plt.figure('квадратична залежність')
    plt.plot(numbers,result,linestyle='-', color='b')
    plt.xlabel("Числа")
    plt.ylabel("Квадрати") 
    plt.grid(True)
    plt.show()

def _sqrt():
    entered = input.get()
    numbers = [float(num) for num in entered.split()]
    
    if sqrt_check(numbers):
        messagebox.showerror("Помилка", "Негативні числа не можуть мати квадратний корінь")
        sys.exit()

    numbers.sort()

    result = [m.sqrt(n) for n in numbers]
    
    output.delete(0, tk.END)
    output.insert(0, ' '.join(map(str, result)))

    sqrt_graph(numbers, result)


def sqrt_graph(numbers, result):
    plt.figure('Коренева залежність')
    plt.plot(numbers,result,linestyle='-',marker='o' ,color='b')
    plt.xlabel("Числа")
    plt.ylabel("Корені") 
    plt.grid(True)
    plt.show()

def sqrt_check(numbers):
    for n in numbers:
        if n<0:
            return True


root = tk.Tk()
root.title('Калькулятор чисел')
root.geometry("300x200")

label1 = tk.Label(root, text='Введіть одне або два числа через пробіл')
label1.place(x=10, y=20)

input = tk.Entry(root, width=30)
input.place(x=50, y=50)

label2 = tk.Label(root, text='Результат')
label2.place(x=10, y=120)

output = tk.Entry(root, width=30)
output.place(x=50, y=140)

add_button = tk.Button(root, text="+", command=add, width=5, height=2)
add_button.place(x=20, y=75)

diff_button = tk.Button(root, text='-', command=diff, width=5,height=2)
diff_button.place(x=70,y=75)

squared_button = tk.Button(root, text='square', command=square, width=10,height=2)
squared_button.place(x=125,y=75)

sqrt_button = tk.Button(root, text='sqrt', command=_sqrt, width=10,height=2)
sqrt_button.place(x=210,y=75)
root.mainloop()
