class PrintMixin:

    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join([f'{key}={value}' for key, value in self.__dict__.items()])})"