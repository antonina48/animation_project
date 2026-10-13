"""Модуль управления жизненным циклом приложения и главным окном интерфейса."""

import tkinter as tk
from src.models.animation_model import RainModel
from src.renderers.renderer import Renderer
from src.widgets.controls import ControlPanel

class App:
    """Класс графического приложения, координирующий логику, интерфейс и рендеринг."""

    def __init__(self, width: int = 800, height: int = 600) -> None:
        self.root = tk.Tk()
        self.root.title("Симуляция трехмерного дождя с управлением")
        self.root.resizable(False, False)

        self.width = width
        self.height = height

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.model = RainModel(width=self.width, height=self.height, count=150)

        self.canvas = tk.Canvas(
            self.main_frame, 
            width=self.width, 
            height=self.height, 
            bg="#0b0b1a"
        )
        self.canvas.pack(side=tk.LEFT)

        self.renderer = Renderer(self.canvas)
        self.controls = ControlPanel(self.main_frame, self._on_controls_change)
        self._is_running = True

    def _on_controls_change(self, count: int, speed_modifier: float) -> None:
        self.model.change_density(count)
        self.model.speed_modifier = speed_modifier

    def _animate(self) -> None:
        if not self._is_running:
            return
        self.model.update()
        self.renderer.render(self.model.drops)
        self.root.after(16, self._animate)

    def run(self) -> None:
        self._animate()
        self.root.mainloop()
