# Для нанесения на диаграмму отдельной точки используется функция scatter() и коодинаты нужной точки

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()

#  координаты точек
# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
# Второй вариант создания точек
x = list(range(1, 1001))
y = [i**2 for i in x]

# ax.scatter(x, y, c='red', s=10)
# s - задает размер точек
# Градиент
ax.scatter(x, y, c=y, cmap=plt.cm.Blues,  s=10)
# Передаем в с список у , затем указываем какя цветовая карта должна быть использована, при помощи аргумента cmap



# Назначение заголовка диаграммы и меток осей
ax.set_title('Моя', fontsize=24)
ax.set_xlabel('Г', fontsize=10)
ax.set_ylabel('В', fontsize=10)

ax.tick_params(axis='both', which='major', labelsize=10)

# Дапазон для каждой оси. axis - получает 4 параметра минимум и максимум по осям x и y
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('test_plot2.png')

# Сохранение диаграммы. Вместо plt.show() использовать plt.savefig()

 


# Цветовые карты позволяют задать градиент, плавный переход от начального цвета к конечному