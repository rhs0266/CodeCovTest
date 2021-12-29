class Base(object):

    def __init__(self):
        self.name = "Base"

    def print(self):
        if self.name == "Base":
            return True
        else:
            return False


class A(Base):
    def __init__(self):
        super().__init__()
        self.name = "A"
