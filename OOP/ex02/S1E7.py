from S1E9 import Character


class Baratheon(Character):
    """ :: CLASS Character (Baratheron) """

    def __init__(self, name: str, is_alive: bool = True):
        """ :: __init__ Baratheon initialization """
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
        super().__init__(name, is_alive)

    def __str__(self):
        """ :: METHOD __str__ for Baratheon """
        return f'Baratheon: name {self.first_name}, eyes {self.eyes}'

    def __repr__(self):
        """ :: METHOD __repr__ for Baratheon """
        return f'Baratheon: name {self.first_name}, eyes {self.eyes}'

    @classmethod
    def create_baratheon(cls, name, is_alive):
        """ :: MEHOD factory func. for Baratheon """
        return cls(name, is_alive)


class Lannister(Character):
    """ :: CLASS Character (Lannister) """

    def __init__(self, name: str, is_alive: bool = True):
        """ :: __init__ Lannister initialization """
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
        super().__init__(name, is_alive)

    def __str__(self):
        """ :: METHOD __str__ for Lannister """
        return f'Lannister: name {self.first_name}, eyes {self.eyes}'

    def __repr__(self):
        """ :: METHOD __repr__ for Lannister """
        return f'Lannister: name {self.first_name}, eyes {self.eyes}'

    @classmethod
    def create_lannister(cls, name, is_alive):
        """ :: MEHOD factory func. for Lannister """
        return cls(name, is_alive)
