from main_cub import Cub

# Построим гистограмму
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание двух кубиков
die_1 = Cub()
# die_2 = Cub()

# Смоделируем серии бросков
res = []
for roll in range(1000):
    result = die_1.roll()
    res.append(result)

# print(res)
    
# Анализ результатов
frequencies = []
for value in range(1, die_1.num_side+1):
    fre = res.count(value)
    frequencies.append(fre)

# print(frequencies)
    

# Визуализация результатов
    # Для постройки столбцов для диаграммы используем x_values
x_valeus = list(range(1, die_1.num_side+1))
    # Класс Bar предоставляет набор данных, которые будут форматироватся в виде столбцевой диаграммы
data = [Bar(x=x_valeus, y=frequencies)]

    #   Для осей предусмотренны различные возможности , каждый параметр сохраняется в виде элемента в словаре. Меняем заголовки осей
x_axis_config = {'title':'Result'}
y_axis_config = {'title':'Frequency of appearing'}
    # Возвращает обьект который задает макет и конфигурацию программы в целом
my_layout = Layout(title='Результаты 1000 бросков', xaxis=x_axis_config, yaxis=y_axis_config)
    # Строит график. Функции передается словарь с обьектами и макет, также задаем имя файла для сохранения
offline.plot({'data':data, 'layout':my_layout}, filename='cub.html')

