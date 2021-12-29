class Base(object):

    def __init__(self):
        self.name = "Base"

    # covered function
    def print(self):
        if self.name == "Base":
            return True
        else:
            return False

    # uncovered function
    def feature(self):
        return None


class A(Base):
    def __init__(self):
        super().__init__()
        self.name = "A"
