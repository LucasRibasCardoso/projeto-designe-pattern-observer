from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    
    @abstractmethod
    def update(self, episodio: str) -> None:
        pass


class Subject(ABC):
    
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self, episodio: str) -> None:
        pass
