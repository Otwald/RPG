from monster_gen import BodyFactory


class Person:
    """a Composition Class that holds all attributes of a Person
    """

    # def __init__(self):
    #     self.body = Body()
    #     self.Equip = Equip()

    def generatePerson(self):
        self.body = BodyFactory().Monster_ArtGen()
        self.body.genBody()

class Equip:
    """acts as an abstract class for different Equipment Generators
    """

    def genEquip(self):
        raise NotImplementedError