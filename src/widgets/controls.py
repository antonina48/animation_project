"""Модуль панели графических элементов управления (слайдеров) параметрами анимации."""

import tkinter as tk
from typing import Callable


class ControlPanel:
    """Класс боковой интерактивной панели с элементами UI управления."""

    def __init__(self, parent: tk.Frame, callback: Callable[[int, float], None]) -> None:
        """Создает виджеты управления (слайдеры плотности и скорости) в окне.

        :param parent: Родительский контейнер Frame для размещения UI элементов.
        :param callback: Функция обратного вызова, принимающая новые параметры (плотность, скорость).
        """
        self.callback = callback

        # Создание боковой панели управления интерфейса
        self.frame = tk.Frame(parent, padx=15, pady=20, bg="#1a1a2e")
        self.frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Заголовок панели управления
        self.label_title = tk.Label(
            self.frame, 
            text="Параметры дождя", 
            fg="white", 
            bg="#1a1a2e", 
            font=("Arial", 12, "bold")
        )
        self.label_title.pack(pady=(0, 20))

        # Слайдер регулирования плотности генерации капель
        self.label_density = tk.Label(self.frame, text="Плотность (кол-во):", fg="white", bg="#1a1a2e")
        self.label_density.pack(anchor=tk.W)
        
        self.slider_density = tk.Scale(
            self.frame, 
            from_=10, 
            to=500, 
            orient=tk.HORIZONTAL,
            command=self._update_parameters,
            bg="#242442",
            fg="white",
            troughcolor="#1a1a2e"
        )
        self.slider_density.set(150)  # Начальное значение
        self.slider_density.pack(fill=tk.X, pady=(0, 20))

        # Слайдер регулирования скорости падения капель (эффект трехмерной скорости)
        self.label_speed = tk.Label(self.frame, text="Модификатор скорости:", fg="white", bg="#1a1a2e")
        self.label_speed.pack(anchor=tk.W)
        
        self.slider_speed = tk.Scale(
            self.frame, 
            from_=0.2, 
            to=3.0, 
            resolution=0.1, 
            orient=tk.HORIZONTAL,
            command=self._update_parameters,
            bg="#242442",
            fg="white",
            troughcolor="#1a1a2e"
        )
        self.slider_speed.set(1.0)  # Начальное значение
        self.slider_speed.pack(fill=tk.X)

    def _update_parameters(self, _: str) -> None:
        """Считывает текущие значения слайдеров и передает их через callback."""
        count = int(self.slider_density.get())
        speed_modifier = float(self.slider_speed.get())
        self.callback(count, speed_modifier)
