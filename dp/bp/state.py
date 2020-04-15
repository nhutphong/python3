from __future__ import annotations
from abc import ABC, abstractmethod
from dp.decorators import design


class viewAbstract(ABC):
    """
    The view defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the view.
    """

    _state = None
    """
    A reference to the current state of the view.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    @design("transition_to")
    def transition_to(self, state: State):
        """
        The view allows changing the State object at runtime.
        """

        print(f"view: Transition to {type(state).__name__}")
        self._state = state
        self._state.view = self#view

    """
    The view delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the view object,
    associated with the State. This backreference can be used by States to
    transition the view to another State.
    """

    @property
    def view(self) -> view:
        return self._view

    @view.setter
    def view(self, view: view) -> None:
        self._view = view

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
view.
"""


class ProdutcState(State):
    def handle1(self) -> None:
        print("ProdutcState handles request1.")
        print("ProdutcState wants to change the state of the view.")
        self.view.transition_to(HumanState())

    def handle2(self) -> None:
        print("ProdutcState handles request2.")


class HumanState(State):
    def handle1(self) -> None:
        print("HumanState handles request1.")

    def handle2(self) -> None:
        print("HumanState handles request2.")
        print("HumanState wants to change the state of the view.")
        self.view.transition_to(ProdutcState())


if __name__ == "__main__":
    # The client code.

    view = viewAbstract(ProdutcState())
    view.request1()
    # view.request2()