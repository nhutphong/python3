from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class SubjectAbstract(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ViewSubject(SubjectAbstract):
    """
       """

    _state: int = None
    """
    
    """

    _observers: List[Observer] = []
    """
   
    """

    def attach(self, observer: Observer) -> None:
        print("view: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
     
        """

        print("view: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
     
        """

        print("\nview: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"view: My state has just changed to: {self._state}")
        self.notify()


class ObserverAbstract(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, view: ViewSubject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class ProducttObserver(ObserverAbstract):
    def update(self, view: ViewSubject) -> None:
        if view._state < 3:
            print("ProducttObserver: Reacted to the event")


class HumanObserver(ObserverAbstract):
    def update(self, view: ViewSubject) -> None:
        if view._state == 0 or view._state >= 2:
            print("HumanObserver: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    view = ViewSubject()

    product = ProducttObserver()
    view.attach(product)

    human = HumanObserver()
    view.attach(human)

    view.some_business_logic()
    view.some_business_logic()

    view.detach(product)

    view.some_business_logic()