# Plotly хорош для построения интерактивной визуализации. Подходит для браузера, автоматически маштабирует под размеры экрана
# Будем анализировать результаты бросков кубиков
# pip install plotly

# Создадим класс кубика
from random import randint

class Cub():
    """Класс, представляющий один кубик"""
    def __init__(self, num_side=6):
        """Шестигранный кубик"""
        self.num_side = num_side

    def roll(self):
        """Берем случайное число от 1 до 6"""
        return randint(1, self.num_side)