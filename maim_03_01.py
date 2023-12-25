import matplotlib.pyplot as plt
from  main_03 import Rand

# # Построения случайного блуждания 
# rw = Rand()
# rw.walk()

# # Нанесение точек на диаграмму
# plt.style.use('classic')
# fig,ax =plt.subplots()
# ax.scatter(rw.x_arr, rw.y_arr, s=15)

# plt.show()




# Генерация блуждания строица пока не выйдем
while True:
 rw = Rand(50000)
 rw.walk()

 # Нанесение точек на диаграмму
 plt.style.use('classic')
 fig,ax =plt.subplots(figsize=(15, 9))
#  Генерируем список чисел - список равен количеству точек
 point_num = range(rw.col_point)
 ax.scatter(rw.x_arr, rw.y_arr, c=point_num, cmap=plt.cm.Blues, edgecolors='none', s=1)
#  edgecolors - убираем черный контур у точек
#  ax.scatter(rw.x_arr, rw.y_arr, s=15)
 

#  Выделение первой и последней точки
 ax.scatter(0,0, c='green', edgecolors='none', s=100)
 ax.scatter(rw.x_arr[-1], rw.y_arr[-1], c='red', edgecolors='none', s=100)

# Удаление осей
 ax.get_xaxis().set_visible(False)
 ax.get_yaxis().set_visible(False)

 plt.show()

 test = input('Выйти да/нет')
 if test == 'да':
  break