from body import Body
from body import Head
from body import Limbs
from body import Torso


class Human(Body):
    """building a Huuuuman
    """

    def getHead(self):
        self.head = HumanHead()
        self.head = self.head.makeReturn()

    def getLimbs(self):
        pass

    def getTorso(self):
        pass


class HumanHead(Head):

    def makeReturn(self):
        return {'eyes': {'color': 'green'}}
