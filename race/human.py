from body import Body
# from body import Head
# from body import Limbs
# from body import Torso


class Human(Body):
    """building a Huuuuman
    """

    def __init__(self):
        super().__init__('human')

    def getHead(self):
        self.head = self.getParts(self.bodyParts, 'head')

    def getLimbs(self):
        self.limbs = self.getParts(self.bodyParts, 'limbs')

    def getTorso(self):
        self.torso = self.getParts(self.bodyParts, 'torso')


# class HumanHead(Head):

#     def makeReturn(self):
#         return {'eyes': {'color': 'green'}}
