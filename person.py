from generator import body_factory as bf


class Person:
    """a Composition Class that holds all attributes of a Person
    """

    class Body:
        head: dict = {}
        torso: dict = {}
        limps: dict = {}

    def __init__(self):
        self.body = self.Body()

    def generatePerson(self):
        tempbody = bf.BodyFactory().Monster_ArtGen()
        for part in tempbody:
            setattr(self.body, list(part.keys())[
                    0],  part[list(part.keys())[0]])


class Equip:
    """acts as an abstract class for different Equipment Generators
    """

    def genEquip(self):
        raise NotImplementedError
