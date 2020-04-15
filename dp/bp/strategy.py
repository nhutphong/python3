from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class View():
    """
    view nhu control nhan vao data ProductStrategy() call cac attr, method
    view dung getter, setter nhan vao data moi HumanStrategy() va call
    xay dung view call data, moi lan call 1 data minh dua vao

    """

    def __init__(self, strategy: Strategy) -> None:
        """
        strategy ban dau luc tao view(ProductStrategy())
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        view.strategy = HumanStrategy() #gan 1 strategy moi
        """ 
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
       
        """

        # ...

        print("view: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        # ...


class StrategyAbstract(ABC):
    """
    
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


class ProductStrategy(StrategyAbstract):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class HumanStrategy(StrategyAbstract):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
  
    view = View(ProductStrategy())
    print("Client: ProductStrategy is set to normal sorting.")
    view.do_some_business_logic()
    print()

    print("Client: HumanStrategy is set to reverse sorting.")
    view.strategy = HumanStrategy()
    view.do_some_business_logic()