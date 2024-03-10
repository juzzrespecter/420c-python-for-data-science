from abc import ABC, abstractmethod


class Character(ABC):
    """ :: CLASS Character (Abstract Class) """

    @abstractmethod
    def __init__(self, name: str, is_alive: bool = True):
        """ :: __init__ Character initialization """
        self.first_name = name
        self.is_alive = is_alive

    def die(self):
        """ :: METHOD Murders a character (stark) """
        self.is_alive = False


class Stark(Character):
    """ :: CLASS Stark """
    def __init__(self, name: str, is_alive: bool = True):
        """ :: __init__ Stark initialization """
        super().__init__(name, is_alive)
