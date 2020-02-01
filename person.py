from generator import body_factory as bf


class Person:
    """a Composition Class that holds all attributes of a Person
    """

    class Body:
        pass

    def __init__(self):
        self.body = self.Body()
    #     self.Equip = Equip()

    def generatePerson(self):
        tempbody = bf.BodyFactory().Monster_ArtGen()
        for part in tempbody:
            # self.body[ =
            setattr(self.body, list(part.keys())[0] ,  part[list(part.keys())[0]] )
            # self.body =


class Equip:
    """acts as an abstract class for different Equipment Generators
    """

    def genEquip(self):
        raise NotImplementedError
