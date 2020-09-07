


"""
nen xay dung cac abstractlass, no la khuon mau de ta iheritance xay dung cac class chua cac method=chuc nang da duoc qui dinh truoc

cac class nen viet cac method trung ten nhau, tinh polymorphism
de de quan ly va dung sau nay


cac class co cac attrs la class khac thuong la view=control 
adapter chua adaptee, adapter control adaptee


"""

class Target():
    """
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)