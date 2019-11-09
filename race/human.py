from body import Body
from body import Head

# Body = bd.Body()


class Human(Body):
    """building a Huuuuman
    """

    def getHead(self):
        self.head = HumanHead()
        self.head = self.head.getHead()

    def getLegs(self):
        pass


class HumanHead(Head):

    def getHead(self):
        return {'eyes': {'color': 'green'}}
