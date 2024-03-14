'''Число возведенное в третью степень, куб. Нанести на диаграмму 5000 кубов'''
'''Применить цветовую карту'''
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()


# Второй вариант создания точек
# Список значений координат по x
x = list(range(1, 5001))
# по y
y = [i**3 for i in x]

# ax.scatter(x,y, c='red', s=10)
# Градиент
# Цветовая карта - серия цветов градтента, определяет плавный переход от начального цвета к конечному
ax.scatter(x, y, c=y, cmap=plt.cm.Blues,  s=10)
# Передаем в с список у , затем указываем какя цветовая карта должна быть использована, при помощи аргумента cmap



# Назначение заголовка диаграммы и меток осей
ax.set_title('Моя', fontsize=24)
ax.set_xlabel('Г', fontsize=10)
ax.set_ylabel('В', fontsize=10)

ax.tick_params(axis='both', which='major', labelsize=10)

# Дапазон для каждой оси. axis - получает 4 параметра минимум и максимум по осям x и y
ax.axis([0, 5100, 0, 125000000000])

plt.show()