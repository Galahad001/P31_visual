from main_cub import Cub
# Построим гистограмму
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Создание двух кубиков
die_1 = Cub()
die_2 = Cub(10)

# Смоделируем серии бросков
res = []
for roll in range(50000):
    result = die_1.roll() + die_2.roll()
    # 
    res.append(result)

# print(res)
    
# Анализ результатов
frequencies = []
max_res = die_1.num_side + die_2.num_side
for value in range(2, max_res+1):
    fre = res.count(value)
    frequencies.append(fre)

# print(frequencies)
    

# Визуализация результатов
    # Для постройки столбцов для диаграммы используем x_values
x_valeus = list(range(2, max_res+1))
    # Класс Bar предоставляет набор данных, которые будут форматироватся в виде столбцевой диаграммы
data = [Bar(x=x_valeus, y=frequencies)]

    #   Для осей предусмотренны различные возможности , каждый параметр сохраняется в виде элемента в словаре. Меняем заголовки осей
x_axis_config = {'title':'Result', 'dtick':1}
y_axis_config = {'title':'Frequency of appearing'}
    # Возвращает обьект который задает макет и конфигурацию программы в целом
my_layout = Layout(title='Результаты 1000 бросков от двух кибиков', xaxis=x_axis_config, yaxis=y_axis_config)
    # Строит график. Функции передается словарь с обьектами и макет, также задаем имя файла для сохранения
offline.plot({'data':data, 'layout':my_layout}, filename='cub_cub.html')

