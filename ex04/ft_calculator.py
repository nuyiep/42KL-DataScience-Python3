
class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Dot product'''
        zipped_num = zip(V1, V2)
        new_vec = []
        for (a, b) in zipped_num:
            product = a * b
            new_vec.append(product)
        results = 0
        for i in new_vec:
            results = results + i
        print(f"Dot product is: {results}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Add vec'''
        zipped_num = zip(V1, V2)
        new_vec = []
        for (a, b) in zipped_num:
            sum = float(a) + float(b)
            new_vec.append(sum)
        print(f"Add Vector is: {new_vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Sous vec- sous in French means 'under' or 'below'''
        # zipped_num = zip(V1, V2)
        new_vec = [float(a - b) for (a, b) in zip(V1, V2)]
        # new_vec = []
        # for (a, b) in zipped_num:
        # 	minus = float(a) - float(b)
        # 	new_vec.append(minus)
        print(f"Sous Vector is: {new_vec}")
