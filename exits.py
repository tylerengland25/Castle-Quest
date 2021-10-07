class Exit:
    def __init__(self, name, ending):
        self.name = name
        self._ending = ending

    def print_ending(self):
        print(self._ending)
