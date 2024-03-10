from S1E7 import Baratheon, Lannister


class King(Lannister, Baratheon):
    """ :: CLASS Character (Baratheron) """

    def __init__(self, name: str, is_alive: bool = True):
        """ :: __init__ King initialization """
        super().__init__(name, is_alive)

    def get_eyes(self):
        """ :: METHOD eyes getter """
        return self.eyes

    def get_hairs(self):
        """ :: METHOD eyes getter """
        return self.hairs

    def set_eyes(self, eyes):
        """ :: METHOD eyes setter """
        self.eyes = eyes
        return self.hairs

    def set_hairs(self, hair):
        """ :: METHOD hairs setter """
        self.hairs = hair
