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
        
        # Переменные состояния анимации
        self._is_paused = False

        # Перехватываем вообще любое нажатие клавиши на клавиатуре для надежности
        self.root.bind("<Key>", self._handle_keyboard)

    def _on_controls_change(self, count: int, speed_modifier: float) -> None:
        self.model.change_density(count)
        self.model.speed_modifier = speed_modifier

    def _handle_keyboard(self, event: tk.Event) -> None:
        """Обрабатывает нажатия клавиш независимо от текущей раскладки языка."""
        # Проверяем Пробел (keysym может быть 'space' или числовым кодом)
        if event.keysym == 'space' or event.keycode == 32:
            self._toggle_pause()
            
        # Проверяем клавишу R (английская 'r'/'R' или русская 'к'/'К')
        elif event.keysym in ('r', 'R', 'Cyrillic_ka', 'Cyrillic_KA') or event.keycode == 82:
            self._reset_application()

    def _toggle_pause(self) -> None:
        """Переключает режим паузы при нажатии на пробел."""
        self._is_paused = not self._is_paused
        if not self._is_paused:
            self._animate()  # Возобновляем цикл анимации, если сняли с паузы

    def _reset_application(self) -> None:
        """Сбрасывает анимацию и слайдеры к исходному состоянию."""
        self.model.reset()
        self.controls.slider_density.set(150)
        self.controls.slider_speed.set(1.0)
        if self._is_paused:
            self._is_paused = False
            self._animate()

    def _animate(self) -> None:
        if self._is_paused:
            return  # Приостанавливаем цикл обновлений
        
        self.model.update()
        self.renderer.render(self.model.drops)
        self.root.after(16, self._animate)

    def run(self) -> None:
        self._animate()
        self.root.mainloop()
