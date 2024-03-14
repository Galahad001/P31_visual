import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Применить стиль к диаграмме
plt.style.use('seaborn-v0_8-darkgrid')


fig, ax = plt.subplots()
ax.scatter(input_values, squares,s=200)

# Назначение заголовка диаграммы и меток осей
ax.set_title('МОЯ ДИАГРАММА', fontsize=20)
ax.set_xlabel('Горизонт', fontsize=14)
ax.set_ylabel('Вертикаль', fontsize=14)

# Назначение размера шрита делений на осях
ax.tick_params(axis='both',  labelsize=14)


# Пытается постороить диаграмму из переданных чисел
plt.show()
