
import random
from typing import List, Dict

class RainModel:


    def __init__(self, width: int, height: int, count: int) -> None:
        self.width = width
        self.height = height
        self.initial_count = count
        self.speed_modifier = 1.0
        self.drops: List[Dict[str, float]] = []
        self.change_density(count)

    def _create_drop(self, init_y: bool = False) -> Dict[str, float]:
        z = random.uniform(0.1, 1.0)
        base_speed = random.uniform(6, 12) * z
        return {
            "x": random.uniform(0, self.width),
            "y": random.uniform(-100, self.height) if init_y else random.uniform(-50, -10),
            "z": z,
            "base_speed": base_speed,
            "speed": base_speed,
            "length": random.uniform(10, 25) * z
        }

    def change_density(self, target_count: int) -> None:
        current_count = len(self.drops)
        if current_count < target_count:
            for _ in range(target_count - current_count):
                self.drops.append(self._create_drop(init_y=True))
        elif current_count > target_count:
            self.drops = self.drops[:target_count]

    def reset(self) -> None:
        """Сбрасывает состояние модели к начальным параметрам."""
        self.speed_modifier = 1.0
        self.drops.clear()
        self.change_density(self.initial_count)

    def update(self) -> None:
        for drop in self.drops:
            drop["speed"] = drop["base_speed"] * self.speed_modifier
            drop["y"] += drop["speed"]
            if drop["y"] > self.height:
                new_drop = self._create_drop(init_y=False)
                drop.update(new_drop)
