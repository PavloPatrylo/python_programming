import pandas as pd
import tkinter as tk
from tkinter import messagebox
import ipywidgets as widgets
from IPython.display import display

# Читання CSV файлів
assortment = pd.read_csv('assortment.csv', names=['ID', 'name', 'category', 'discount'])
sales1 = pd.read_csv('sales1.csv', names=['ID', 'amount'])
sales2 = pd.read_csv('sales2.csv', names=['ID', 'amount'])
sales = pd.concat([sales1, sales2])
tarif = pd.read_csv("tarif.csv", names=["ID", "price"])

# Перевірка на коректність даних
print(assortment.head())
print(sales.head())
print(tarif.head())

# Злиття даних
data1 = pd.merge(assortment, sales, on='ID', how='inner')
data = pd.merge(data1, tarif, on='ID', how='inner')

# Обчислення реальної ціни і суми
data['real_price'] = data['price']
data.loc[data['discount'] == 'Yes', 'real_price'] *= 0.9
data['summary'] = data['real_price'] * data['amount']

# Перевірка наявності категорій
print(data['category'].unique())

# Функція для виведення товарів категорії "One"
def show_category_one(data):
    filtered_data = data[data['category'] == 'One']
    
    if filtered_data.empty:
        output_label.value = "No products found in category 'One'."
    else:
        result = "\n".join([f"{row['name']} - {row['summary']}" for index, row in filtered_data.iterrows()])
        output_label.value = f"Category 'One' Products:\n{result}"

# Створення віджету кнопки
button = widgets.Button(description="Show Category One")

# Створення віджету для відображення результатів
output_label = widgets.Label(value="")

# Прив'язка функції до кнопки
button.on_click(lambda x: show_category_one(data))

# Виведення віджетів
display(button, output_label)