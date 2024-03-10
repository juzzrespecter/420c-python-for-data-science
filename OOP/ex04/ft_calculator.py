class calculator:
    """ :: CLASS calculator """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """ MEHTOD dotproduct """
        print(f'Dot product is {sum([v1 * v2 for v1, v2 in zip(V1, V2)])}')

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """ METHOD addvector """
        print(f'Add vector is {[v1 + v2 for v1, v2 in zip(V1, V2)]}')

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """ METHOD susvector """
        print(f'Sus vector is {[v1 - v2 for v1, v2 in zip(V1, V2)]}')
