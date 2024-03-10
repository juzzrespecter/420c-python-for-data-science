from sys import stderr


class calculator:
    """ :: CLASS calculator """
    def __init__(self, v):
        """ :: __init__ ft_calculator initialization """
        self.__vector = v

    def __add__(self, rhs) -> None:
        """ :: METHOD add operation overload """
        try:
            self.__vector = [v + rhs for v in self.__vector]
            print(self.__vector)
        except TypeError as e:
            print(f'{type(e).__name__}: {e}', file=stderr)

    def __mul__(self, rhs) -> None:
        """ :: METHOD multiply operation overload """
        try:
            self.__vector = [v * rhs for v in self.__vector]
            print(self.__vector)
        except TypeError as e:
            print(f'{type(e).__name__}: {e}', file=stderr)

    def __sub__(self, rhs) -> None:
        """ :: METHOD substraction operation overload """
        try:
            self.__vector = [v - rhs for v in self.__vector]
            print(self.__vector)
        except TypeError as e:
            print(f'{type(e).__name__}: {e}', file=stderr)

    def __truediv__(self, rhs) -> None:
        """ :: METHOD division operation overload """
        try:
            self.__vector = [v / rhs for v in self.__vector]
            print(self.__vector)
        except ZeroDivisionError:
            print('Bad division by zero', file=stderr)
        except TypeError as e:
            print(f'{type(e).__name__}: {e}', file=stderr)
