

class BuilderBaseClass:
    """
    Базовый класс для билдера. Можно дополнить ещё другими полезными
    методами.
    """
    def __init__(self):
        self.result = {}

    def build(self):
        return self.result
