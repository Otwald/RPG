class Body:
    """acts as an abstract Class for different Body generators
    """

    def getHead(self):
        raise NotImplementedError

    def getLegs(self):
        raise NotImplementedError

    def genBody(self):
        self.getHead()
        self.getLegs()


class Head:
    pass

