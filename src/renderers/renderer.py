

import tkinter as tk
from typing import List, Dict


class Renderer:


    def __init__(self, canvas: tk.Canvas) -> None:
        """Инициализирует слой рендеринга, привязывая его к объекту холста.

        :param canvas: Экземпляр tk.Canvas для графического вывода примитивов.
        """
        self.canvas = canvas

    def render(self, drops: List[Dict[str, float]]) -> None:
        """Очищает экран и выполняет отрисовку капель дождя с эффектом перспективы.

        :param drops: Список объектов капель с их актуальными координатами.
        """
        self.canvas.delete("all")

        for drop in drops:
            x1 = drop["x"]
            y1 = drop["y"]
            x2 = x1
            y2 = y1 + drop["length"]

            # Псевдо-3D визуализация за счет цвета и толщины линии:
            # Дальние капли (малый z) — тонкие и тусклые, ближние — толстые и неоновые.
            if drop["z"] < 0.4:
                color = "#3d2b63"  # Дальний план (тускло-фиолетовый)
                width = 1
            elif drop["z"] < 0.7:
                color = "#7b5cb7"  # Средний план (умеренный фиолетовый)
                width = 2
            else:
                color = "#c39eff"  # Ближний план (яркий неоновый)
                width = 3

            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
