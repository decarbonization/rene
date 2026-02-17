from abc import ABC, abstractmethod


class Keyboard(ABC):
    @abstractmethod
    def show_keyboard(self): ...

    @abstractmethod
    def hide_keyboard(self): ...
