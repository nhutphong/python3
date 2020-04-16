from __future__ import annotations
from abc import ABC, abstractmethod
from utils.decorators import design


@design("viewAbstract")
class viewAbstract(ABC):
    """
   
    """

    _state = None
    """
   
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    @design("transition_to")
    def transition_to(self, state: State):
        """
        
        """

        print(f"view: Transition to {type(state).__name__}")
        self._state = state
        self._state.view = self#view

    """
    
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
 
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

"""

@design("ProdutcState")
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


# if __name__ == "__main__":
#     print("itself")
#     view = viewAbstract(ProdutcState())
#     view.request1()
# else:
#     print("duoc import")
#     view = viewAbstract(ProdutcState())
#     view.request1()
#     # view.request2()