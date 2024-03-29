# Matplotlib - матиматически=ая библтот=тека по построению диаграмм.
# Plotly - создание визуализации для цифровых устройств. Автоматически маштаюирует по размерам экрана, генерирует визуализацию
# pip install matplotlib
import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Применить стиль к диаграмме
plt.style.use('seaborn-v0_8-darkgrid')

# Функция позволяет сгенерировать одну или несколько поддиаграмм на одной диаграмме. fig - представляет весь рисунок цедиком. ax -представляет одну одну диаграмму на рисунке
fig, ax = plt.subplots()
# Толщина линии
ax.plot(input_values, squares, linewidth=3)

# Назначение заголовка диаграммы и меток осей
ax.set_title('МОЯ ДИАГРАММА', fontsize=20)
ax.set_xlabel('Горизонт', fontsize=14)
ax.set_ylabel('Вертикаль', fontsize=14)

# Назначение размера шрита делений на осях
ax.tick_params(axis='both',  labelsize=14)


# Пытается постороить диаграмму из переданных чисел
plt.show()

# pyplot - содержит ряд функций для построения диаграмм и графиков
# pyplot - если plot передается числовая последовательность то она считаетчто первый параметр соответсвует  0

# subplots - генирирует одну или несколько поддиаграмм на одной диаграмме. Переменная ax представляет одну диаграмму на рисунке, переменная fig представляет весь рисунок или набор генерируеммых диаграмм.

# plot - пытается построить  осмысленное графическое  представление для заданных чисел.
# show - выводит окно и выводит графиг.

# ------------
# linewidth - толщина линии
# set_title - Заголовок диаграммы
# set_xlabel и set_ylabel - назначить заголовки осей
# tick_params - определяет оформление делений на осях
# axis='both' - отношение к обеим осям
# labelsize - размер для меток делений

# -----------
# Можно использовать готовые стили для оформления диаграммы. Чтобы узнать какие стили есть можно прописать следующие print(plt.style.available)

# ----------
# Посмотреть втроенные стили для диаграмм print(plt.style.available)