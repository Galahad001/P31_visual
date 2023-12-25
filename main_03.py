# Случайные точки
from random import choice

class Rand():
    """Класс для генерирования случайных блужданий"""
    def __init__(self, col_point=5000):
        """Инициальзировать атрибуты блуждания"""
        self.col_point = col_point

        # Все блуждания начинаются с точки (0,0)
        self.x_arr = [0]
        self.y_arr = [0]


    def walk(self):
        """Вычисляет все точки блуждания"""

        # Шаги генерируются до достижения нужной длины
        while len(self.x_arr) < self.col_point:

            # Определение направления и длины перемещения
            x_nap = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_nap * x_distance

            y_nap = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_nap * y_distance

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений
            x = self.x_arr[-1] + x_step
            y = self.y_arr[-1] + y_step

            self.x_arr.append(x)
            self.y_arr.append(y)
