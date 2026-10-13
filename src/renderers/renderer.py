"""Модуль графического отображения объектов сцены на виртуальном холсте."""

import tkinter as tk
from typing import List, Dict

class Renderer:
    """Графический отрисовщик элементов сцены на Canvas."""

    def __init__(self, canvas: tk.Canvas) -> None:
        self.canvas = canvas

    def render(self, drops: List[Dict[str, float]]) -> None:
        self.canvas.delete("all")
        for drop in drops:
            x1 = drop["x"]
            y1 = drop["y"]
            x2 = x1
            y2 = y1 + drop["length"]

            if drop["z"] < 0.4:
                color = "#3d2b63"
                width = 1
            elif drop["z"] < 0.7:
                color = "#7b5cb7"
                width = 2
            else:
                color = "#c39eff"
                width = 3

            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
