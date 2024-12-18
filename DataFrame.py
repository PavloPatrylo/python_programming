
import pandas as pd

data = {
    'Name': ['Anna', 'Boris', 'Catherine'],
    'Age': [24, 27, 22],
    'City': ['Kyiv', 'Lviv', 'Odessa']
}
df = pd.DataFrame(data)

names = df['Name'] #виведення імен, зіертаємося за ключем
print(names)

# пошук за індексом 
first_row_loc = df.loc[0]   # Використання методу loc
first_row_iloc = df.iloc[0] # Використання методу iloc
print(first_row_loc) #виведення 0 елемента
print(first_row_iloc) #виведення 0 елемента

#складні зрізи
subset = df.loc[0:1, ['Name', 'City']] #між двокрапкою вказуємо індексний діапазон, а вквадратних дужках параметри зрізу
print(subset)

print('\nПОВНА ТАБЛИЦЯ')
print(df)
print('\n')

#   ДОДАВАННЯ І ВИДАЛЕННЯ ЕЛЕМЕНТІВ (в pandas вісь 0 - це рядок, а 1 - це стовпець. inplace=True -- команда для зміни об'єкта)
df['Country'] = ['Ukraine', 'Ukraine', 'Ukraine'] # додавання стовпця країна
print(df)

df.drop('City', axis=1, inplace=True) # видалення стовпця з вказанням осі
print(df)

df.loc[3] = ['Dmitro', 25, 'Ukraine'] # додавання рядка на 3 позицію
print(df)
#df.loc[len(df)] = ['Dmitro', 25, 'Ukraine'] -- спосіб додати рядок в кінець 

df.drop(1, inplace=True) # коли ми не вказуємо вісь, то автоматично вважаємо, що працюмо з рядком. видалення 1 рядка
print(df)


#   КОНКАТЕНАЦІІЯ ПО РЯДКАХ І СТОПЦЯХ
print('\nКОНКАТЕНАЦІЯ ПО РЯДКАХ І СТОВПЦЯХ')

# Створення двох DataFrame, конкатенація за віссю 0
df1 = pd.DataFrame({
    'Name': ['Anna', 'Boris'],
    'Age': [24, 27]
})
df2 = pd.DataFrame({
    'Name': ['Catherine', 'Dmitro'],
    'Age': [22, 25]
})

# Конкатенація по рядках (додавання нових рядків)
df_res = pd.concat([df1, df2], ignore_index=True)
print(df_res)

# Конкатенація за вісю 1
df3 = pd.DataFrame({
    'City': ['Kyiv', 'Lviv'],
    'Country': ['Ukraine', 'Ukraine']
})

# Конкатенація по стовпцях (додавання нових стовпців)
df = pd.concat([df1, df3], axis=1)
print(df)


#    ЗЛИТТТЯ (merge)
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Anna', 'Boris', 'Catherine']
})
df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Age': [24, 27, 22]
})

# Злиття по спільному стовпцю 'ID'
df = pd.merge(df1, df2, on='ID', how='inner') # how - це вказання типу злиття, inner - це перетин
print(df)


#   ФІЛЬТРУВАННЯ (використання операторів & (AND), | (OR), ~ (NOT))
# фільтрування за умовою
df = pd.DataFrame({
    'Name': ['Anna', 'Boris', 'Catherine', 'Dmitro'],
    'Age': [24, 27, 22, 25],
    'City': ['Kyiv', 'Lviv', 'Odessa', 'Kyiv']
})
# фільтрування за одним паратметром
filtered_df = df[df['Age'] >= 25] # вибір рядків, де вік більше або рівний 25
print(filtered_df)
# фільтрування за двома параметрами
filtered_df = df[(df['Age'] >= 25) & (df['City'] == 'Kyiv')] #вибір рядків, де вік більше або рівний 25 ТА місто - Kyiv
print(filtered_df)
# фільтрування за 1 параметром, але 2 стовпцями
filtered_df = df[df['Age'] >= 25][['Name', 'City']] #Вибір стовпців 'Name' і 'City', де вік більше або рівний 25
print(filtered_df)

#   СОТРУВАННЯ
# Сортування за віком у порядку зростання
sorted_df = df.sort_values(by='Age')
print(sorted_df)

# Сортування за індексом
sorted_df = df.sort_index()
print(sorted_df)

# ФІЛЬТРУВАННЯ І СОРТУВАННЯ: вік більше 24, потім сортування за алфавітом за іменем
filtered_sorted_df = df[df['Age'] > 24].sort_values(by='Name')
print(filtered_sorted_df)

#   ПОВОРОТ ТАБЛИЦІ 
pivot_table_df = df.pivot_table(index='City', columns='Name', values='Age', aggfunc='mean')
print(pivot_table_df)
