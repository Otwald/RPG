class Body:
    """acts as an abstract Class for different Body generators
    """

    def getHead(self):
        raise NotImplementedError

    def getLimbs(self):
        raise NotImplementedError

    def getTorso(self):
        raise NotImplementedError

    def genBody(self):
        self.getHead()
        self.getLimbs()
        self.getTorso()


class Head:

    def makeReturn(self):
        raise NotImplementedError

class Limbs:
    
    def makeReturn(self):
        raise NotImplementedError

class Torso:
    
    def makeReturn(self):
        raise NotImplementedError

