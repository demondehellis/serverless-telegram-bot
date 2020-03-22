class Cat():
    """Cat"""
    def __init__(self, params = {}):
        self._params = params

    def params(self, params = None):
        if params is not None:
            self._params = params
        return self._params

    def param(self, key, value = None):
        if value is not None:
            self._params[key] = value

        return self._params[key]

    def energy(self, value = None):
        return self.param('energy', value)

    def hunger(self, value = None):
        return self.param('hunger', value)

    def tick(self):
        self.energy(self.energy() - 1)
        self.hunger(self.hunger() + 1)
